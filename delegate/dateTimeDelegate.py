# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDateTimeEdit, QItemDelegate
from PyQt5.QtCore import Qt, QDate, QDateTime

class DateTimeDelegate(QItemDelegate):
    
    def __init__(self, parent, columDefaultDate=-1):
        QItemDelegate.__init__(self, parent)
        self.columDefaultDate = columDefaultDate
    
    def createEditor(self, parent, option, index):
        self.dateEdit = QDateTimeEdit(parent)
        #self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setButtonSymbols(2)
        if self.columDefaultDate >=0:
            date = index.model().data(index.model().index(index.row(),self.columDefaultDate),Qt.DisplayRole)
        else:
            date =QDate(2000, 1, 1)
            
        self.dateEdit.setMinimumDate(date)
        self.dateEdit.setDisplayFormat("dd/MM/yyyy HH:mm")
        return self.dateEdit

    def setModelData(self, editor, model, index):
        self.dateEdit.setDisplayFormat("dd/MM/yyyy HH:mm")
        if self.dateEdit.dateTime().time().toString("hh:mm")=="00:00":
            model.setData(index, QDateTime(), Qt.EditRole)
        else:
            model.setData(index, self.dateEdit.dateTime(), Qt.EditRole)
    
