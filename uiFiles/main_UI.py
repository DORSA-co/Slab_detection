# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1006, 609)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setMinimumSize(QSize(0, 40))
        self.top_frame.setStyleSheet(u"QFrame{\n"
"background-color:#16222A;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"}")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(779, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.minimize_btn = QPushButton(self.top_frame)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_btn.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.maximize_btn = QPushButton(self.top_frame)
        self.maximize_btn.setObjectName(u"maximize_btn")
        self.maximize_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_btn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.maximize_btn)

        self.close_btn = QPushButton(self.top_frame)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.top_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.side_frame = QFrame(self.centralwidget)
        self.side_frame.setObjectName(u"side_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.side_frame.sizePolicy().hasHeightForWidth())
        self.side_frame.setSizePolicy(sizePolicy1)
        self.side_frame.setMinimumSize(QSize(150, 0))
        self.side_frame.setStyleSheet(u"#side_frame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3A6073, stop:0.75 #16222A)\n"
"}\n"
"\n"
"QPushButton{\n"
"border: 0px;\n"
"color: white;\n"
"font-weight: bold;\n"
"padding: 15px 10px;\n"
"font-size:12px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,20);\n"
"\n"
"}")
        self.side_frame.setFrameShape(QFrame.StyledPanel)
        self.side_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_image_btn = QPushButton(self.side_frame)
        self.side_image_btn.setObjectName(u"side_image_btn")
        self.side_image_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.side_image_btn.setStyleSheet(u"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #3A6073, stop: 0.029 #3A6073, stop: 0.03 rgba(120, 146, 223, 40), stop: 1 rgba(120, 146, 223, 40))")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_image_btn.setIcon(icon3)
        self.side_image_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.side_image_btn)

        self.side_drawing_btn = QPushButton(self.side_frame)
        self.side_drawing_btn.setObjectName(u"side_drawing_btn")
        self.side_drawing_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/drawing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.side_drawing_btn.setIcon(icon4)
        self.side_drawing_btn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.side_drawing_btn)

        self.verticalSpacer = QSpacerItem(20, 518, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.side_frame)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.image_page = QWidget()
        self.image_page.setObjectName(u"image_page")
        self.verticalLayout_3 = QVBoxLayout(self.image_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 3)
        self.open_folder_btn = QPushButton(self.image_page)
        self.open_folder_btn.setObjectName(u"open_folder_btn")
        self.open_folder_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_folder_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/open_folder_hover.png);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/open_folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_folder_btn.setIcon(icon5)
        self.open_folder_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.open_folder_btn)

        self.open_file_btn = QPushButton(self.image_page)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_file_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/open_file_hover.png);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_file_btn.setIcon(icon6)
        self.open_file_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.open_file_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.tabWidget = QTabWidget(self.image_page)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget{\n"
"    font-weight: bold;\n"
" 	border: 2px solid rgba(22, 34, 42, 30);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #C4C4C3;\n"
"    background-color: Transparent;\n"
"    margin-top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    border: 1px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; \n"
"    min-width: 120px;\n"
"    padding: 2px;\n"
"	background-color: rgb(225, 225, 225);\n"
"	color: rgb(100, 100, 100)\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"	border: None;\n"
"	background-color: #16222A;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:hover{\n"
"	 background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #fafafa, stop: 0.4 #f4f4f4, stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"	border: None;\n"
"	background-color: #385c6e;\n"
"	color: white;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-"
                        "color: #C2C7CB;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px;\n"
"}")
        self.full_view_tab = QWidget()
        self.full_view_tab.setObjectName(u"full_view_tab")
        self.horizontalLayout_5 = QHBoxLayout(self.full_view_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.full_prev_btn = QPushButton(self.full_view_tab)
        self.full_prev_btn.setObjectName(u"full_prev_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.full_prev_btn.sizePolicy().hasHeightForWidth())
        self.full_prev_btn.setSizePolicy(sizePolicy2)
        self.full_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.full_prev_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/prev_hover.png);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/prev.png", QSize(), QIcon.Normal, QIcon.Off)
        self.full_prev_btn.setIcon(icon7)
        self.full_prev_btn.setIconSize(QSize(48, 48))

        self.horizontalLayout_5.addWidget(self.full_prev_btn)

        self.frame_4 = QFrame(self.full_view_tab)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.full_image_label = QLabel(self.frame_4)
        self.full_image_label.setObjectName(u"full_image_label")
        self.full_image_label.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.full_image_label)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.full_next_btn = QPushButton(self.full_view_tab)
        self.full_next_btn.setObjectName(u"full_next_btn")
        sizePolicy2.setHeightForWidth(self.full_next_btn.sizePolicy().hasHeightForWidth())
        self.full_next_btn.setSizePolicy(sizePolicy2)
        self.full_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.full_next_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/next_hover.png);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.full_next_btn.setIcon(icon8)
        self.full_next_btn.setIconSize(QSize(48, 48))

        self.horizontalLayout_5.addWidget(self.full_next_btn)

        self.tabWidget.addTab(self.full_view_tab, "")
        self.single_view_tab = QWidget()
        self.single_view_tab.setObjectName(u"single_view_tab")
        self.horizontalLayout_6 = QHBoxLayout(self.single_view_tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.single_prev_btn = QPushButton(self.single_view_tab)
        self.single_prev_btn.setObjectName(u"single_prev_btn")
        sizePolicy2.setHeightForWidth(self.single_prev_btn.sizePolicy().hasHeightForWidth())
        self.single_prev_btn.setSizePolicy(sizePolicy2)
        self.single_prev_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.single_prev_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/prev_hover.png);\n"
"}")
        self.single_prev_btn.setIcon(icon7)
        self.single_prev_btn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.single_prev_btn)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 40, -1, -1)
        self.plate_frame = QFrame(self.single_view_tab)
        self.plate_frame.setObjectName(u"plate_frame")
        self.plate_frame.setMinimumSize(QSize(0, 80))
        self.plate_frame.setMaximumSize(QSize(16777215, 80))
        self.plate_frame.setStyleSheet(u"#plate_frame{\n"
"	background-color: rgb(38, 61, 74);\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: transparent;\n"
"	color: white;\n"
"	font-size: 24px;\n"
"\n"
"}")
        self.plate_frame.setFrameShape(QFrame.StyledPanel)
        self.plate_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.plate_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.plate_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_9.addWidget(self.label_2)

        self.slab_number_lbl = QLabel(self.plate_frame)
        self.slab_number_lbl.setObjectName(u"slab_number_lbl")
        sizePolicy.setHeightForWidth(self.slab_number_lbl.sizePolicy().hasHeightForWidth())
        self.slab_number_lbl.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.slab_number_lbl)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addWidget(self.plate_frame)

        self.single_image_label = QLabel(self.single_view_tab)
        self.single_image_label.setObjectName(u"single_image_label")
        self.single_image_label.setMinimumSize(QSize(700, 200))

        self.verticalLayout_6.addWidget(self.single_image_label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.single_next_btn = QPushButton(self.single_view_tab)
        self.single_next_btn.setObjectName(u"single_next_btn")
        sizePolicy2.setHeightForWidth(self.single_next_btn.sizePolicy().hasHeightForWidth())
        self.single_next_btn.setSizePolicy(sizePolicy2)
        self.single_next_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.single_next_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/next_hover.png);\n"
"}")
        self.single_next_btn.setIcon(icon8)
        self.single_next_btn.setIconSize(QSize(48, 48))

        self.horizontalLayout_6.addWidget(self.single_next_btn)

        self.tabWidget.addTab(self.single_view_tab, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.image_page)
        self.drawing_page = QWidget()
        self.drawing_page.setObjectName(u"drawing_page")
        self.verticalLayout_5 = QVBoxLayout(self.drawing_page)
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.drawing_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.drawing_detect_btn = QPushButton(self.frame_2)
        self.drawing_detect_btn.setObjectName(u"drawing_detect_btn")
        self.drawing_detect_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.drawing_detect_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/detect_hover.png);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/detect.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drawing_detect_btn.setIcon(icon9)
        self.drawing_detect_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.drawing_detect_btn)

        self.drawing_clear_btn = QPushButton(self.frame_2)
        self.drawing_clear_btn.setObjectName(u"drawing_clear_btn")
        self.drawing_clear_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.drawing_clear_btn.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	icon: url(:/icons/icons/clear_hover.png);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.drawing_clear_btn.setIcon(icon10)
        self.drawing_clear_btn.setIconSize(QSize(35, 35))

        self.horizontalLayout_4.addWidget(self.drawing_clear_btn)

        self.abbas = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.abbas)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(self.drawing_page)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_7.setContentsMargins(20, 20, 20, 20)
        self.drawing_label = QLabel(self.frame)
        self.drawing_label.setObjectName(u"drawing_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.drawing_label.sizePolicy().hasHeightForWidth())
        self.drawing_label.setSizePolicy(sizePolicy4)
        self.drawing_label.setMinimumSize(QSize(640, 480))
        self.drawing_label.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.drawing_label)


        self.verticalLayout_5.addWidget(self.frame)

        self.stackedWidget.addWidget(self.drawing_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maximize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.side_image_btn.setText(QCoreApplication.translate("MainWindow", u" Image         ", None))
        self.side_drawing_btn.setText(QCoreApplication.translate("MainWindow", u" Drawing      ", None))
#if QT_CONFIG(tooltip)
        self.open_folder_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Open Folder", None))
#endif // QT_CONFIG(tooltip)
        self.open_folder_btn.setText("")
#if QT_CONFIG(tooltip)
        self.open_file_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Open File", None))
#endif // QT_CONFIG(tooltip)
        self.open_file_btn.setText("")
        self.full_prev_btn.setText("")
        self.full_image_label.setText("")
        self.full_next_btn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.full_view_tab), QCoreApplication.translate("MainWindow", u"Full View", None))
        self.single_prev_btn.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Slab Serial Number :", None))
        self.slab_number_lbl.setText("")
        self.single_image_label.setText("")
        self.single_next_btn.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.single_view_tab), QCoreApplication.translate("MainWindow", u"Single View", None))
        self.drawing_detect_btn.setText("")
        self.drawing_clear_btn.setText("")
        self.drawing_label.setText("")
    # retranslateUi

