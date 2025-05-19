from PySide6.QtCore import QTimer, QUrl, QStandardPaths, QTemporaryFile
from PySide6.QtWidgets import QMessageBox,  QDialog, QFileDialog
from PySide6.QtGui import QIcon

from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWebEngineCore import QWebEngineSettings

import win32print
import shutil
import os, gc

from module.pdf_previewer_ui import Ui_Dialog_Preview_Pdf
from utils.widgets.rotating_circle import WaitingCircle

class PdfViewDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog_Preview_Pdf()
        self.ui.setupUi(self)
        self.setWindowTitle("Preview PDF")
        self.setFixedSize(self.width(), self.height())
        self.configure_button_aux_viewer()
        self.webview = self.ui.webEngineView        
        self.webview.setZoomFactor(1)
        self.web_settings = self.webview.settings()
        self.web_settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        self.loading_indicator = WaitingCircle(parent=self)
        self.loading_indicator.hide()
        self.start_page = 1
        
        self.pdf_path = ""
        script_directory = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.abspath(os.path.join(script_directory, ".."))
        self.pdf_js_path = os.path.join(project_root, "utils" ,"pdfjs", "web", "viewer.html").replace('\\', '/')
        
        self.output_pdf_directory = os.path.join(project_root, "docs").replace('\\', '/')  
              
        self.webview.page().profile().downloadRequested.connect(self._handle_download)
        self.webview.page().printRequested.connect(self._handle_print_request)        
        self.ui.btn_out_viewer.clicked.connect(self.out_button_clicked)
        self.delay_dialog_charge_data()        

    def configure_button_aux_viewer(self):
        self.ui.print_pdf.setIcon(QIcon("utils/icons/icon_printer.png"))
        self.ui.print_pdf.clicked.connect(self._handle_print_request)
        self.ui.print_pdf.setToolTip("Imprimir PDF")
        self.ui.print_pdf.setVisible(False)
        self.ui.save_us_pdf.setIcon(QIcon("utils/icons/icon_download_pdf.png"))
        self.ui.save_us_pdf.clicked.connect(self.simulate_pdfjs_download)
        self.ui.save_us_pdf.setToolTip("Guardar PDF")
        self.ui.save_us_pdf.setVisible(False)

    def configure_button_visibility(self):
        self.ui.print_pdf.setVisible(True)
        self.ui.save_us_pdf.setVisible(True)

    def simulate_pdfjs_download(self):
        js_code = """
            (function() {
                let downloadButton = document.querySelector("#download");
                if (downloadButton) {
                    downloadButton.click();
                    return "Descarga iniciada.";
                } else {
                    return "Botón de descarga no encontrado.";
                }
            })();
        """
        self.webview.page().runJavaScript(js_code, self._on_js_result)

    def _on_js_result(self, result):
        print(f"Resultado JS: {result}")

    def _force_repaint(self):       
        self.webview.resize(self.webview.width()+1, self.webview.height())  # trigger layout
        self.webview.resize(self.webview.width()-1, self.webview.height())  # restore

    def delay_dialog_charge_data(self):
        self.loading_indicator.start()
        QTimer.singleShot(500, self.load_pdf_from_path)       

    def load_pdf_from_path(self):
        try:
            os.makedirs(self.output_pdf_directory, exist_ok=True)
            self.pdf_source_path = os.path.join(self.output_pdf_directory, "PDF Test File HTML5.pdf").replace('\\', '/')
            if not os.path.isfile(self.pdf_source_path):
                raise FileNotFoundError("PDF de origen no encontrado.")

            # Crear archivo temporal sin pasarle la ruta de uno existente
            self.temp_pdf_file = QTemporaryFile(self)
            self.temp_pdf_file.setAutoRemove(False)

            if not self.temp_pdf_file.open():
                raise Exception("No se pudo crear archivo temporal.")

            # Copiar el contenido del PDF al archivo temporal
            temp_path = self.temp_pdf_file.fileName()
            shutil.copyfile(self.pdf_source_path, temp_path)

            self.pdf_path = temp_path
            print(f"PDF temporal creado: {self.pdf_path}")

        except Exception as e:
            self.webview.setHtml(f"<h2 style='color:red;'>Error al cargar PDF</h2><p>{str(e)}</p>")
        finally:            
            self._preview()

    def _preview(self):
        """Muestra el PDF y gestiona las descargas"""     
        def enable_downloads():
            self.webview.loadFinished.disconnect(enable_downloads)        
        self.webview.loadFinished.connect(enable_downloads)
        self.webview.loadFinished.connect(self.configure_button_visibility)
        self.webview.loadFinished.connect(self.loading_indicator.stop())        
        self.load_pdf()
        QTimer.singleShot(100, self._force_repaint)

    def load_pdf(self):
        self.webview.load(QUrl.fromUserInput(f'file:///{self.pdf_js_path}?file=file:///{self.pdf_path}#page={self.start_page}'))
        print(f"self.pdf_path: {self.pdf_path}")
        print(f"self.pdf_js_path: {self.pdf_js_path}")        

    def _handle_print_request(self):
        if not os.path.exists(self.pdf_path):
                QMessageBox.warning(self, "Error", "Archivo PDF no disponible.")
                return

        # Crear objeto QPrinter
        printer = QPrinter(QPrinter.HighResolution)

        # Mostrar diálogo de selección de impresora
        dialog = QPrintDialog(printer, self)
        dialog.setWindowTitle("Seleccionar impresora")
        if dialog.exec() != QDialog.Accepted:
            QMessageBox.information(self, "Cancelado", "No se seleccionó impresora.")
            return

        # Obtener nombre de la impresora seleccionada
        printer_name = printer.printerName()
        print(f"Impresora seleccionada: {printer_name}")

        try:
            # Imprimir directamente con win32print
            hPrinter = win32print.OpenPrinter(printer_name)
            job_info = ("Impresión desde PDF Viewer", None, "RAW")
            win32print.StartDocPrinter(hPrinter, 1, job_info)
            win32print.StartPagePrinter(hPrinter)

            with open(self.pdf_path, "rb") as f:
                win32print.WritePrinter(hPrinter, f.read())

            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)
            print(f"Archivo enviado a: {printer_name}")

        except Exception as e:
            QMessageBox.critical(self, "Error de impresión", str(e))

        finally:
            if 'hPrinter' in locals():
                win32print.ClosePrinter(hPrinter)

    def _handle_download(self, download_item):
        print("Presiono el botón de descargar")
        """Manejo moderno de descargas en PySide6"""
        try: 
            # Configurar nombre sugerido            
            suggested_name = f"Test_Download_PDF.pdf"
            default_path = os.path.join(
                QStandardPaths.writableLocation(QStandardPaths.DownloadLocation),
                suggested_name
            )
            # Creamos un diálogo modal independiente
            dialog = QFileDialog(self, "Guardar PDF", default_path, "PDF Files (*.pdf)")
            dialog.setFileMode(QFileDialog.AnyFile)
            dialog.setAcceptMode(QFileDialog.AcceptSave)
            dialog.setModal(True)

            if dialog.exec() == QDialog.Accepted:
                selected_files = dialog.selectedFiles()
                if selected_files:
                    path = selected_files[0]
                    download_item.setDownloadDirectory(os.path.dirname(path))
                    download_item.setDownloadFileName(os.path.basename(path))
                    download_item.accept()
                else:
                    download_item.cancel()
            else:
                download_item.cancel()
                # Limpieza adicional para evitar reintentos
                self._cleanup_after_cancel()

        except Exception as e:
            download_item.cancel()
            QMessageBox.warning(self, "Error", f"No se pudo iniciar la descarga:\n{str(e)}")    

    def _cleanup_after_cancel(self):
        """Limpieza exhaustiva después de cancelar"""
        # Forzar garbage collection del diálogo
        gc.collect()
        # Limpiar cachés del WebEngine
        self.webview.page().profile().clearHttpCache()
        self.webview.page().profile().clearAllVisitedLinks()          
    
    def out_button_clicked(self):
        self.clear_input_fields()
        self.reject()

    def closeEvent(self, event):
        self.clear_input_fields()
        super().closeEvent(event)

    def clear_temp_pdf_file(self):
        if os.path.exists(self.pdf_path) and self.temp_pdf_file.isOpen():
            try:
                self.temp_pdf_file.close()
                self.temp_pdf_file.remove()
            except Exception as e:
                print(f"Error al cerrar archivo temporal: {str(e)}")

    def clear_webview_data(self):
        self.webview.page().profile().downloadRequested.disconnect()
        self.webview.page().printRequested.disconnect()
        self.webview.page().profile().clearAllVisitedLinks()
        self.webview.close()

    def clear_input_fields(self):  
        self.clear_webview_data()
        self.clear_temp_pdf_file()
        self.pdf_path = None
        self.ot_info = None
        self.output_pdf_directory = None
