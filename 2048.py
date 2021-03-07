from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np

import random
import time
import traceback, sys



class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mv=True
        self.co2=0
        self.count=0
        self.mat=np.zeros(16).reshape(4,4)
        self.glob=5

        self.initUI()
        self.start2048()

        self.show()


    def initUI(self):
        mlayout=QHBoxLayout()
        mainlayout=QVBoxLayout()


        self.table=QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)

        self.table.setFont(QFont('Times', 40))
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.table.setAlternatingRowColors(True)

        for i in range(4):
            for j in range(4):
                self.table.setItem(i,j,QTableWidgetItem(' '))

        layout = QGridLayout()

        btn=QPushButton('Up')
        btn.clicked.connect(self.move_up)
        layout.addWidget(btn, 0, 1)
        btn1=QPushButton('Left')
        btn1.clicked.connect(self.move_left)
        btn2=QPushButton('Right')
        btn2.clicked.connect(self.move_right)
        layout.addWidget(btn1, 1, 0)
        layout.addWidget(btn2, 1, 2)
        btn3=QPushButton('Down')
        btn3.clicked.connect(self.move_down)
        layout.addWidget(btn3, 2, 1)





        mainlayout.addWidget(self.table)
        mlayout.addLayout(mainlayout)
        mlayout.addLayout(layout)







        self.setLayout(mlayout)

    def res_table(self):
        for i in range(4):
            for j in range(4):
                self.table.setItem(i,j,QTableWidgetItem(' '))



    def sizeHint(self):
        return QSize(700,700)






    def move_up(self):
        if self.count==0:
            self.mv=True
        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[:,i]=np.flip(k[:,i])

        self.mat=l
        self.move()

        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[:,i]=np.flip(k[:,i])
        self.mat=l

        self.matotab()




    def matotab(self):
        for i in range(4):
            for j in range(4):

                self.table.setItem(i,j,QTableWidgetItem(str(self.mat[i,j])))



    def start2048(self):
        if self.mv:
            if np.count_nonzero(self.mat)==16:
                print("Full")
                self.close()
            while True:
                i=random.randint(0,3)
                j=random.randint(0,3)
                k=random.choice([2,2,2,2,4])




                if not self.mat[i,j]:

                    self.mat[i,j]=k


                    break
        self.matotab()

    def move_down(self):
        if self.count==0:
            self.mv=True
        self.move()


    def move(self):
        if self.mv:
            self.count+=1
            #define the zero matrice

            self.glob=self.mat.copy()
            self.stack()


            self.calc()
            if np.array_equal(self.glob,self.mat):
                print('Cant move down')
                self.mv=False
                self.count=0
            self.start2048()



    def stack(self):


        for i in range(4):
            k=[0 for i in range(4)]
            count=0
            for j in range(4):
                if self.mat[3-j,i]!=0:
                    k[3-count]=self.mat[3-j,i]
                    count+=1
            self.mat[:,i]=k



        self.matotab()




    def calc(self):
        for i in range(4):
            k=[0 for i in range(4)]
            count=0
            j=0
            while j<4:
                if self.mat[3-j,i]==self.mat[2-j,i]:
                    k[3-count]=2*self.mat[3-j,i]
                    self.mat[2]
                    j+=2
                    count+=1
                elif self.mat[3-j,i]!=self.mat[2-j,i]:
                    k[3-count]=self.mat[3-j,i]
                    count+=1
                    j+=1
            self.mat[:,i]=k




        self.matotab()
























    def move_left(self):
        if self.count==0:
            self.mv=True
        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[:,i]=np.flip(k[i,:])

        self.mat=l
        self.move()

        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[i,:]=np.flip(k[:,i])
        self.mat=l

        self.matotab()
    def move_right(self):
        if self.count==0:
            self.mv=True
        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[:,i]=k[i,:]

        self.mat=l
        self.move()

        k=self.mat.copy()
        l=np.zeros([4,4])
        for i in range(4):
            l[:,i]=k[i,:]
        self.mat=l

        self.matotab()


    def paintEvent(self, event):

        painter = QPainter(self)
        brush = QBrush()
        brush.setColor(QColor('#CED0F0'))
        brush.setStyle(Qt.SolidPattern)

        rect = QRect(0, 0, painter.device().width(), painter.device().height())



        painter.fillRect(rect,brush)







app = QApplication([])
window = MainWindow()

app.exec_()
