# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/robosar_gui/src/robosar_gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(937, 621)
        self.e_stop_button = QtWidgets.QPushButton(Dialog)
        self.e_stop_button.setGeometry(QtCore.QRect(570, 550, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("src/robosar_gui/src/../../../../Downloads/stop_sign_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.e_stop_button.setIcon(icon)
        self.e_stop_button.setIconSize(QtCore.QSize(25, 25))
        self.e_stop_button.setObjectName("e_stop_button")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, -10, 231, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("src/robosar_gui/src/robosar_logo_big.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 80, 111, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(30, 110, 331, 481))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 315, 479))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(586, 90, 111, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(590, 240, 111, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(610, 520, 67, 17))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.homing_button = QtWidgets.QPushButton(Dialog)
        self.homing_button.setGeometry(QtCore.QRect(690, 550, 191, 41))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("src/robosar_gui/src/../../../../Downloads/avengers__endgame__2019__avengers_logo_png__by_mintmovi3_dd4bz30-fullview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homing_button.setIcon(icon1)
        self.homing_button.setIconSize(QtCore.QSize(25, 25))
        self.homing_button.setObjectName("homing_button")
        self.start_mission_button = QtWidgets.QPushButton(Dialog)
        self.start_mission_button.setGeometry(QtCore.QRect(410, 550, 141, 41))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("src/robosar_gui/src/../../../../Downloads/k4-detail1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_mission_button.setIcon(icon2)
        self.start_mission_button.setIconSize(QtCore.QSize(25, 25))
        self.start_mission_button.setObjectName("start_mission_button")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(420, 270, 441, 231))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.mission_timer_label = QtWidgets.QLabel(Dialog)
        self.mission_timer_label.setGeometry(QtCore.QRect(490, 120, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.mission_timer_label.setFont(font)
        self.mission_timer_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mission_timer_label.setObjectName("mission_timer_label")
        self.stop_timer_button = QtWidgets.QPushButton(Dialog)
        self.stop_timer_button.setGeometry(QtCore.QRect(780, 140, 89, 25))
        self.stop_timer_button.setObjectName("stop_timer_button")
        self.restart_timer_button = QtWidgets.QPushButton(Dialog)
        self.restart_timer_button.setGeometry(QtCore.QRect(780, 170, 89, 25))
        self.restart_timer_button.setObjectName("restart_timer_button")
        self.start_timer_button = QtWidgets.QPushButton(Dialog)
        self.start_timer_button.setGeometry(QtCore.QRect(780, 110, 89, 25))
        self.start_timer_button.setObjectName("start_timer_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.e_stop_button.setText(_translate("Dialog", " E-Stop"))
        self.label.setText(_translate("Dialog", "Mission Control"))
        self.label_3.setText(_translate("Dialog", "Agent Status"))
        self.label_4.setText(_translate("Dialog", "Mission Timer"))
        self.label_5.setText(_translate("Dialog", "Task Allocation"))
        self.label_6.setText(_translate("Dialog", "Actions"))
        self.homing_button.setText(_translate("Dialog", "  Avengers Assemble"))
        self.start_mission_button.setText(_translate("Dialog", "Start Mission"))
        self.mission_timer_label.setText(_translate("Dialog", "00:00"))
        self.stop_timer_button.setText(_translate("Dialog", "Pause"))
        self.restart_timer_button.setText(_translate("Dialog", "Restart"))
        self.start_timer_button.setText(_translate("Dialog", "Resume"))
