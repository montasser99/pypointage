# -*- coding: utf-8 -*-

"""
Module implementing authWindow.
"""
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtSql import QSqlQuery

from .Ui_authWindow import Ui_authWindow
from  view.mainWindow import MainWindow
from model.connectionHelper import connectionHelper
from model.sessionHelper import SessionHelper

class authWindow(QDialog, Ui_authWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(authWindow, self).__init__(parent)
        self.setupUi(self)
        
        #self.sessionHelper=SessionHelper("")
        
        self.connector=connectionHelper()
        self.connector.connect_main()
    
    @pyqtSlot(str)
    def on_lineEditUsr_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.clearWaningLable()
    
    @pyqtSlot()
    def on_lineEditUsr_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.check_password()
    
    @pyqtSlot(str)
    def on_lineEditPwd_textChanged(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.clearWaningLable()
    
    @pyqtSlot()
    def on_lineEditPwd_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.check_password()
    
    @pyqtSlot()
    def on_cancelButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    @pyqtSlot()
    def on_okButton_clicked(self):
        """
        Slot documentation goes here.
        """
        self.check_password()

    def check_password(self):
        query=QSqlQuery("SELECT utilisateur,mp FROM utilisateur where utilisateur like '"+self.lineEditUsr.text()+"'and mp like '"+self.lineEditPwd.text()+"'")
        #pwField=query.record().indexOf("utilisateur")
        #usrField=query.record().indexOf("mp")
        if query.next():
            self.sessionHelper=SessionHelper(self.lineEditUsr.text())
            self.start_app()
        elif self.lineEditUsr.text()=="":
            self.sessionHelper=SessionHelper("anon")
            self.start_app()
        else:
            self.setWarningLabel()
    
    def start_app(self):
        self.connector.close_connections()
        self.mainw=MainWindow(self.sessionHelper)
        self.mainw.show()
        self.close()
        
    def clearWaningLable(self):
        self.label.clear()
        
    def setWarningLabel(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("authWindow", "Login Failed"))
        
   # @pyqtSlot()
    def accept(self):
        return True
