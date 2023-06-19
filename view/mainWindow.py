# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QLocale
from PyQt5.QtWidgets import QMainWindow

from .Ui_mainWindow import Ui_MainWindow
from model.configHelper import configHelper
from model.connectionHelper import connectionHelper

#sub windows
from .employers import Employers
#from .pagedTabelView import PagedTableView
from .filteredTabelView import FilteredTabelView
from .testDataTransformation import TestDataTransformation
from .tableAndEdit import TableAndEdit

#testing
from model.pointageJournalierPtModel import PointageJournalierPtModel
from model.employerPtModel import employerPtModel
from model.ptModelIpPointeuseO import IpPointeuse
from model.ptModelPointeuseO import Pointeuse

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, sessionHelper, parent=None):
        """
        Constructor)
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setLocale(QLocale(QLocale.French, QLocale.France))
        
        settings=configHelper()
        self.sessionHelper=sessionHelper
        self.sessionHelper.parent=parent
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info), self.sessionHelper.getUserName())
        self.connector=connectionHelper()
        #self.connector.connect_main()

    
    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        if self.sessionHelper.isDirty():
            if not self.sessionHelper.echoDirty():
                return False
        self.connector.close_connections()
        self.close()
        # TODO: not implemented yet
        #raise NotImplementedError
    
    
    @pyqtSlot()
    def on_actionListe_des_personnels_triggered(self):
        """
        Slot documentation goes here.
        """
        if not hasattr(self, "employersW"):
            self.employersW=Employers(self)
            self.tabWidget.addTab(self.employersW, "Liste Employers")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.employersW))
        
    def tab_is_not_open(self):
        return True
    
    @pyqtSlot()
    def on_actionListe_de_Pointage_triggered(self):
        """
        Slot documentation goes here.
        """
        if not hasattr(self, "listePointage"):
            self.listePointage=FilteredTabelView(self, PointageJournalierPtModel())
            self.tabWidget.addTab(self.listePointage, "Liste Pointage")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.listePointage))
    
    @pyqtSlot()
    def on_actionCalcule_Pointage_triggered(self):
        """
        Slot documentation goes here.
        """
        if not hasattr(self, "testCalcule"):
            model=PointageJournalierPtModel()
            self.testCalcule=TestDataTransformation(self, tabel_model=model)
            self.tabWidget.addTab(self.testCalcule, "Test de Calcule")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.testCalcule))
    
    @pyqtSlot()
    def on_actionListe_ptModel_triggered(self):
        """
        Slot documentation goes here.
        """
        if not hasattr(self, "listeModel"):
            model=employerPtModel()
            #model=PointageJournalierPtModel()
            self.listeModel=TableAndEdit(self, model)
            self.tabWidget.addTab(self.listeModel, "Liste model")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.listeModel))
    
    @pyqtSlot()
    def on_actionlecture_pointeuse_triggered(self):
        #lecture et importation pointeuse
        if not hasattr(self, "lecturePointeuse"):
            model=IpPointeuse()
            #model=PointageJournalierPtModel()
            self.lecturePointeuse=TableAndEdit(self, model)
            self.tabWidget.addTab(self.lecturePointeuse, "lecture Pointeuse")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.lecturePointeuse))

    @pyqtSlot()
    def on_actionPointage_Brute_triggered(self):
        #lecture et importation pointeuse
        if not hasattr(self, "pointageBrut"):
            model=Pointeuse()
            #model=PointageJournalierPtModel()
            self.pointageBrut=TableAndEdit(self, model)
            self.tabWidget.addTab(self.pointageBrut, "pointage Brut")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(self.pointageBrut))
        
