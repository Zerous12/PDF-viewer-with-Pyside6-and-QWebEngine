import sys
from PySide6.QtWidgets import QApplication

from module.pdf_previewer_functions import PdfViewDialog


class App():
    def __init__(self):
        self.app = QApplication([]) # Inicializa la aplicación Qt        
        self.preview_panel = PdfViewDialog()
        self.preview_panel.show()
        
    def run(self):
        try:
            sys.exit(self.app.exec())         
        except SystemExit: 
            pass
    
#////////////////////////////////////////////////Main/////////////////////////////////////////////////////

if __name__ == "__main__": 
    application = App()   
    application.run()  