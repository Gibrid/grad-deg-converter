# -*- coding: cp1251 -*-
"""
Created on Sun Nov 08 15:39:23 2009

@author: Gibrid
"""
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from math import floor, modf


class angleGMS:
    def __init__(self, grad, mins, sec):
        self.grad = float(grad)
        self.mins  = float(mins)
        self.sec  = float(sec)
        
    def convert(self):
        return (self.sec/60 + self.mins)/60 + self.grad

class angleGMS_modern:
    def set_g(self, g):
        self.g = g
    def set_m(self, m):
        self.m = m
    def set_s(self, s):
        self.s = s
    # :FIXME !!!


class angleDec:
    def __init__(self, dec):
        self.dec = float(dec)
    
    def getGrad(self):
        return floor(self.dec)

    def getMins(self):
        return floor(modf(self.dec)[0]*60)
    
    def getSec(self):
        return modf(modf(self.dec)[0]*60)[0]*60


def main():
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())


class MyWindow(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        QWidget.resize(self,120,100)

        # create objects
        label = QLabel(self.tr("Enter angle"))
        self.le = QLineEdit()
        self.te = QTextEdit()
        self.tb = QTextBrowser()

        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.tb)
        self.setLayout(layout)

        self.connect(self.le, SIGNAL("returnPressed(void)"),
            self.run_command)

    def run_command(self):
        """
        ����� ����������� � TextBrowser
        """
        import string

        try:
            angle = str(self.le.text())
            
        except ValueError:
            self.tb.append(u'Enter angle')

        else:
            flag = 'gms_to_deg'

            for char in angle:
                if char == ',':
                        """deg -> conv."""
                        flag = 'deg_to_gms'

                        
        if flag == 'gms_to_deg':
            splitted_angle = angle.split(' ')

            for i in range(3):
                    
                if len(splitted_angle) == 1:
                    grad = splitted_angle[0]
                    mins = 0
                    sec  = 0

                if len(splitted_angle) == 2:
                    grad = splitted_angle[0]
                    mins  = splitted_angle[1]
                    sec  = 0

                if len(splitted_angle) == 3:
                    grad = splitted_angle[0]
                    mins  = splitted_angle[1]
                    sec  = splitted_angle[2]
        
            ang = angleGMS(string.atof(grad),
                    string.atof(mins),
                    string.atof(sec)
                    )
        
            self.tb.append(str(ang.convert()))

        else:
            angle = angle.replace(',', '.')

            Angle = angleDec(string.atof(angle))

            self.tb.append(
                    '%d\xb0 %d\' %3.4f\"' % (Angle.getGrad(), Angle.getMins(), Angle.getSec())
                    )

if __name__ == "__main__":
    main()
