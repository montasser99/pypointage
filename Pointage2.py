#!/usr/bin/env python3 
#coding:utf-8 

import sys
import os
from PyQt5.QtWidgets import QApplication

from  view.authWindow import authWindow
from model.configHelper import configHelper    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    settings=configHelper()
    with open(os.getcwd()+ os.sep +"resources/"+settings.get_value("StyleSheet/fichierCss"), 'r') as f:
        style = f.read()
        # Set the stylesheet of the application
        app.setStyleSheet(style)    
    authw=authWindow()
    authw.show()
    sys.exit(app.exec())
    
