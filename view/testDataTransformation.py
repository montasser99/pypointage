# -*- coding: utf-8 -*-

"""
Module implementing TestDataTransformation.
"""

from PyQt5.QtCore import pyqtSlot,  pyqtSignal
from PyQt5.QtWidgets import QWidget

from .Ui_testDataTransformation import Ui_TestDataTransformation
from .filteredTabelView import FilteredTabelView

class TestDataTransformation(QWidget, Ui_TestDataTransformation):
    """
    Class documentation goes here.
    """
    startCalculation= pyqtSignal('QAbstractTableModel')
    startCalculation_2= pyqtSignal('QAbstractTableModel')
    
    def __init__(self, parent=None, tabel_model=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(TestDataTransformation, self).__init__(parent)
        self.setupUi(self)
        
        
        self.result=TableModel()
        self.tableView_res.setModel(self.result)
        self.model=tabel_model
        self.filteredTabelView=FilteredTabelView(self, self.model)
        self.verticalLayout.addWidget(self.filteredTabelView)
        
        self.startCalculation_2.connect(self.model.transformData)
        self.startCalculation.connect(self.model.getAttendancePerDay)
        
    
    @pyqtSlot()
    def on_pushButtonRun_clicked(self):
        """
        Slot documentation goes here.
        """
        self.startCalculation.emit(self.result)
        #self.model.transformData(self.result)
        #self.result=TableModel(self.model.transformData())
        #self.tableView_res.setModel(self.result)
    
    @pyqtSlot()
    def on_pushButtonRun_2_clicked(self):
        """
        Slot documentation goes here.
        """
        self.startCalculation_2.emit(self.result)

from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)
import operator

class TableModel(QAbstractTableModel):

    def __init__(self, addresses=None, parent=None):
        super().__init__(parent)

        if addresses is None:
            self.addresses = []
        else:
            self.addresses = addresses

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows the model holds. """
        return len(self.addresses)

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns the model holds. """
        return 2

    def data(self, index, role=Qt.DisplayRole):
        """ Depending on the index and role given, return data. If not
            returning data, return None (PySide equivalent of QT's
            "invalid QVariant").
        """
        if not index.isValid():
            return None

        if not 0 <= index.row() < len(self.addresses):
            return None

        if role == Qt.DisplayRole:
            Matricule = self.addresses[index.row()]["Matricule"]
            Hrs = self.addresses[index.row()]["Hrs"]

            if index.column() == 0:
                return Matricule
            elif index.column() == 1:
                return Hrs

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Horizontal:
            if section == 0:
                return "Matricule"
            elif section == 1:
                return "Hrs"

        return None

    def insertRows(self, position, rows=1, index=QModelIndex()):
        """ Insert a row into the model. """
        self.beginInsertRows(QModelIndex(), position, position + rows - 1)

        for row in range(rows):
            self.addresses.insert(position + row, {"Matricule": "", "Hrs": ""})

        self.endInsertRows()
        return True

    def removeRows(self, position, rows=1, index=QModelIndex()):
        """ Remove a row from the model. """
        self.beginRemoveRows(QModelIndex(), position, position + rows - 1)

        del self.addresses[position:position + rows]

        self.endRemoveRows()
        return True
        
    def clearData(self):
        """ Remove all data from the model. """
        self.removeRows(0, self.rowCount())

    def setData(self, index, value, role=Qt.EditRole):
        """ Adjust the data (set it to <value>) depending on the given
            index and role.
        """
        if role != Qt.EditRole:
            return False

        if index.isValid() and 0 <= index.row() < len(self.addresses):
            address = self.addresses[index.row()]
            if index.column() == 0:
                address["Matricule"] = value
            elif index.column() == 1:
                address["Hrs"] = value
            else:
                return False

            self.dataChanged.emit(index, index)
            return True

        return False
        
    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.layoutAboutToBeChanged.emit()
        self.addresses = sorted(self.addresses, key=operator.itemgetter(
            self.headerData(Ncol,  Qt.Horizontal)))        
        if order == Qt.DescendingOrder:
            self.addresses.reverse()
        self.layoutChanged.emit()

    def flags(self, index):
        """ Set the item flags at the given index. Seems like we're
            implementing this function just to see how it's done, as we
            manually adjust each tableView to have NoEditTriggers.
        """
        if not index.isValid():
            return Qt.ItemIsEnabled
        return Qt.ItemFlags(QAbstractTableModel.flags(self, index) |
                            Qt.ItemIsEditable)
