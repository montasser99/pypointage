# -*- coding: utf-8 -*-

"""
Module implementing FilteredTabelView.
"""

from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget
#from PyQt5.QtSql import QSqlTableModel

from .Ui_filteredTabelView import Ui_FilteredTabelView


class FilteredTabelView(QWidget, Ui_FilteredTabelView):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, tabel_model=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(FilteredTabelView, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_limit.setValidator(QIntValidator(0, 9999, self))
        self.dateTimeEdit.setDate(QDate.currentDate().addYears(-20))
        self.dateTimeEdit_2.setDate(QDate.currentDate())
        
        self.model=tabel_model
        #self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tableView.setModel(self.model)
    
    @pyqtSlot()
    def on_lineEdit_filter_returnPressed(self):
        """
        Slot documentation goes here.
        """
        #self.model.setMultiFilter(self.lineEdit_filter.text())
        self.setFilters()
    
    @pyqtSlot()
    def on_lineEdit_limit_returnPressed(self):
        """
        Slot documentation goes here.
        """
        self.model.setPageSize(self.lineEdit_limit.text())
    
    @pyqtSlot()
    def on_dateTimeEdit_editingFinished(self):
        """
        Slot documentation goes here.
        """
        self.setFilters()
    
    @pyqtSlot()
    def on_dateTimeEdit_2_editingFinished(self):
        """
        Slot documentation goes here.
        """
        self.setFilters()
        
    @pyqtSlot()
    def setFilters(self):
        self.model.setMultiFilter(self.lineEdit_filter.text(), self.dateTimeEdit.dateTime(), self.dateTimeEdit_2.dateTime())

