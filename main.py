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
        self.PathToImange_Open = QtWidgets.QTextEdit(self.centralwidget)
        self.PathToImange_Open.setGeometry(QtCore.QRect(10, 10, 861, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.PathToImange_Open.setFont(font)
        self.PathToImange_Open.setStyleSheet("")
        self.PathToImange_Open.setObjectName("PathToImange_Open")
        self.Open = QtWidgets.QPushButton(self.centralwidget)
        self.Open.setGeometry(QtCore.QRect(880, 10, 111, 31))
        self.Open.setStyleSheet("")
        self.Open.setFlat(False)
        self.Open.setObjectName("Open")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 360, 225))
        self.label.setStyleSheet("")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(880, 370, 111, 31))
        self.Save.setStyleSheet("")
        self.Save.setFlat(False)
        self.Save.setObjectName("Save")
        self.PathToImange_Save = QtWidgets.QTextEdit(self.centralwidget)
        self.PathToImange_Save.setGeometry(QtCore.QRect(10, 370, 861, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(12)
        self.PathToImange_Save.setFont(font)
        self.PathToImange_Save.setStyleSheet("")
        self.PathToImange_Save.setObjectName("PathToImange_Save")
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
        self.ExproseTime = QtWidgets.QTextEdit(self.centralwidget)
        self.ExproseTime.setGeometry(QtCore.QRect(880, 410, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(24)
        self.ExproseTime.setFont(font)
        self.ExproseTime.setStyleSheet("")
        self.ExproseTime.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ExproseTime.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ExproseTime.setReadOnly(True)
        self.ExproseTime.setObjectName("ExproseTime")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 85, 345, 217))
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 50, 435, 286))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Desktop/Рамка2.png"))
        self.label_3.setObjectName("label_3")
        self.Stop = QtWidgets.QPushButton(self.centralwidget)
        self.Stop.setGeometry(QtCore.QRect(770, 520, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Stop.setFont(font)
        self.Stop.setAutoFillBackground(False)
        self.Stop.setStyleSheet("")
        self.Stop.setFlat(False)
        self.Stop.setObjectName("Stop")
        self.imange_Up = QtWidgets.QPushButton(self.centralwidget)
        self.imange_Up.setGeometry(QtCore.QRect(440, 50, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imange_Up.setFont(font)
        self.imange_Up.setObjectName("imange_Up")
        self.imange_Down = QtWidgets.QPushButton(self.centralwidget)
        self.imange_Down.setGeometry(QtCore.QRect(440, 170, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imange_Down.setFont(font)
        self.imange_Down.setObjectName("imange_Down")
        self.imange_Left = QtWidgets.QPushButton(self.centralwidget)
        self.imange_Left.setGeometry(QtCore.QRect(410, 110, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imange_Left.setFont(font)
        self.imange_Left.setObjectName("imange_Left")
        self.imange_Right = QtWidgets.QPushButton(self.centralwidget)
        self.imange_Right.setGeometry(QtCore.QRect(470, 110, 60, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.imange_Right.setFont(font)
        self.imange_Right.setObjectName("imange_Right")
        self.imange_RotateLeft = QtWidgets.QPushButton(self.centralwidget)
        self.imange_RotateLeft.setGeometry(QtCore.QRect(400, 230, 60, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imange_RotateLeft.setFont(font)
        self.imange_RotateLeft.setObjectName("imange_RotateLeft")
        self.imange_RotateRight = QtWidgets.QPushButton(self.centralwidget)
        self.imange_RotateRight.setGeometry(QtCore.QRect(470, 230, 60, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imange_RotateRight.setFont(font)
        self.imange_RotateRight.setObjectName("imange_RotateRight")
        self.imange_FlipV = QtWidgets.QPushButton(self.centralwidget)
        self.imange_FlipV.setGeometry(QtCore.QRect(400, 310, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imange_FlipV.setFont(font)
        self.imange_FlipV.setObjectName("imange_FlipV")
        self.imange_FlipH = QtWidgets.QPushButton(self.centralwidget)
        self.imange_FlipH.setGeometry(QtCore.QRect(470, 310, 60, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.imange_FlipH.setFont(font)
        self.imange_FlipH.setObjectName("imange_FlipH")
        self.Exprose = QtWidgets.QPushButton(self.centralwidget)
        self.Exprose.setGeometry(QtCore.QRect(10, 520, 751, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Exprose.setFont(font)
        self.Exprose.setAutoFillBackground(False)
        self.Exprose.setStyleSheet("")
        self.Exprose.setFlat(False)
        self.Exprose.setObjectName("Exprose")
        MainWindow.setCentralWidget(self.centralwidget)

        self.imangePosition = [0, 0, 0, 0]
        self.progressBar.setProperty("value", 0)
        self.horizontalSlider.sliderMoved.connect(self.sliderTime)
        self.screen=QtWidgets.QWidget()
        self.label0 = QtWidgets.QLabel(self.screen)
        self.label0.setText("IMANGE NOT FOUND")
        self.Open.clicked.connect(self.openfile)
        self.Exprose.clicked.connect(self.exprose)
        self.Stop.clicked.connect(self.screen.close)
        self.retranslateUi(MainWindow)
        self.pixmap=QPixmap()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Open.setText(_translate("MainWindow", "Open"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.ExproseTime.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Bahnschrift\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.Stop.setText(_translate("MainWindow", "STOP"))
        self.imange_Up.setText(_translate("MainWindow", "UP"))
        self.imange_Down.setText(_translate("MainWindow", "DOWN"))
        self.imange_Left.setText(_translate("MainWindow", "LEFT"))
        self.imange_Right.setText(_translate("MainWindow", "RIGHT"))
        self.imange_RotateLeft.setText(_translate("MainWindow", "R_LEFT"))
        self.imange_RotateRight.setText(_translate("MainWindow", "R_RIGHT"))
        self.imange_FlipV.setText(_translate("MainWindow", "Flip_V"))
        self.imange_FlipH.setText(_translate("MainWindow", "Flip_H"))
        self.Exprose.setText(_translate("MainWindow", "EXPROSE"))
    def sliderTime(self):
        self.ExproseTime.setText(str(self.horizontalSlider.value()))
    def SetImangeTranformation(self,positionV,positionH,angle,flip):
        print(self.imangePosition)

    def SetLableImange(self,imgforpixmap):
        height, width, channel = imgforpixmap.shape
        bytesPerLine = 3 * width
        qImg = QImage(imgforpixmap.data, width, height, bytesPerLine, QImage.Format_RGB888)
        return QPixmap(qImg)
    def ConvertToSubpixel(self,imgforsubppixel):
        subpixel2 = imgforsubppixel[:, :, 1].T
        subpixel2 = np.reshape(subpixel2, (2560, 540, 3)).swapaxes(0, 1)
        subpixel2 = np.flip(subpixel2, 2)
        subpixel= subpixel2.copy()
        return subpixel
    def openfile(self):
        filename = QFileDialog.getOpenFileName()[0]
        start_time = time.time()
        print(filename)
        self.PathToImange_Open.setText(filename)
        self.Inputimg = Image.open(filename)
        self.Inputimg.load()
        self.startconver()

    def FitToBOARD(self,imgForTranform):
        tempimange=np.zeros((1620,2560,3), dtype=np.uint8)
        inputimange = np.asarray(self.Inputimg)
        if inputimange.shape[0]>inputimange.shape[1]:
            inputimange = np.rot90(inputimange, 1)
        ImSize=inputimange.shape
        boardL=1620
        boardH=2560
        SizeL=ImSize[1]
        SizeH=ImSize[0]
        OffsetL=(boardH/2)-(SizeL/2)-480
        OffsetH=(boardL/2)-(SizeH/2)
        print(OffsetL)
        print(OffsetH)
        tempimange[0+int(OffsetH):ImSize[0]+int(OffsetH), 0+int(OffsetL):ImSize[1]+int(OffsetL), :]=inputimange
        imange=tempimange
        return imange
    def startconver(self,):
        start_time = time.time()

        self.label.setScaledContents(False)
        self.label.setPixmap(self.SetLableImange(np.asarray(self.Inputimg)).scaledToHeight(225))
        self.label_2.setPixmap(self.SetLableImange(self.ConvertToSubpixel(self.FitToBOARD(self.Inputimg))))
        img2 = Image.fromarray(self.ConvertToSubpixel(self.FitToBOARD(self.Inputimg)), "RGB")
        img2.save("testGleb.bmp")
        print("--- %s seconds ---" % (time.time() - start_time))


    def stopExprose(self):
        print("stop")
        self.screen.close()
        self.my_qtimer.stop()
    def waitexprose(self):
        if self.i>=0 :
            self.progressBar.setValue(self.i)
            self.ExproseTime.setText(str(self.i))
            self.i-=1
            print(self.i)

        else:
            print("stop")
            self.screen.close()
            self.my_qtimer.stop()
    def exprose(self):
        self.label0.setPixmap(self.SetLableImange(self.ConvertToSubpixel(self.FitToBOARD(self.Inputimg))))
        monitor = QDesktopWidget().screenGeometry(1)
        self.screen.move(monitor.left(), monitor.top())
        self.screen.showFullScreen()
        self.my_qtimer = QtCore.QTimer()
        self.my_qtimer.timeout.connect(self.waitexprose)
        self.delay=int(self.horizontalSlider.value())
        print(self.delay)
        self.i=self.delay
        self.progressBar.setMaximum(self.i)
        self.progressBar.setMinimum(0)
        self.my_qtimer.start(1000)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



