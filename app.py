# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import os

from worker import Worker

from separator import initSeparator

from PyQt5 import QtCore, QtGui, QtWidgets

import time

class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 280)
        MainWindow.setMinimumSize(QtCore.QSize(500, 280))
        MainWindow.setMaximumSize(QtCore.QSize(500, 280))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 466, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setObjectName("gridLayout")

        self.output_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.output_label.setObjectName("output_label")
        self.gridLayout.addWidget(self.output_label, 4, 0, 1, 1)

        self.foldername = QtWidgets.QLabel(self.gridLayoutWidget)
        self.foldername.setObjectName("foldername")
        self.gridLayout.addWidget(self.foldername, 2, 1, 1, 1)

        self.filename_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.filename_label.setObjectName("filename_label")
        self.gridLayout.addWidget(self.filename_label, 1, 0, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cancelButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.cancelButton, 5, 0, 1, 1)

        self.finishLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.finishLabel.setObjectName("finishLabel")
        self.gridLayout.addWidget(self.finishLabel, 5, 1, 1, 1)

        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setObjectName("start")
        self.gridLayout.addWidget(self.startButton, 5, 2, 1, 1)
        self.filename = QtWidgets.QLabel(self.gridLayoutWidget)
        self.filename.setObjectName("filename")
        self.gridLayout.addWidget(self.filename, 1, 1, 1, 1)
        self.dir_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.dir_label.setObjectName("dir_label")
        self.gridLayout.addWidget(self.dir_label, 2, 0, 1, 1)
        self.choose_file = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.choose_file.setObjectName("choose_file")
        self.gridLayout.addWidget(self.choose_file, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stems_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.stems_2.setChecked(True)
        self.stems_2.setObjectName("stems_2")
        self.ntracksgroup = QtWidgets.QButtonGroup(MainWindow)
        self.ntracksgroup.setObjectName("ntracksgroup")
        self.ntracksgroup.addButton(self.stems_2)
        self.horizontalLayout_3.addWidget(self.stems_2)
        self.stems_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.stems_4.setObjectName("stems_4")
        self.ntracksgroup.addButton(self.stems_4)
        self.horizontalLayout_3.addWidget(self.stems_4)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        self.choose_folder = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.choose_folder.setObjectName("choose_folder")
        self.gridLayout.addWidget(self.choose_folder, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.mp3_out = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.mp3_out.setChecked(True)
        self.mp3_out.setObjectName("mp3_out")
        self.saidagroup = QtWidgets.QButtonGroup(MainWindow)
        self.saidagroup.setObjectName("saidagroup")
        self.saidagroup.addButton(self.mp3_out)
        self.horizontalLayout_6.addWidget(self.mp3_out)
        self.wav_out = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.wav_out.setObjectName("radioButton")
        self.saidagroup.addButton(self.wav_out)
        self.horizontalLayout_6.addWidget(self.wav_out)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.separator_params = dict()

        self.threadpool = QtCore.QThreadPool()

        self.timer = QtCore.QTimer()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stems Separator"))
        self.output_label.setText(_translate("MainWindow", "Saída:"))
        self.foldername.setText(_translate("MainWindow", ""))
        self.filename_label.setText(_translate("MainWindow", "Arquivo:"))
        self.finishLabel.setText(_translate("MainWindow", ""))
        self.cancelButton.setText(_translate("MainWindow", "Cancelar"))
        self.startButton.setText(_translate("MainWindow", "Iniciar"))
        self.filename.setText(_translate("MainWindow", ""))
        self.dir_label.setText(_translate("MainWindow", "Diretório:"))
        self.choose_file.setText(_translate("MainWindow", "Escolher"))
        self.label_6.setText(_translate("MainWindow", "Stems Separatator - ALPHA"))
        self.stems_2.setText(_translate("MainWindow", "2 stems"))
        self.stems_4.setText(_translate("MainWindow", "4 stems"))
        self.choose_folder.setText(_translate("MainWindow", "Escolher"))
        self.label.setText(_translate("MainWindow", "N° de Tracks:"))
        self.mp3_out.setText(_translate("MainWindow", ".mp3"))
        self.wav_out.setText(_translate("MainWindow", ".wav"))

        self.choose_file.clicked.connect(self.choose_file_handler)
        self.choose_folder.clicked.connect(self.choose_folder_handler)

        self.startButton.clicked.connect(self.startHandler)
        self.cancelButton.clicked.connect(app.quit)


    def finishedHandler(self):
        self.finishLabel.setText("Processamento Finalizado, a Aplicação será fechada em 5s.")
        self.timer.timeout.connect(app.quit)
        self.timer.start(5000)

    def startHandler(self):
        if(self.stems_2.isChecked()):
            self.separator_params['stems'] = 'spleeter:2stems'
        else:
            self.separator_params['stems'] = 'spleeter:4stems'

        if(self.mp3_out.isChecked()):
            self.separator_params['codec'] = 'mp3'
        else:
            self.separator_params['codec'] = 'wav'

        self.startButton.setText('Carregando...')
        self.startButton.setEnabled(False)

        worker = Worker(initSeparator, self.separator_params)
        worker.signals.finished.connect(self.finishedHandler)

        self.threadpool.start(worker)


    def choose_file_handler(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Select File", os.getcwd(), "Audio Files (*.mp3 *.wav)")
        self.filename.setText(filename[0])
        self.separator_params['filename'] = filename[0]

    def choose_folder_handler(self):
        foldername = QtWidgets.QFileDialog.getExistingDirectory()
        self.foldername.setText(foldername)
        self.separator_params['foldername'] = foldername




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
