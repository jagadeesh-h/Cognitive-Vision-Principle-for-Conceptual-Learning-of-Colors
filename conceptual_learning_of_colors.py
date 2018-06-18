#----------- Cognitive Vision Principle for Conceptual Learning of Colors ------------#
#------------------------------- Author: Jagadeesh Hariharan -------------------------#
#------------------------------- Date Modified: June 01,2017 -------------------------#

#----importing required packages--------#
import pandas as pd
from sklearn.cluster import KMeans
import sys
import cv2
import numpy as np
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *

#----- Initiating try-catch blocks-----------------#
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))


#----  Learning of Colors Class--------#
class Ui_MainWindow(object):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.setupUi(self)

    # ---- Design Elements for GUI--------#
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(599, 477)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        # ---- Importing the logo for the GUI--------#
        MainWindow.setWindowIcon(QtGui.QIcon('/home/jagadeesh/Desktop/py/PycharmProjects/QT/cw.png'))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 601, 271))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.learn = QtGui.QWidget()
        self.learn.setEnabled(True)
        self.learn.setObjectName(_fromUtf8("learn"))
        self.label_6 = QtGui.QLabel(self.learn)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 301, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label = QtGui.QLabel(self.learn)
        self.label.setGeometry(QtCore.QRect(10, 110, 21, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.Rinput = QtGui.QTextEdit(self.learn)
        self.Rinput.setGeometry(QtCore.QRect(30, 100, 50, 30))
        self.Rinput.setObjectName(_fromUtf8("Rinput"))
        self.label_2 = QtGui.QLabel(self.learn)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 21, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Ginput = QtGui.QTextEdit(self.learn)
        self.Ginput.setGeometry(QtCore.QRect(110, 100, 50, 30))
        self.Ginput.setObjectName(_fromUtf8("Ginput"))
        self.label_3 = QtGui.QLabel(self.learn)
        self.label_3.setGeometry(QtCore.QRect(170, 110, 21, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Binput = QtGui.QTextEdit(self.learn)
        self.Binput.setGeometry(QtCore.QRect(190, 100, 50, 30))
        self.Binput.setObjectName(_fromUtf8("Binput"))
        self.enterrgb = QtGui.QPushButton(self.learn)
        self.enterrgb.setGeometry(QtCore.QRect(245, 100, 120, 30))
        self.enterrgb.setObjectName(_fromUtf8("enterrgb"))
        #QtCore.QObject.connect(self.enterrgb, QtCore.SIGNAL("clicked()"), self.inputrgb)


        self.enterrgb.clicked.connect(self.inputrgb)

        self.line_10 = QtGui.QFrame(self.learn)
        self.line_10.setGeometry(QtCore.QRect(0, 60, 371, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_10.setFont(font)
        self.line_10.setFrameShadow(QtGui.QFrame.Raised)
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.learnload = QtGui.QPushButton(self.learn)
        self.learnload.setGeometry(QtCore.QRect(10, 160, 101, 27))
        self.learnload.setObjectName(_fromUtf8("learnload"))

        self.learnload.clicked.connect(self.file_open1)


        self.label_5 = QtGui.QLabel(self.learn)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.learnbutton = QtGui.QPushButton(self.learn)
        self.learnbutton.setGeometry(QtCore.QRect(100, 200, 141, 27))
        self.learnbutton.setObjectName(_fromUtf8("learnbutton"))
        self.line_9 = QtGui.QFrame(self.learn)
        self.line_9.setGeometry(QtCore.QRect(0, 140, 371, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_9.setFont(font)
        self.line_9.setFrameShadow(QtGui.QFrame.Raised)
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.line = QtGui.QFrame(self.learn)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 241))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.learncolorinput = QtGui.QTextEdit(self.learn)
        self.learncolorinput.setGeometry(QtCore.QRect(10, 30, 161, 31))
        self.learncolorinput.setObjectName(_fromUtf8("learncolorinput"))

        global color_entered

        self.line_12 = QtGui.QFrame(self.learn)
        self.line_12.setGeometry(QtCore.QRect(0, 230, 641, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_12.setFont(font)
        self.line_12.setFrameShadow(QtGui.QFrame.Raised)
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.learnimg = QtGui.QLabel(self.learn)
        self.learnimg.setGeometry(QtCore.QRect(380, 40, 171, 181))
        self.learnimg.setText(_fromUtf8(""))
        self.learnimg.setObjectName(_fromUtf8("learnimg"))
        self.txtlbl2_3 = QtGui.QLabel(self.learn)
        self.txtlbl2_3.setGeometry(QtCore.QRect(380, 10, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtlbl2_3.setFont(font)
        self.txtlbl2_3.setObjectName(_fromUtf8("txtlbl2_3"))
        self.Binputfromimage = QtGui.QTextEdit(self.learn)
        self.Binputfromimage.setGeometry(QtCore.QRect(280, 160, 45, 31))
        self.Binputfromimage.setObjectName(_fromUtf8("Binputfromimage"))
        self.Ginputfromimage = QtGui.QTextEdit(self.learn)
        self.Ginputfromimage.setGeometry(QtCore.QRect(210, 160, 45, 31))
        self.Ginputfromimage.setObjectName(_fromUtf8("Ginputfromimage"))
        self.label_11 = QtGui.QLabel(self.learn)
        self.label_11.setGeometry(QtCore.QRect(120, 170, 21, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.Rinputfromimage = QtGui.QTextEdit(self.learn)
        self.Rinputfromimage.setGeometry(QtCore.QRect(140, 160, 45, 31))
        self.Rinputfromimage.setObjectName(_fromUtf8("Rinputfromimage"))
        self.label_12 = QtGui.QLabel(self.learn)
        self.label_12.setGeometry(QtCore.QRect(190, 170, 21, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.learn)
        self.label_13.setGeometry(QtCore.QRect(260, 170, 21, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("ll.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.learn, icon1, _fromUtf8(""))
        self.rr = QtGui.QWidget()
        self.rr.setObjectName(_fromUtf8("rr"))
        self.line_7 = QtGui.QFrame(self.rr)
        self.line_7.setGeometry(QtCore.QRect(0, 100, 391, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_7.setFont(font)
        self.line_7.setFrameShadow(QtGui.QFrame.Raised)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.rrload = QtGui.QPushButton(self.rr)
        self.rrload.setGeometry(QtCore.QRect(20, 40, 101, 27))
        self.rrload.setObjectName(_fromUtf8("rrload"))

        self.rrload.clicked.connect(self.file_open2)


        self.rrcoloroutput = QtGui.QTextEdit(self.rr)
        self.rrcoloroutput.setGeometry(QtCore.QRect(270, 40, 111, 31))
        self.rrcoloroutput.setObjectName(_fromUtf8("rrcoloroutput"))
        self.label_7 = QtGui.QLabel(self.rr)
        self.label_7.setGeometry(QtCore.QRect(140, 50, 121, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.rrcolorinput = QtGui.QTextEdit(self.rr)
        self.rrcolorinput.setGeometry(QtCore.QRect(140, 140, 111, 31))
        self.rrcolorinput.setObjectName(_fromUtf8("rrcolorinput"))
        self.label_8 = QtGui.QLabel(self.rr)
        self.label_8.setGeometry(QtCore.QRect(10, 150, 121, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rrbutton = QtGui.QPushButton(self.rr)
        self.rrbutton.setGeometry(QtCore.QRect(260, 140, 121, 27))
        self.rrbutton.setObjectName(_fromUtf8("rrbutton"))

        self.rrbutton.clicked.connect(self.Rkmeans)


        self.label_4 = QtGui.QLabel(self.rr)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 161, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_9 = QtGui.QLabel(self.rr)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 141, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txtlbl2_2 = QtGui.QLabel(self.rr)
        self.txtlbl2_2.setGeometry(QtCore.QRect(400, 10, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.txtlbl2_2.setFont(font)
        self.txtlbl2_2.setObjectName(_fromUtf8("txtlbl2_2"))
        self.rrimageoutput = QtGui.QLabel(self.rr)
        self.rrimageoutput.setGeometry(QtCore.QRect(400, 30, 191, 201))
        self.rrimageoutput.setText(_fromUtf8(""))
        self.rrimageoutput.setObjectName(_fromUtf8("rrimageoutput"))
        self.line_2 = QtGui.QFrame(self.rr)
        self.line_2.setGeometry(QtCore.QRect(380, 0, 16, 241))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_11 = QtGui.QFrame(self.rr)
        self.line_11.setGeometry(QtCore.QRect(0, 230, 601, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.line_11.setFont(font)
        self.line_11.setFrameShadow(QtGui.QFrame.Raised)
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("l.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.rr, icon2, _fromUtf8(""))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 300, 581, 151))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 141, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        #print names

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # ---- Lables for elements in GUI--------#
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Colour Learning", None))
        self.label_6.setText(_translate("MainWindow", "Enter RGB Values or Load an image", None))
        self.label.setText(_translate("MainWindow", "R", None))
        self.label_2.setText(_translate("MainWindow", "G", None))
        self.label_3.setText(_translate("MainWindow", "B", None))
        self.enterrgb.setText(_translate("MainWindow", "Learn from RGB ", None))
        self.learnload.setText(_translate("MainWindow", "Load Image", None))
        self.label_5.setText(_translate("MainWindow", "Enter Color Name", None))
        self.learnbutton.setText(_translate("MainWindow", "Learn from Image", None))
        self.txtlbl2_3.setText(_translate("MainWindow", "Learning Image", None))
        self.label_11.setText(_translate("MainWindow", "R", None))
        self.label_12.setText(_translate("MainWindow", "G", None))
        self.label_13.setText(_translate("MainWindow", "B", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.learn), _translate("MainWindow", "Learning", None))
        self.rrload.setText(_translate("MainWindow", "Load Image", None))
        self.label_7.setText(_translate("MainWindow", "Color Recognised", None))
        self.label_8.setText(_translate("MainWindow", "Type Color name", None))
        self.rrbutton.setText(_translate("MainWindow", "Retrive Color", None))
        self.label_4.setText(_translate("MainWindow", "Recognition of Color", None))
        self.label_9.setText(_translate("MainWindow", "Retrieval of Color", None))
        self.txtlbl2_2.setText(_translate("MainWindow", "Retrieved Image", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rr), _translate("MainWindow", "Recognition/Retrieval", None))
        self.label_10.setText(_translate("MainWindow", "System Response", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))


    def __del__(self):
        sys.stdout = sys.__stdout__

    def normalOutputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    # ---- Input from User--------#
    def inputrgb(self):
        global Redinput
        global Greeninput
        global Blueinput
        Redinput = int(self.Rinput.toPlainText())
        Greeninput = int(self.Ginput.toPlainText())
        Blueinput = int(self.Binput.toPlainText())
        color_entered = str(self.learncolorinput.toPlainText())
        color_entered = color_entered.lower()

        # ---- Predicting color through k-means Clustering--------#
        def kmeans(self):
            # ---- creating kmeans cluster for the 1298 dataset-------_#
            kmeans = KMeans(n_clusters=len(arr), random_state=0).fit(arr)
            centroids = kmeans.cluster_centers_
            labels = kmeans.labels_

            # ---- gets RGB values from image--------#
            testpt = []
            testpt.append(Redinput)
            testpt.append(Greeninput)
            testpt.append(Blueinput)

            # ----- displays the image for the corresponding RGB value ---------#
            average_color_img = np.array([[testpt] * 250] * 250, np.uint8)
            height, width, bytesPerComponent = average_color_img.shape
            bytesPerLine = 3 * width
            #average_color_img = cv2.cvtColor(average_color_img, cv2.COLOR_BGR2RGB)
            qImg = QtGui.QImage(average_color_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.learnimg.setPixmap(QtGui.QPixmap.fromImage(qImg))

            # --------- user input of colorname --------------#
            colorinput = color_entered

            # ---------- loop checks whether color name already exist or not ---------------- #
            for x in names:
                if (x == colorinput.lower()):
                    print('Color Already Exist')
                    nametest = 0
                    break
                else:
                    nametest = 1

            # ------------- loop checks whether RGB already exist or not ----------------------#
            for x in arr:
                if (x == testpt):
                    print('RGB Already Exist')
                    rgbtest = 0
                    break
                else:
                    rgbtest = 1

            # ---------------- appends new colorname to the list ---------------------------#
            if (nametest == 1 and rgbtest == 1):
                # predicts the closest color
                print ('Predicting!')
                pred = kmeans.predict(np.array(testpt).reshape(1, -1))

                predictedrgb = []

                # ----------loop for plotting the predicted and the original color data-----#
                for i in range(len(arr)):
                    # plots the graph in red for predefined color and blue for new color as x
                    if (labels[i] == pred):
                        predictedrgb = arr[i]


                # ------------updating the list-------------------------------------#
                names.append(colorinput)
                red.append(predictedrgb[0])
                green.append(predictedrgb[1])
                blue.append(predictedrgb[2])

                # writes the new list to the csv file
                df = pd.DataFrame({'Name': names, 'R': red, 'G': green, 'B': blue})
                df.to_csv('color_datasetapril26.csv', index=False)
                print('New color name learnt!')

            else:
                print('Color and RGB value already exist')

        kmeans(self)

    # ------------------- Image Processing of the input image ----------------------------------------#
    def file_open1(self):

        dl= QtGui.QFileDialog()
        input = QtGui.QFileDialog.getOpenFileName(dl, 'Open File')

        if input.isEmpty() == False:
            cvfilename = input.toLocal8Bit().data()  # convert Qstring to char*
            img = cv2.imread(cvfilename)

            average_color_per_row = np.average(img, axis=0)

            average_color = np.average(average_color_per_row, axis=0)

            # Dominant RGB values
            average_color = np.uint8(average_color)

            average_color_img = np.array([[average_color] * 250] * 250, np.uint8)
            height, width, bytesPerComponent = average_color_img.shape
            bytesPerLine = 3 * width
            average_color_img = cv2.cvtColor(average_color_img, cv2.COLOR_BGR2RGB)
            qImg = QtGui.QImage(average_color_img.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.learnimg.setPixmap(QtGui.QPixmap.fromImage(qImg))

            global rgbvaluefromimage
            rgbvaluefromimage = average_color.tolist()

            Ripfromimage = str(rgbvaluefromimage[2])
            Gipfromimage = str(rgbvaluefromimage[1])
            Bipfromimage = str(rgbvaluefromimage[0])
            self.Rinputfromimage.setText(Ripfromimage)
            self.Ginputfromimage.setText(Gipfromimage)
            self.Binputfromimage.setText(Bipfromimage)
            self.learnbutton.clicked.connect(self.imagelearn)

    #--------------- Learning through Human Interaction ---------------------#
    def imagelearn(self):
        color_entered = str(self.learncolorinput.toPlainText())
        color_entered = color_entered.lower()

        def kmeans(self):
            # ------------- creating kmeans cluster for the 1298 dataset ---------#
            kmeans = KMeans(n_clusters=len(arr), random_state=0).fit(arr)
            centroids = kmeans.cluster_centers_
            labels = kmeans.labels_

            # ------ gets RGB values from image ----------#
            testpt = rgbvaluefromimage

            # --------- user input of colorname ----------#
            colorinput = color_entered


            # loop checks whether color name already exist or not
            #for x in names:
                #if (x == colorinput):
                   # print('Color Already Exist')
                   # nametest = 0
                    #break
                #else:
                   # nametest = 1

            # ----------- loop checks whether RGB already exist or not------------#
            for x in arr:
                if (x == testpt):
                    print('RGB Already Exist')
                    rgbtest = 0
                    break
                else:
                    rgbtest = 1

            # appends new colorname to the list
            #if (nametest == 1 and rgbtest == 1):
            if (rgbtest == 1):
                # predicts the closest color
                print ('Predicting!')
                pred = kmeans.predict(np.array(testpt).reshape(1, -1))

                predictedrgb = []

                # loop for plotting the predicted and the original color data
                for i in range(len(arr)):
                    # plots the graph in red for predefined color and blue for new color as x
                    if (labels[i] == pred):
                        predictedrgb = arr[i]

                # gets the index value for the predicted color
                # predictedcolor = arr.index([predictedrgb[0], predictedrgb[1], predictedrgb[2]])

                # matches the name for the predicted color
                # names[predictedcolor]

                # ---------- updating the list -------------#
                names.append(colorinput)
                red.append(predictedrgb[0])
                green.append(predictedrgb[1])
                blue.append(predictedrgb[2])

                # ----------writes the new list to the csv file--------#
                df = pd.DataFrame({'Name': names, 'R': red, 'G': green, 'B': blue})
                df.to_csv('color_datasetapril26.csv', index=False)
                print('New color name learnt!')

        kmeans(self)

    # ----------- Predicting Color through from the user uploaded file----------#
    def file_open2(self):

        rrdl = QtGui.QFileDialog()
        rrinput = QtGui.QFileDialog.getOpenFileName(rrdl, 'Open File')

        if rrinput.isEmpty() == False:
            rrcvfilename = rrinput.toLocal8Bit().data()  # convert Qstring to char*
            rrimg = cv2.imread(rrcvfilename)

            rraverage_color_per_row = np.average(rrimg, axis=0)

            rraverage_color = np.average(rraverage_color_per_row, axis=0)

            # ----------- Dominant RGB values----------#
            rraverage_color = np.uint8(rraverage_color)
            global dominantrgb
            dominantrgb = rraverage_color
            print ("R = %d") % dominantrgb[2]
            print ("G = %d") % dominantrgb[1]
            print ("B = %d") % dominantrgb[0]

            rraverage_color_img = np.array([[rraverage_color] * 250] * 250, np.uint8)
            rrheight, rrwidth, rrbytesPerComponent = rraverage_color_img.shape
            rrbytesPerLine = 3 * rrwidth
            rraverage_color_img = cv2.cvtColor(rraverage_color_img, cv2.COLOR_BGR2RGB)
            rrqImg = QtGui.QImage(rraverage_color_img.data, rrwidth, rrheight, rrbytesPerLine, QImage.Format_RGB888)
            self.rrimageoutput.setPixmap(QtGui.QPixmap.fromImage(rrqImg))

            # ---------- Recognition-- rr (from image)-----------#
            def rrkmeans(self):
                # creating kmeans cluster for the 1298 dataset
                kmeans = KMeans(n_clusters=len(arr), random_state=0).fit(arr)
                centroids = kmeans.cluster_centers_
                labels = kmeans.labels_

                # -----gets RGB values from image---------#
                testpt = []
                testpt.append(dominantrgb[2])
                testpt.append(dominantrgb[1])
                testpt.append(dominantrgb[0])

                # ------loop checks whether RGB already exist or not---------#
                for x in arr:
                    if (x == testpt):
                        print('RGB Already Exist')
                        rgbtest = 0
                        break
                    else:
                        rgbtest = 1

                # ---------- predicts the colorname from the list --------------#
                if (rgbtest == 1):
                    # predicts the closest color
                    pred = kmeans.predict(np.array(testpt).reshape(1, -1))
                    predictedrgb = []

                    # ---------- loop for plotting the predicted and the original color data----------#
                    for i in range(len(arr)):
                        # plots the graph in red for predefined color and blue for new color as x
                        if (labels[i] == pred):
                            predictedrgb = arr[i]


                    # --------- gets the index value for the predicted color ----------#
                    predictedcolor = arr.index([predictedrgb[0], predictedrgb[1], predictedrgb[2]])

                    # ---------- matches the name for the predicted color------------- #
                    nn = names[predictedcolor]
                    self.rrcoloroutput.setText(nn)

                # ------------- finds the name from the database ------------------#
                if (rgbtest == 0):
                    tt = 0  # tt gets the column number of the colorname

                    for x in arr:

                        tt = tt + 1
                        if (x == testpt):
                            rgbtest = 0
                            break
                        else:
                            rgbtest = 1
                    tt = tt - 1
                    nn = str(names[tt])
                    self.rrcoloroutput.setText(nn)

            rrkmeans(self)

    #Retrieval-- R
    def Rkmeans(self):
        # user input of colorname
        colorinput = str(self.rrcolorinput.toPlainText())
        yy = 0 #yy has the column number of the colorname


        for x in names:

            yy = yy+1
            if (x.lower() == colorinput.lower()):
                nametest = 0
                break
            else:
                nametest = 1

        if nametest == 1:
            print('Entered Color not in Database')


        if nametest == 0:
            yy = yy - 1
            testpt = arr[yy]
            rraverage_color_img = np.array([[testpt] * 250] * 250, np.uint8)
            rrheight, rrwidth, rrbytesPerComponent = rraverage_color_img.shape
            rrbytesPerLine = 3 * rrwidth
            #rraverage_color_img = cv2.cvtColor(rraverage_color_img, cv2.COLOR_BGR2RGB)
            rrqImg = QtGui.QImage(rraverage_color_img.data, rrwidth, rrheight, rrbytesPerLine, QImage.Format_RGB888)
            self.rrimageoutput.setPixmap(QtGui.QPixmap.fromImage(rrqImg))
            print ("R = %d") % testpt[0]
            print ("G = %d") % testpt[1]
            print ("B = %d") % testpt[2]


# -------------------- Main Function --------------------- #
def main():
    global average_color
    average_color = []

    global rraverage_color
    rraverage_color = []

    # ------- creating list from data frame------ #
    global red
    global green
    global blue
    global names
    global arr
    df = pd.read_csv('color_datasetapril26.csv')
    red = df.reset_index()['R'].values.tolist()
    green = df.reset_index()['G'].values.tolist()
    blue = df.reset_index()['B'].values.tolist()
    names = df.reset_index()['Name'].values.tolist()
    arr = df.reset_index()[['R', 'G', 'B']].values.tolist()
    #print isinstance(arr, list)


    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




