from PySide6.QtCore import (QCoreApplication,QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QGridLayout, QGroupBox, QHBoxLayout,QWidget , QLabel, QPushButton, QSizePolicy, QSpacerItem, QLabel)
from PySide6.QtWebEngineWidgets import QWebEngineView

class Ui_Dialog_Preview_Pdf(object):
    def setupUi(self, Dialog_Preview_Pdf):
        if not Dialog_Preview_Pdf.objectName():
            Dialog_Preview_Pdf.setObjectName(u"Dialog_Preview_Pdf")
        Dialog_Preview_Pdf.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dialog_Preview_Pdf.setEnabled(True)
        Dialog_Preview_Pdf.resize(950, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_Preview_Pdf.sizePolicy().hasHeightForWidth())
        Dialog_Preview_Pdf.setSizePolicy(sizePolicy)
        Dialog_Preview_Pdf.setMinimumSize(QSize(850, 768))
        Dialog_Preview_Pdf.setMaximumSize(QSize(950, 768))
        Dialog_Preview_Pdf.setStyleSheet(u"QDialog#Dialog_Preview_Pdf {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 86, 115, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        Dialog_Preview_Pdf.setModal(True)
        self.frame = QFrame(Dialog_Preview_Pdf)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, 70, 952, 701))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(921, 701))
        self.frame.setMaximumSize(QSize(952, 701))
        self.frame.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QGroupBox */\n"
"QGroupBox {\n"
"border: 1px solid ;\n"
"border-radius: 5px;\n"
"border-color:#003f50;\n"
"background-color: transparent;\n"
"}\n"
"\n")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(1)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.groupBox_action = QGroupBox(self.frame)
        self.groupBox_action.setObjectName(u"groupBox_action")
        sizePolicy.setHeightForWidth(self.groupBox_action.sizePolicy().hasHeightForWidth())
        self.groupBox_action.setSizePolicy(sizePolicy)
        self.groupBox_action.setMinimumSize(QSize(180, 85))
        font = QFont()
        font.setBold(False)
        self.groupBox_action.setFont(font)
        self.btn_out_viewer = QPushButton(self.groupBox_action)
        self.btn_out_viewer.setObjectName(u"btn_out_viewer")
        self.btn_out_viewer.setGeometry(QRect(30, 20, 120, 41))
        self.btn_out_viewer.setMinimumSize(QSize(120, 40))
        self.btn_out_viewer.setMaximumSize(QSize(120, 41))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(11)
        self.btn_out_viewer.setFont(font1)
        self.btn_out_viewer.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #bcbcbc  ;\n"
"border-radius: 5px; \n"
"background-color:  #7ad17a;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"color: #ffffff;\n"
"background-color: #00aa00;\n"
"border: 1px solid #00aaff ;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"color: #ffffff;\n"
"background-color: #ffaa00;\n"
"border: 1px solid #69cdff ;\n"
"}")

        self.horizontalLayout_2.addWidget(self.groupBox_action)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.groupbox_preview = QGroupBox(self.frame)
        self.groupbox_preview.setObjectName(u"groupbox_preview")
        self.groupbox_preview.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupbox_preview.sizePolicy().hasHeightForWidth())
        self.groupbox_preview.setSizePolicy(sizePolicy1)
        self.groupbox_preview.setMinimumSize(QSize(901, 580))
        self.groupbox_preview.setMaximumSize(QSize(932, 588))
        self.groupbox_preview.setAutoFillBackground(False)
        self.groupbox_preview.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.gridLayout_3 = QGridLayout(self.groupbox_preview)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(5)
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(5, 20, 5, 5)
        self.webEngineView = QWebEngineView(self.groupbox_preview)
        self.webEngineView.setObjectName(u"webEngineView")
        sizePolicy1.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.webEngineView.setFont(font2)

        self.gridLayout_3.addWidget(self.webEngineView, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.groupbox_preview, 0, 0, 1, 1)

        self.horizontalLayoutWidget = QWidget(Dialog_Preview_Pdf)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 941, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 10)
        self.label_headboard = QLabel(self.horizontalLayoutWidget)
        self.label_headboard.setObjectName(u"label_headboard")
        sizePolicy.setHeightForWidth(self.label_headboard.sizePolicy().hasHeightForWidth())
        self.label_headboard.setSizePolicy(sizePolicy)
        self.label_headboard.setMinimumSize(QSize(270, 60))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Black"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.label_headboard.setFont(font3)
        self.label_headboard.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_headboard)

        self.print_pdf = QPushButton(self.horizontalLayoutWidget)
        self.print_pdf.setObjectName(u"print_pdf")
        sizePolicy.setHeightForWidth(self.print_pdf.sizePolicy().hasHeightForWidth())
        self.print_pdf.setSizePolicy(sizePolicy)
        self.print_pdf.setMinimumSize(QSize(30, 30))
        self.print_pdf.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid transparent ;\n"
"border-radius: 5px; \n"
"background-color:  transparent;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"color: #ffffff;\n"
"background-color: #f6b565;\n"
"border: 1px solid #7f8c8d;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"color: #ffffff;\n"
"background-color: #ffaa00;\n"
"border: 2px solid transparent ;\n"
"}")

        self.horizontalLayout.addWidget(self.print_pdf)

        self.save_us_pdf = QPushButton(self.horizontalLayoutWidget)
        self.save_us_pdf.setObjectName(u"save_us_pdf")
        sizePolicy.setHeightForWidth(self.save_us_pdf.sizePolicy().hasHeightForWidth())
        self.save_us_pdf.setSizePolicy(sizePolicy)
        self.save_us_pdf.setMinimumSize(QSize(30, 30))
        self.save_us_pdf.setStyleSheet(u"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid transparent ;\n"
"border-radius: 5px; \n"
"background-color:  transparent;\n"
"}\n"
"            \n"
"QPushButton:hover {\n"
"color: #ffffff;\n"
"background-color: #f6b565;\n"
"border: 1px solid #7f8c8d;\n"
"}\n"
"\n"
"QPushButton:pressed { \n"
"color: #ffffff;\n"
"background-color: #ffaa00;\n"
"border: 2px solid transparent ;\n"
"}")

        self.horizontalLayout.addWidget(self.save_us_pdf)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.retranslateUi(Dialog_Preview_Pdf)

        QMetaObject.connectSlotsByName(Dialog_Preview_Pdf)
    # setupUi

    def retranslateUi(self, Dialog_Preview_Pdf):
        Dialog_Preview_Pdf.setWindowTitle(QCoreApplication.translate("Dialog_Preview_Pdf", u"Dialog", None))
        self.groupBox_action.setTitle(QCoreApplication.translate("Dialog_Preview_Pdf", u"Acci\u00f3n", None))
#if QT_CONFIG(tooltip)
        self.btn_out_viewer.setToolTip(QCoreApplication.translate("Dialog_Preview_Pdf", u"Salir", None))
#endif // QT_CONFIG(tooltip)
        self.btn_out_viewer.setText(QCoreApplication.translate("Dialog_Preview_Pdf", u"\u2714 Salir", None))
        self.groupbox_preview.setTitle(QCoreApplication.translate("Dialog_Preview_Pdf", u"Preview", None))
        self.label_headboard.setText(QCoreApplication.translate("Dialog_Preview_Pdf", u"Previsualizaci\u00f3n", None))
        self.print_pdf.setText("")
        self.save_us_pdf.setText("")
    # retranslateUi

