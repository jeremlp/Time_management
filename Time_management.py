# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:09:01 2021
@author: jerem
"""

import time
import numpy as np
import datetime

import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import time
import pyqtgraph as pg

import json
class MainWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # with open("CalendarData.json", "w") as write_file:
        #     json.dump({}, write_file)

        """VARIABLES"""
        self.CurrentActivity = "None"
        self.TotalHours = 0

        self.OnStartNow = datetime.datetime.now()
        self.lastDstr = str(self.OnStartNow)[11:19]
        print(f"Start time : {str(self.OnStartNow)[11:19]}")
        self.nbTicks = 1

        self.NoneCount = 0
        self.LessonCount = 0
        self.WatchingVideoCount = 0
        self.ProgrammingCount = 0
        self.StudyingCount = 0
        self.FriendsCount = 0
        self.HellyCount = 0

        self.Buttons = []

        self.ActivitiesCount = [self.NoneCount, self.LessonCount, self.StudyingCount, self.HellyCount, self.FriendsCount, self.WatchingVideoCount,self.ProgrammingCount]
        self.colors = ["lightgray", "darkturquoise", "cornflowerblue" ,"indianred", "limegreen", "mediumorchid", "orange"]
        """Main Window"""
        self.setGeometry(75,25,1280,700)
        self.setWindowTitle("Live Calendar")
        self.setWindowIcon(QtGui.QIcon('D:/JLP/_INFORMATIQUE_/_FILES_/PHOTOS/LiveCalendar.PNG'))

        # a figure instance to plot on


        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        """Matplotlib"""
        self.figure = Figure()
        self.figure.autofmt_xdate()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.ax2 = self.figure2.add_subplot(111)
        self.ax2.axis('equal')

        self.hours = [self.lastDstr]

        SubBoxLayout = QtWidgets.QVBoxLayout()
        SubBoxLayout2 = QtWidgets.QVBoxLayout()

        #LABELS ===================

        self.Hourslabel = QtWidgets.QLabel(f"Total hours : {self.TotalHours}")
        font = QtGui.QFont('Arial', 16)
        font.setBold(True)
        self.Hourslabel.setFont(font)
        layoutLabel =  QtWidgets.QHBoxLayout()
        layoutLabel.addWidget(self.Hourslabel)
        SubBoxLayout.addLayout(layoutLabel)

        self.label = QtWidgets.QLabel(f"Activity : {self.CurrentActivity}")
        font = QtGui.QFont('Arial', 14)
        font.setBold(True)
        self.label.setFont(font)
        layoutLabel =  QtWidgets.QHBoxLayout()
        layoutLabel.addWidget(self.label)
        SubBoxLayout.addLayout(layoutLabel)
        #LABELS ===================

        #BUTTON ===================
        myFont=QtGui.QFont()
        myFont.setBold(True)
        self.button = QtWidgets.QPushButton("None")
        self.button.setFont(myFont)
        layout1 = self.creatPara("None", self.button)
        SubBoxLayout2.addLayout(layout1)
        self.button.clicked.connect(lambda : self.ChangeActivity("None", self.button))
        self.Buttons.append(self.button)

        self.button0 = QtWidgets.QPushButton("Lesson")
        self.button0.setStyleSheet("background-color: darkturquoise")
        self.button0.setFont(myFont)
        layout1 = self.creatPara("Lesson", self.button0)
        SubBoxLayout2.addLayout(layout1)
        self.button0.clicked.connect(lambda : self.ChangeActivity("Lesson",self.button0))
        self.Buttons.append(self.button0)

        self.button1 = QtWidgets.QPushButton("Study")
        self.button1.setStyleSheet("background-color: cornflowerblue")
        self.button1.setFont(myFont)
        layout1 = self.creatPara("Study", self.button1)
        SubBoxLayout2.addLayout(layout1)
        self.button1.clicked.connect(lambda : self.ChangeActivity("Study", self.button1))
        self.Buttons.append(self.button1)

        self.button2 = QtWidgets.QPushButton("Helly")
        self.button2.setStyleSheet("background-color: indianred")
        self.button2.setFont(myFont)
        layout1 = self.creatPara("Helly", self.button2)
        SubBoxLayout2.addLayout(layout1)
        self.button2.clicked.connect(lambda : self.ChangeActivity("Helly", self.button2))
        self.Buttons.append(self.button2)

        self.button3 = QtWidgets.QPushButton("Friends")
        self.button3.setStyleSheet("background-color: limegreen")
        self.button3.setFont(myFont)
        layout1 = self.creatPara("Playing w/ Friends", self.button3)
        SubBoxLayout2.addLayout(layout1)
        self.button3.clicked.connect(lambda : self.ChangeActivity("Friends", self.button3))
        self.Buttons.append(self.button3)

        self.button4 = QtWidgets.QPushButton("Watching Videos")
        self.button4.setStyleSheet("background-color: mediumorchid")
        self.button4.setFont(myFont)
        layout1 = self.creatPara("Watching Videos", self.button4)
        SubBoxLayout2.addLayout(layout1)
        self.button4.clicked.connect(lambda : self.ChangeActivity("Watching Videos", self.button4))
        self.Buttons.append(self.button4)

        self.button5 = QtWidgets.QPushButton("Programming")
        self.button5.setStyleSheet("background-color: orange")
        self.button5.setFont(myFont)
        layout1 = self.creatPara("Programming", self.button5)
        SubBoxLayout2.addLayout(layout1)
        self.button5.clicked.connect(lambda : self.ChangeActivity("Programming", self.button5))
        self.Buttons.append(self.button5)

        self.groupBox = QtWidgets.QGroupBox("Settings")
        self.groupBox.setMinimumWidth(320)
        self.groupBox.setMaximumWidth(320)

        self.SubGroupBox = QtWidgets.QGroupBox("Infos")
        self.SubGroupBox.setMinimumWidth(320)
        self.SubGroupBox.setMaximumWidth(320)
        self.SubGroupBox.setMaximumHeight(200)
        self.SubGroupBox.setLayout(SubBoxLayout)

        self.SubGroupBox2 = QtWidgets.QGroupBox("Activities")
        self.SubGroupBox2.setMinimumWidth(320)
        self.SubGroupBox2.setMaximumWidth(320)
        self.SubGroupBox2.setLayout(SubBoxLayout2)

        MediumLayout = QtWidgets.QVBoxLayout()
        MediumLayout.addWidget(self.SubGroupBox)
        MediumLayout.addWidget(self.SubGroupBox2)
        self.groupBox.setLayout(MediumLayout)


        PlotLayout = QtWidgets.QVBoxLayout()
        PlotLayout.addWidget(self.canvas)
        PlotLayout.addWidget(self.canvas2)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.groupBox)
        layout.addLayout(PlotLayout)
        self.setLayout(layout)

        self.refreshRate = 5 #s
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.GetActivity)
        self.timer.start(1000 * self.refreshRate) # refresh rate in ms


        self.DT = 60 * 2  #s
        self.EveryTicks = 1 * 30
        self.Drawtimer = pg.QtCore.QTimer()
        self.Drawtimer.timeout.connect(self.Draw)
        self.Drawtimer.start(1000 * self.DT) # refresh rate in ms



    def creatPara(self,name, widget):
        layout =  QtWidgets.QHBoxLayout()
        #layout.addWidget(QtWidgets.QLabel(name))
        layout.addWidget(widget)
        return layout

    def ChangeActivity(self, activity, button):
        highlight_font=QtGui.QFont()
        highlight_font.setBold(True)

        myFont=QtGui.QFont()

        #print("clicked :", activity)
        self.CurrentActivity = activity
        self.file_name = "Calendar_" + activity + ".PNG"
        self.changeIcon()
        self.label.setText(f"Activity : {activity}")

        for b in self.Buttons: #Reset all font
            b.setFont(myFont)

        button.setFont(highlight_font)


    def GetActivity(self):
        t0 = time.perf_counter()
        d = datetime.datetime.now()

        dstr = str(d)[2:19] #Or 11:19
        self.ax.set_title(dstr)
        self.canvas.draw()

        #self.updateJson()

        self.TotalHours += self.refreshRate
        TotalHours = str(datetime.timedelta(seconds=self.TotalHours))
        self.Hourslabel.setText(f"Total hours : {TotalHours}")

        self.hatch = None
        self.edgecolor = None
        self.file_name = None
        if self.CurrentActivity == "None":
            self.color = "lightgray"
            self.NoneCount += self.refreshRate
            self.file_name = 'CalendarNone.PNG'
            t = str(datetime.timedelta(seconds=self.NoneCount))
            self.button.setText(f"{self.CurrentActivity} : {t}")

        if self.CurrentActivity == "Lesson":
            self.color = "none"
            self.hatch="X"
            self.edgecolor="darkturquoise"
            self.LessonCount += self.refreshRate
            self.file_name = 'CalendarTurquoise.jpg'
            t = str(datetime.timedelta(seconds=self.LessonCount))
            self.button0.setText(f"{self.CurrentActivity} : {t}")

        elif self.CurrentActivity == "Study":
            self.color = "cornflowerblue"
            self.StudyingCount += self.refreshRate
            self.file_name = 'CalendarBlue.PNG'
            t = str(datetime.timedelta(seconds=self.StudyingCount))
            self.button1.setText(f"{self.CurrentActivity} : {t}")

        elif self.CurrentActivity == "Helly":
            self.color = "indianred"
            self.HellyCount += self.refreshRate
            self.file_name = 'CalendarRed.PNG'
            t = str(datetime.timedelta(seconds=self.HellyCount))
            self.button2.setText(f"{self.CurrentActivity} : {t}")

        elif self.CurrentActivity == "Friends":
            self.color = "limegreen"
            self.FriendsCount += self.refreshRate
            self.file_name = "CalendarGreen.jpg"
            t = str(datetime.timedelta(seconds=self.FriendsCount))
            self.button3.setText(f"{self.CurrentActivity} : {t}")

        elif self.CurrentActivity == "Watching Videos":
            self.color = "mediumorchid"
            self.WatchingVideoCount += self.refreshRate
            self.file_name = 'CalendarPurple.PNG'
            t = str(datetime.timedelta(seconds=self.WatchingVideoCount))
            self.button4.setText(f"{self.CurrentActivity} : {t}")

        elif self.CurrentActivity == "Programming":
            self.color = "orange"
            self.ProgrammingCount += self.refreshRate
            self.file_name = 'CalendarOrange.PNG'
            t = str(datetime.timedelta(seconds=self.ProgrammingCount))
            self.button5.setText(f"{self.CurrentActivity} : {t}")

        #print("time :", (time.perf_counter() - t0)*1000, "ms")
        self.ActivitiesCount = [self.NoneCount, self.LessonCount, self.StudyingCount, self.HellyCount, self.FriendsCount, self.WatchingVideoCount,self.ProgrammingCount]
        self.DrawPieChart()

    def DrawPieChart(self):

        self.ax2.clear()

        pourcent = np.array(self.ActivitiesCount)*100 /self.TotalHours
        colors = self.colors.copy()
        indexes = []
        for i in range(len(pourcent)):
            if pourcent[i] == 0:
                indexes.append(i)
        pourcent = np.delete(pourcent, indexes)
        colors = [i for j, i in enumerate(colors) if j not in indexes]

        #print(pourcent)

        self.ax2.pie(pourcent, colors = colors, radius = 1, labels= None, autopct='%1.1f%%',shadow=True, startangle=90)
        self.figure2.canvas.draw_idle()


    def updateJson(self):
        JSON_NAME = "D:/JLP/_INFORMATIQUE_/_FILES_/JSON/CalendarData.json"
        with open(JSON_NAME, "r") as read_file:
            data = json.load(read_file)


        now = str(datetime.datetime.now()) #Never change

        data[now] = self.CurrentActivity

        with open(JSON_NAME, "w") as write_file:
                json.dump(data, write_file)


    def Draw(self):
        """TIME"""
        d = datetime.datetime.now()

        self.dstr = str(d)[11:16]
        self.nbTicks += 1
        if self.nbTicks % self.EveryTicks != 0:
            self.hours.append("")
        else:
            self.hours.append(self.dstr)

        if self.dstr >= '20:00' and self.dstr < '21:00':
            self.ax.plot(['20:00','20:00'], [0,1], c = "k", linewidth = 2)

        if d.day > self.OnStartNow.day or d.month > self.OnStartNow.month:
            self.ax.plot(['00:00','00:00'], [0,1], c = "k", linewidth = 2)

        # if self.dstr >= self.dstr[:2]+":00":
        #      self.ax.plot([self.dstr[:2]+":00",self.dstr[:2]+":00"], [0,1], c = "gray", linestyle='dashed', linewidth = 1)

        x = [self.lastDstr, self.dstr]

        y = [1,1]

        self.ax.fill_between(x, y, facecolor = self.color, hatch = self.hatch, edgecolor = self.edgecolor)
        self.canvas.draw()
        # self.ax.plot([self.lastDstr, self.lastDstr],[0,1], linewidth = 2, c = "b")
        # self.ax.plot([self.dstr, self.dstr],[0,1],  linewidth = 2, c = "r")

        #LABELS

        self.labels = self.ax.xaxis.get_ticklabels()


        # for n, label in enumerate(self.labels):
        #     if n % self.EveryTicks != 0:
        #         label.set_c("w")

        self.ax.set_xticklabels(self.hours, fontsize = 8,rotation = 60)
        self.canvas.draw()
        self.lastDstr = self.dstr
        #plt.pause(0.001)


    def changeIcon(self):
        import ctypes
        myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setWindowIcon(QtGui.QIcon('D:/JLP/_INFORMATIQUE_/_FILES_/PHOTOS/CalendarPic/' + self.file_name))
    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QtGui.QMessageBox.question(self, 'Message',
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            #sys.exit()
        else:
            event.ignore()

if __name__ == '__main__':
    import ctypes
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = QtWidgets.QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
