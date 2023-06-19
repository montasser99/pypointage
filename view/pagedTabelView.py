# -*- coding: utf-8 -*-

"""
Module implementing PagedTableView.
"""

from PyQt5.QtCore import pyqtSlot, QModelIndex
from PyQt5.QtWidgets import QWidget
from PyQt5.QtSql import QSqlQueryModel

from .Ui_pagedTabelView import Ui_PagedTableView


class PagedTableView(QWidget, Ui_PagedTableView):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, tabel_name=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        @param tabel : db tabel to show
        """
        super(PagedTableView, self).__init__(parent)
        self.setupUi(self)
        
        self.tabel_name=tabel_name
        self.tableModel=QSqlQueryModel()
        self.tableModel.setQuery("SELECT * FROM "+tabel_name+" LIMIT 10");
        self.tableView.setModel(self.tableModel)        
    
    @pyqtSlot()
    def on_lineEdit_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.on_lineEdit_editingFinished()
    
    @pyqtSlot()
    def on_lineEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        self.tableModel.setQuery("SELECT * FROM "+self.tabel_name+" LIMIT "+self.lineEdit.text());
    
    @pyqtSlot()
    def on_toolButtonL_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("TODO")
    
    @pyqtSlot()
    def on_toolButtonR_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("TODO")
    
    @pyqtSlot(QModelIndex)
    def on_tableView_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        print("tableview clicked")
