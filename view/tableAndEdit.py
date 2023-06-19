# -*- coding: utf-8 -*-

"""
Module implementing TableAndEdit.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QModelIndex,  Qt
from PyQt5.QtWidgets import (QWidget, QLineEdit, QLabel, QComboBox, QDataWidgetMapper
                                                        , QMessageBox, QStyledItemDelegate, QItemEditorFactory)
from PyQt5.QtSql import QSqlRelationalDelegate

from .Ui_tableAndEdit import Ui_TableAndEdit
from .filteredTabelView import FilteredTabelView

class TableAndEdit(QWidget, Ui_TableAndEdit):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, table_model=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(TableAndEdit, self).__init__(parent)
        self.setupUi(self)
        
        self.sessionHelper=parent.sessionHelper
        self.table_model=table_model
        
        self.setupModelUI()        
        self.updateUI("view_mode")

        
    def setupModelUI(self):
        self.filteredTabelView=FilteredTabelView(self.widget, self.table_model)
        #self.filteredTabelView.tableView.setItemDelegate(QSqlRelationalDelegate(self))
        self.verticalLayout_2.addWidget(self.filteredTabelView)
        field_names=self.table_model.getFieldNames()
        self.mapper=QDataWidgetMapper(self)
        self.mapper.setModel(self.table_model)
        #for QComboBox to work correctily
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
        self.lineWidget={}
        factory= QItemEditorFactory()
        i=0
        for field_name in field_names:
            if self.table_model.getFieldType(i)==self.table_model.F_ComboBox:
                self.lineWidget[field_name]=[QLabel(self.table_model.headerData(i,  Qt.Horizontal), self), \
                    QComboBox(self), self]
                if self.table_model.relation(i).isValid():
                    #self.lineWidget[field_name][1].clear()
                    self.lineWidget[field_name][1].setModel(self.table_model.relationModel(i))
                    self.lineWidget[field_name][1].setModelColumn(
                        self.table_model.relationModel(i).fieldIndex(self.table_model.relation(i).displayColumn()))
            else:
                self.lineWidget[field_name]=[QLabel(self.table_model.headerData(i,  Qt.Horizontal), self), \
                    factory.createEditor(self.table_model.getFieldType(i), self)]
            self.mapper.addMapping(self.lineWidget[field_name][1], i)
            if self.table_model.getFieldType(i)==self.table_model.F_Date or self.table_model.getFieldType(i)==self.table_model.F_DateTime:
                self.lineWidget[field_name][1].setCalendarPopup(True)
            self.formLayout.addRow(self.lineWidget[field_name][0], 
                self.lineWidget[field_name][1])
            #self.gridLayout_2.addWidget(self.lineWidget[field_name][0], i, 0)
            #self.gridLayout_2.addWidget(self.lineWidget[field_name][1], i, 1)
            i+=1
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.toFirst()
        self.filteredTabelView.tableView.clicked.connect(self.table_clicked)
        if self.table_model.exec_button!="" :
            self.ExecB.setText(self.table_model.exec_button)

    def setupACC(self, sessionHleper):
        if not sessionHleper.hasCredential("admin"):
            self.DeleteB.setEnabled(False)

    @pyqtSlot()
    def updateUI(self,  mode):
        #UI Modes:
        #edit_mode, view_mode
        self.UI_mode=mode
        if mode=="edit_mode":
            self.sessionHelper.setDirty(dirty=True)
            print(self.sessionHelper.isDirty())
            self.SaveB.setEnabled(True)
            self.EditB.setEnabled(False)
            self.CancelB.setEnabled(True)
            self.DeleteB.setEnabled(False)
            self.NewB.setEnabled(False)
            for k, lineEdit in self.lineWidget.items():
                lineEdit[1].setEnabled(True)
        if mode=="view_mode":
            self.sessionHelper.setDirty(dirty=False)
            self.SaveB.setEnabled(False)
            self.EditB.setEnabled(True)
            self.CancelB.setEnabled(False)
            self.DeleteB.setEnabled(True)
            self.NewB.setEnabled(True)
            for k, lineEdit in self.lineWidget.items():
                lineEdit[1].setEnabled(False)
                
        self.setupACC(self.sessionHelper)
    
    @pyqtSlot(QModelIndex)
    def table_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        if (not self.table_model.isDirty()) and (self.UI_mode!="edit_mode"):
            self.mapper.setCurrentModelIndex(index)
    
    @pyqtSlot()
    def on_EditB_clicked(self):
        self.updateUI("edit_mode")
    
    @pyqtSlot()
    def on_SaveB_clicked(self):
        self.mapper.submit()
        if not self.table_model.submit():
            sqlErr=self.table_model.lastError()
            print(sqlErr.isValid())
            print(sqlErr.text())
            print(sqlErr.ErrorType())
            #print(sqlErr.databaseText())
            #print(sqlErr.driverText())
            return False
        self.updateUI("view_mode")
    
    @pyqtSlot()
    def on_DeleteB_clicked(self):
        ret = QMessageBox.warning(self, "PyPointage",
                               "The document has been modified.\n"
                                "Do you want to save your changes?",
                               QMessageBox.Ok | QMessageBox.Cancel,
                               QMessageBox.Ok)
        if ret== QMessageBox.Ok:
            self.table_model.removeRows(self.mapper.currentIndex(),  1)
    
    @pyqtSlot()
    def on_NewB_clicked(self):
        self.table_model.insertRows(self.table_model.rowCount(), 1)
        self.filteredTabelView.tableView.selectRow(self.table_model.rowCount()-1)
        self.mapper.toLast()
        self.updateUI("edit_mode")
    
    @pyqtSlot()
    def on_CancelB_clicked(self):
        self.table_model.revert()
        self.updateUI("view_mode")

    @pyqtSlot()
    def on_ExecB_clicked(self):
        if self.table_model.exec_button!="" :
            if not self.table_model.transformData():
                pass
                
