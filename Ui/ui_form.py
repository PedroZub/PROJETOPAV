# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QToolBox, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(Widget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMaximumSize(QSize(9, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_container)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 160, 440))
        self.verticalLayout_5 = QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 160, 440))
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(Widget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.top_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_uhg = QWidget()
        self.pg_uhg.setObjectName(u"pg_uhg")
        self.horizontalLayout_10 = QHBoxLayout(self.pg_uhg)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_13 = QFrame(self.pg_uhg)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_13)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.uhgreview = QLineEdit(self.frame_13)
        self.uhgreview.setObjectName(u"uhgreview")
        self.uhgreview.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.uhgreview, 5, 0, 1, 1)

        self.uhgid = QLineEdit(self.frame_13)
        self.uhgid.setObjectName(u"uhgid")
        self.uhgid.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.uhgid, 0, 0, 1, 1)

        self.uhguserid = QLineEdit(self.frame_13)
        self.uhguserid.setObjectName(u"uhguserid")
        self.uhguserid.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.uhguserid, 1, 0, 1, 1)

        self.uhgrate = QLineEdit(self.frame_13)
        self.uhgrate.setObjectName(u"uhgrate")
        self.uhgrate.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.uhgrate, 3, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_12, 6, 0, 1, 1)

        self.uhggameid = QLineEdit(self.frame_13)
        self.uhggameid.setObjectName(u"uhggameid")
        self.uhggameid.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.uhggameid, 2, 0, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.pg_uhg)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.pbcuhg = QPushButton(self.frame_14)
        self.pbcuhg.setObjectName(u"pbcuhg")

        self.verticalLayout_13.addWidget(self.pbcuhg)

        self.pbsuhg = QPushButton(self.frame_14)
        self.pbsuhg.setObjectName(u"pbsuhg")

        self.verticalLayout_13.addWidget(self.pbsuhg)

        self.pbauhg = QPushButton(self.frame_14)
        self.pbauhg.setObjectName(u"pbauhg")

        self.verticalLayout_13.addWidget(self.pbauhg)

        self.pbeuhg = QPushButton(self.frame_14)
        self.pbeuhg.setObjectName(u"pbeuhg")

        self.verticalLayout_13.addWidget(self.pbeuhg)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_13)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.pg_uhg)
        self.pg_game = QWidget()
        self.pg_game.setObjectName(u"pg_game")
        self.horizontalLayout_9 = QHBoxLayout(self.pg_game)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_11 = QFrame(self.pg_game)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gamedura = QLineEdit(self.frame_11)
        self.gamedura.setObjectName(u"gamedura")
        self.gamedura.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.gamedura, 5, 0, 1, 1)

        self.gameid = QLineEdit(self.frame_11)
        self.gameid.setObjectName(u"gameid")
        self.gameid.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.gameid, 0, 0, 1, 1)

        self.gamename = QLineEdit(self.frame_11)
        self.gamename.setObjectName(u"gamename")
        self.gamename.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.gamename, 1, 0, 1, 1)

        self.gamegender = QLineEdit(self.frame_11)
        self.gamegender.setObjectName(u"gamegender")
        self.gamegender.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.gamegender, 3, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 6, 0, 1, 1)

        self.platgame = QLineEdit(self.frame_11)
        self.platgame.setObjectName(u"platgame")
        self.platgame.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.platgame, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.pg_game)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.pbcgame = QPushButton(self.frame_12)
        self.pbcgame.setObjectName(u"pbcgame")

        self.verticalLayout_12.addWidget(self.pbcgame)

        self.pbsgame = QPushButton(self.frame_12)
        self.pbsgame.setObjectName(u"pbsgame")

        self.verticalLayout_12.addWidget(self.pbsgame)

        self.pbagame = QPushButton(self.frame_12)
        self.pbagame.setObjectName(u"pbagame")

        self.verticalLayout_12.addWidget(self.pbagame)

        self.pbegame = QPushButton(self.frame_12)
        self.pbegame.setObjectName(u"pbegame")

        self.verticalLayout_12.addWidget(self.pbegame)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_11)


        self.horizontalLayout_9.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.pg_game)
        self.pg_user = QWidget()
        self.pg_user.setObjectName(u"pg_user")
        self.horizontalLayout_5 = QHBoxLayout(self.pg_user)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_3 = QFrame(self.pg_user)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.userid = QLineEdit(self.frame_3)
        self.userid.setObjectName(u"userid")
        self.userid.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.userid, 0, 0, 1, 1)

        self.username = QLineEdit(self.frame_3)
        self.username.setObjectName(u"username")
        self.username.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.username, 1, 0, 1, 1)

        self.userage = QLineEdit(self.frame_3)
        self.userage.setObjectName(u"userage")
        self.userage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.userage, 3, 0, 1, 1)

        self.usergender = QLineEdit(self.frame_3)
        self.usergender.setObjectName(u"usergender")
        self.usergender.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.usergender, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.pg_user)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pbcuser = QPushButton(self.frame_4)
        self.pbcuser.setObjectName(u"pbcuser")

        self.verticalLayout_7.addWidget(self.pbcuser)

        self.pbsuser = QPushButton(self.frame_4)
        self.pbsuser.setObjectName(u"pbsuser")

        self.verticalLayout_7.addWidget(self.pbsuser)

        self.pbauser = QPushButton(self.frame_4)
        self.pbauser.setObjectName(u"pbauser")

        self.verticalLayout_7.addWidget(self.pbauser)

        self.pbeuser = QPushButton(self.frame_4)
        self.pbeuser.setObjectName(u"pbeuser")

        self.verticalLayout_7.addWidget(self.pbeuser)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.pg_user)

        self.verticalLayout_6.addWidget(self.stackedWidget)
    

        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)


        self.retranslateUi(Widget)

        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)

    

    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"BackDB", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"User", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Game", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"UserGame", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Widget", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p>Projeto Pav 2023<br/>BackDB</p><p><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("Widget", u"Page 2", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.uhgreview.setPlaceholderText(QCoreApplication.translate("Widget", u"Review", None))
        self.uhgid.setPlaceholderText(QCoreApplication.translate("Widget", u"ID", None))
        self.uhguserid.setPlaceholderText(QCoreApplication.translate("Widget", u"UserID", None))
        self.uhgrate.setPlaceholderText(QCoreApplication.translate("Widget", u"Nota", None))
        self.uhggameid.setPlaceholderText(QCoreApplication.translate("Widget", u"GameID", None))
        self.pbcuhg.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.pbsuhg.setText(QCoreApplication.translate("Widget", u"Selecionar", None))
        self.pbauhg.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.pbeuhg.setText(QCoreApplication.translate("Widget", u"Excluir", None))
        self.gamedura.setPlaceholderText(QCoreApplication.translate("Widget", u"Dura\u00e7\u00e3o", None))
        self.gameid.setPlaceholderText(QCoreApplication.translate("Widget", u"ID", None))
        self.gamename.setPlaceholderText(QCoreApplication.translate("Widget", u"Nome", None))
        self.gamegender.setPlaceholderText(QCoreApplication.translate("Widget", u"G\u00eanero", None))
        self.platgame.setPlaceholderText(QCoreApplication.translate("Widget", u"Plataforma", None))
        self.pbcgame.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.pbsgame.setText(QCoreApplication.translate("Widget", u"Selecionar", None))
        self.pbagame.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.pbegame.setText(QCoreApplication.translate("Widget", u"Excluir", None))
        self.userid.setPlaceholderText(QCoreApplication.translate("Widget", u"ID", None))
        self.username.setPlaceholderText(QCoreApplication.translate("Widget", u"Nome", None))
        self.userage.setPlaceholderText(QCoreApplication.translate("Widget", u"Idade", None))
        self.usergender.setPlaceholderText(QCoreApplication.translate("Widget", u"G\u00eanero", None))
        self.pbcuser.setText(QCoreApplication.translate("Widget", u"Cadastrar", None))
        self.pbsuser.setText(QCoreApplication.translate("Widget", u"Selecionar", None))
        self.pbauser.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.pbeuser.setText(QCoreApplication.translate("Widget", u"Excluir", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"BackDB", None))
    # retranslateUi

