# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDateTimeEdit, QItemDelegate
from PyQt5.QtCore import Qt


class CalenderPopupDelegate(QItemDelegate):
    
    def __init__(self, parent):
        QItemDelegate.__init__(self, parent)
       
    def createEditor(self, parent, option, index):
        self.dateEdit = QDateTimeEdit(parent)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        return self.dateEdit
        

    def setModelData(self, editor, model, index):
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        model.setData(index, self.dateEdit.date(), Qt.EditRole)
        
