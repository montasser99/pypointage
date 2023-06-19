# -*- coding: utf-8 -*-

"""
Module implementing Employers.
"""

from PyQt5.QtCore import pyqtSlot,  QModelIndex
from PyQt5.QtWidgets import QWidget,  QDataWidgetMapper, QMessageBox
#from PyQt5.QtSql import QSqlTableModel,  QSqlRecord

from .Ui_employers import Ui_Employers
from model.ptQSqlTableModel import PtQSqlTableModel

class Employers(QWidget, Ui_Employers):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(Employers, self).__init__(parent)
        self.setupUi(self)
        self.updateUI("view_mode")
        self.setupACC(parent.sessionHelper)
        
        self.employerModel=PtQSqlTableModel()
        self.employerModel.setTable("employer")
        self.employerModel.setEditStrategy(PtQSqlTableModel.OnRowChange)
        self.employerModel.select()
        self.employerModel.setTabelsToFilter(["matricule", "nom",  "prenom",  "sexe"])
        self.tableEmployers.setModel(self.employerModel)
        #mapping to widgets
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.employerModel)
        self.mapper.addMapping(self.lineEdit,  0)
        self.mapper.addMapping(self.lineEdit_matriculeDRH,  1)
        self.mapper.addMapping(self.lineEdit_2,  2)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.toFirst()
        
        #connections
        self.employerModel.primeInsert.connect(self.initRow)
        #self.employerModel.beforeUpdate.connect(self.confirm_update)
        
    @pyqtSlot(QModelIndex)
    def on_tableEmployers_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        if not self.employerModel.isDirty():
            self.mapper.setCurrentModelIndex(index)
    
    @pyqtSlot()
    def on_CancelB_clicked(self):
        """
        Slot documentation goes here.
        """
        self.employerModel.revert()
        self.updateUI("view_mode")
    
    @pyqtSlot()
    def on_NewB_clicked(self):
        """
        Slot documentation goes here.
        """
        self.employerModel.insertRows(self.employerModel.rowCount(), 1)
        self.tableEmployers.selectRow(self.employerModel.rowCount()-1)
        self.mapper.toLast()
    
    @pyqtSlot()
    def on_SaveB_clicked(self):
        """
        Slot documentation goes here.
        """
        self.mapper.submit()
        if not self.employerModel.submit():
            sqlErr=self.employerModel.lastError()
            print(sqlErr.text())

    @pyqtSlot(int, "QSqlRecord&")
    def initRow(self, row, record):
        #populate the new row with Predifined Data
        record.setValue(0,  0)
        record.setValue(1,  0)
        record.setValue(2,  "basla")
        self.mapper.submit()

    @pyqtSlot(int, "QSqlRecord&")
    def confirm_update(self, row, record):
        #confirme before saving data
        ret = QMessageBox.warning(self, "PyPointage",
                               "The document has been modified.\n"
                                "Do you want to save your changes?",
                               QMessageBox.Ok | QMessageBox.Cancel,
                               QMessageBox.Ok)
        if ret==QMessageBox.Cancel:
            self.employerModel.revertAll()
        
    @pyqtSlot()
    def on_DeleteB_clicked(self):
        """
        Slot documentation goes here.
        """
        ret = QMessageBox.warning(self, "PyPointage",
                               "The document has been modified.\n"
                                "Do you want to save your changes?",
                               QMessageBox.Ok | QMessageBox.Cancel,
                               QMessageBox.Ok)
        if ret== QMessageBox.Ok:
            self.employerModel.removeRows(self.mapper.currentIndex(),  1)
    
    @pyqtSlot()
    def on_lineEdit_filter_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.employerModel.setMultiFilter(self.lineEdit_filter.text())

    @pyqtSlot()
    def on_EditB_clicked(self):
        """
        Slot documentation goes here.
        """
        self.updateUI("edit_mode")
        
    def setupACC(self, sessionHleper):
        if not sessionHleper.hasCredential("admin"):
            self.DeleteB.setEnabled(False)

    @pyqtSlot()
    def updateUI(self,  mode):
        #UI Modes:
        #edit_mode, view_mode
        if mode=="edit_mode":
            self.SaveB.setEnabled(True)
            self.EditB.setEnabled(False)
        if mode=="view_mode":
            self.SaveB.setEnabled(False)
            self.EditB.setEnabled(True)            
