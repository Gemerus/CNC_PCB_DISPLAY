import threading

import numpy as np
from PIL import Image
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import  QPixmap, QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDesktopWidget
import time
import threading
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 861, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(880, 10, 111, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 360, 225))
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 370, 111, 31))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 370, 861, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 470, 981, 41))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 410, 861, 51))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setMinimum(9)
        self.horizontalSlider.setMaximum(61)
        self.horizontalSlider.setSingleStep(5)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(880, 410, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("")
        self.textEdit_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 85, 345, 217))
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 520, 751, 71))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 50, 435, 286))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Desktop/Рамка2.png"))
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 520, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 90, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(440, 210, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 150, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)


        self.progressBar.setProperty("value", 0)
        self.horizontalSlider.sliderMoved.connect(self.sliderTime)
        self.screen=QtWidgets.QWidget()
        self.label0 = QtWidgets.QLabel(self.screen)
        self.label0.setText("IMANGE NOT FOUND")
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_3.clicked.connect(self.exprose)
        self.pushButton_4.clicked.connect(self.screen.close)
        self.retranslateUi(MainWindow)
        self.pixmap=QPixmap()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.textEdit_3.setHtml(_translate("MainWindow",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "EXPROSE"))
        self.pushButton_4.setText(_translate("MainWindow", "STOP"))
        self.pushButton_5.setText(_translate("MainWindow", "UP"))
        self.pushButton_6.setText(_translate("MainWindow", "DOWN"))
        self.pushButton_7.setText(_translate("MainWindow", "LEFT"))
        self.pushButton_8.setText(_translate("MainWindow", "RIGHT"))

    def sliderTime(self):
        self.textEdit_3.setText(str(self.horizontalSlider.value()))

    def startconver(self,filename):
        start_time = time.time()

        img = Image.open(filename)
        img.load()

        tempimange=np.zeros((1620,2560,3), dtype=np.uint8)
        inputimange = np.asarray(img)
        inputimange=np.rot90(inputimange,1)
        position=inputimange.shape
        tempimange[0+100:position[0]+100, 0:position[1], :]=inputimange
        imange=tempimange
        height, width, channel = imange.shape
        bytesPerLine = 3 * width
        qImg = QImage(imange.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap = QPixmap(qImg)
        self.label.setPixmap(pixmap)


        subpixel2 = imange[:, :, 1].T
        subpixel2 = np.reshape(subpixel2, (2560, 540, 3)).swapaxes(0, 1)
        subpixel2 = np.flip(subpixel2, 2)
        subpixel= subpixel2.copy()

        height, width, channel = subpixel.shape
        bytesPerLine = 3 * width
        qImg1 = QImage(subpixel.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap(qImg1)
        self.label_2.setPixmap(self.pixmap)


        img2 = Image.fromarray(subpixel, "RGB")
        img2.save("testGleb.bmp")
        print("--- %s seconds ---" % (time.time() - start_time))


    def openfile(self):
        filename = QFileDialog.getOpenFileName()[0]
        start_time = time.time()
        print(filename)
        self.textEdit.setText(filename)
        self.startconver(filename)
    def waitexprose(self):
        print("stop")
        self.screen.close()
        self.my_qtimer.stop()
    def exprose(self):
        #self.label0.setPixmap(self.pixmap)
        monitor = QDesktopWidget().screenGeometry(1)
        self.screen.move(monitor.left(), monitor.top())
        self.screen.showFullScreen()
        self.my_qtimer = QtCore.QTimer()
        self.my_qtimer.timeout.connect(self.waitexprose)
        delay=int(self.horizontalSlider.value())
        print(delay)
        self.my_qtimer.start(delay*1000)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



