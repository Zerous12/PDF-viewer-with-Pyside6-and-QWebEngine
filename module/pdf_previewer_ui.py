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
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTabWidget */\n"
"QTabWidget {\n"
"border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	color: #ffffff;\n"
"    font-size: 13px;	\n"
"	font-family: \"Segoe UI\";\n"
"    font-weight: bold;\n"
"    background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"    padding: 6px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.903409 rgba(240, 240, 240, 255), stop:0.931818 rgba(0, 170, 255, 255));\n"
"	color: #000000;\n"
"	border-top: 2px solid #00aaff;\n"
"	border-bottom: 2px solid;\n"
"	border: transparent;\n"
"	min-width: 120px;\n"
"}\n"
"QTab"
                        "Bar::tab:hover {	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.903409 rgba(42, 48,55, 255), stop:0.931818 rgba(246, 181, 101, 255));\n"
"	color: #ffffff;\n"
"	border-top: 2px solid #ffaa00;\n"
"	border: transparent;	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 2px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(35, 35, 35);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item {\n"
"	font-size: 10px;\n"
"	font-family: \"Segoe UI\";\n"
"	font-weight: normal;\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(33, 37, 43);\n"
"}\n"
"QTableWidget::item:selected {	\n"
"	background-color: rgb(0, 50,120);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget::horizont"
                        "alHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView {\n"
" background-color: transparent;\n"
"}\n"
"QHeaderView::section {\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QHeaderView::section:horizontal {\n"
"	color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QToolButton */\n"
"QToolButton {\n"
"    background-color: rgb(0, 170, 127);\n"
"    margin: 0px;\n"
"    padding: 2px;\n"
"}\n"
"QToolButton::menu-button {\n"
"padding: 2px;\n"
"/* 16px width + 4px for border = 20px allocated above *"
                        "/\n"
"width: 16px;\n"
"outline: none;		\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QToolButton::menu-arrow {\n"
"height: 24px;\n"
"width: 24px;    \n"
"}\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #7f8c8d;\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"   background-color: #46aa8f;   \n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"   background-color:  #58d2b2;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: marg"
                        "in;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::left-arrow:horizontal {\n"
"    border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"    border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:hover, QScrollBar::right-arrow:horizontal:hover {\n"
"    background: #46aa8f;\n"
"}\n"
"QScrollBar::left-arrow:horizontal:pressed, QScrollBar::right-arrow:horizontal:pressed {\n"
"    background: #58d2b2;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	borde"
                        "r: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"	background: #7f8c8d;\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::handle:vertical:hover {\n"
"	background-color: #46aa8f;   \n"
" }\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background-color:  #58d2b2;   \n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical{\n"
"  border-top-left-radius: 4px;\n"
""
                        "  border-top-right-radius: 4px;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border-bottom-left-radius: 4px;\n"
"   border-bottom-right-radius: 4px;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
" }\n"
" QScrollBar::up-arrow:vertical:hover, QScrollBar::down-arrow:vertical:hover {\n"
"    background: #46aa8f;\n"
" }\n"
"QScrollBar::up-arrow:vertical:pressed, QScrollBar::down-arrow:vertical:pressed {\n"
"     background: #58d2b2;\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CalendarWidget */\n"
"QDateEdit {	\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(33, 37, 43);\n"
"	padding: 2px;\n"
"	padding-left: 8px;\n"
"}\n"
"QDateEdit::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-lef"
                        "t-color: rgb(33, 37, 43);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/icon_menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(33, 37, 43);\n"
" }\n"
"QDateEdit::drop-down:selected {\n"
"    border-left-color:  rgb(0, 163, 245);\n"
"	background-color: rgb(0, 163, 245);\n"
"}\n"
"\n"
"QDateEdit::drop-down:pressed {\n"
"    border-left-color:   rgb(246, 181, 101);\n"
"    background-color: rgb(246, 181, 101);\n"
"}\n"
"	\n"
"QCalendarWidget QWidget{\n"
"	alternate-background-color: #ace0fa; 	\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth,\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"	border: no"
                        "ne;\n"
"	qproperty-icon: none;\n"
"	min-width: 16px;\n"
"	max-width: 16px;\n"
"	min-height: 16px;\n"
"	max-height: 16px;\n"
"	border-radius: 3px;\n"
"	background-color: transparent;\n"
"	padding: 5px;\n"
"	}\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth{\n"
"	margin-right: 5px; \n"
"	padding-left: 5px;\n"
"	image: url(:/icons/images/icons/cil-chevron-right.png);\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth{\n"
"	margin-left: 5px;\n"
"	image: url(:/icons/images/icons/cil-chevron-left.png);\n"
"} \n"
"QCalendarWidget QWidget#qt_calendar_prevmonth:hover,\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth:hover{\n"
"	background-color: #46aac4;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_prevmonth:pressed,\n"
"QCalendarWidget QWidget#qt_calendar_nextmonth:pressed{\n"
"	background-color: #ffaa00;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton{\n"
"	color: rgb(255, 255, 255);\n"
"	margin: 5px;\n"
"	font-size: 13px;\n"
"	border-radius: 3px;\n"
"	background-color: transparent;\n"
"	paddin"
                        "g: 0px 10px;\n"
"	margin-left: 15px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton{\n"
"	width: 70px;\n"
"	min-height: 22px;\n"
"	max-height: 22px;\n"
"	color: rgb(255, 255, 255);\n"
"	font-size: 13px;\n"
"	background-color: transparent;\n"
"	border-radius: 3px;\n"
"	padding: 5px 2px;\n"
"	margin: 5px 0px;\n"
"	margin-right: 20px;\n"
"	margin-left: 1px;	\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton:hover,\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton:hover{\n"
"	background-color: #46aac4;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_yearbutton:pressed,\n"
"QCalendarWidget QWidget#qt_calendar_monthbutton:pressed{\n"
"	background-color: #46aa8f;\n"
"	color: #ffffff;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit{\n"
"	width: 60px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	font-size: 13px;\n"
"	font-weight: bold;	\n"
"	margin-left: 3px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::down-button{\n"
"	backgroun"
                        "d-image: url(:/icons/images/icons/cil-caret-bottom.png);\n"
"	subcontrol-position: left;\n"
"	subcontrol-origin: margin;\n"
"	margin: 5px 0px;	\n"
"    background-repeat: no-repeat; \n"
"    background-position: center; \n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button{\n"
"	background-image: url(:/icons/images/icons/cil-caret-top.png);\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin; \n"
"	margin: 5px 0px;\n"
"	margin-left: 0px;\n"
"	margin-right: 0px;	\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::down-button,\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button{\n"
"	border-color: transparent;\n"
"	width: 24px;\n"
"	height: 24px;\n"
"	border-radius: 12px;	\n"
"	background-color: transparent;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::down-button:hover,\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button:hover{\n"
"	background-color: #46aac4;\n"
"	color: #ffff"
                        "ff;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::down-button:pressed,\n"
"QCalendarWidget QWidget#qt_calendar_yearedit::up-button:pressed{\n"
"	background-color: #ffaa00;\n"
"	color: #ffffff;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_calendarview{\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	background-color: #fbfbfb;\n"
"	border-top: transparent;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-left-radius: 2px;\n"
"	border-bottom-right-radius: 2px;\n"
"	padding: 0px 0px 0px 0px;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_calendarview::item:hover{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(0, 170, 255);\n"
"	color: #ffffff;\n"
"}\n"
"QCalendarWidget QWidget#qt_calendar_calendarview::item:selected{\n"
"	border-radius: 3px;\n"
"	background-color: rgb(0, 170, 127);\n"
"}\n"
"QCalendarWidget QMenu {\n"
"	background-color: rgb(255, 255,255);\n"
"	margin: 2px;\n"
"	border-radius:  3px;\n"
"}\n"
"QCalendarWidget QMenu::item {\n"
"    padding: 2px 25px"
                        " 2px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"QCalendarWidget QMenu::item:selected {\n"
"	background-color: rgb(0, 170, 255); \n"
"	color: rgb(255, 255, 255); \n"
"}\n"
"QCalendarWidget QMenu::item:enabled:pressed {\n"
"    background-color: #ffaa00;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Menu */\n"
"QMenu{\n"
"    margin: 2px;\n"
"	border-radius:  3px;\n"
"}\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent;\n"
"}\n"
"QMenu::item:enabled:selected {    \n"
"    background: #009fef;\n"
"	color: #ffffff;\n"
"}\n"
"QMenu::icon:checked {\n"
"    background: gray;\n"
"    border: 1px inset gray;\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"}\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: #4f4f4f;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
""
                        "    height: 13px;\n"
"}\n"
"QMenu::item:disabled {\n"
"	color: #a2a2a2;\n"
"}\n"
"QMenu::item:enabled:pressed {\n"
"    background-color: #ffaa00;\n"
"}")
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

