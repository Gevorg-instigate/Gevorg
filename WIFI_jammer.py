#!/usr/bin/python

import sys
from PyQt4.QtGui import QWidget, QApplication, QMainWindow, QPushButton, \
                        QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout, \
                        QComboBox


class main_window(QWidget):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent) 
        self.window_config()
        self.set_layout()

    def set_layout(self):
        form = QFormLayout()
        grid = QGridLayout()
        vbox = QVBoxLayout()
        grid.addLayout(self.create_spinBox(), 0, 0)
        grid.addLayout(self.create_buttons(), 1, 0)
        form.addRow(grid)
        vbox.addLayout(form)
        self.setLayout(vbox)

    def create_buttons(self):
        hbox = QHBoxLayout()
        hbox.addLayout(self.set_scan_button())
        hbox.addLayout(self.set_jammer_button())
        return hbox

    def create_spinBox(self):
        wifi_name = QComboBox()
        wifi_name.addItems('-')
        hbox = QHBoxLayout()
        hbox.addWidget(wifi_name)
        return hbox

    def set_scan_button(self):
        scan_button = QPushButton('Scan')
        vbox = QVBoxLayout()
        vbox.addWidget(scan_button)
        return vbox

    def set_jammer_button(self):
        jammer_button = QPushButton('Jammer')
        vbox = QVBoxLayout()
        vbox.addWidget(jammer_button)
        return vbox

    def window_config(self):
        self.setWindowTitle("WIFI Jammer")
        self.move(450, 150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    obj = main_window()
    obj.show()
    sys.exit(app.exec_())
