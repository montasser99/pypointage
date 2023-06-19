#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Pointage2 employer Model
#CREATE TABLE public.employer

#)

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtSql import QSqlRelation
#from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from .ptQSqlTableModel import PtQSqlTableModel

class Pointeuse(PtQSqlTableModel):
    def __init__(self):
        super(Pointeuse,self).__init__()
        
        self.setTable("pointeuse")
        self.setHeaderData(0, Qt.Horizontal, "donnee")
        self.setHeaderData(1, Qt.Horizontal, "Valid")
        self.setTabelsToFilter(["matricule"])
        self.filter_date_field="date_j"
        self.setLimit("10")
        self.initFieldTypes()
        self.field_types[0]=self.F_String
        self.field_types[1]=self.F_Int
        self.field_types[2]=self.F_Int
        self.field_types[3]=self.F_Date
        self.field_types[4]=self.F_DateTime
        self.select()

    def insert_pointages(self, pointages):
        #insert attendence 
        #returns false if the is a problem
        if pointages==False:
            return False
        PRecord=self.record()
        PRecord.clearValues()
        for k,  v in pointages.items():
            PRecord.setValue("donnee", "K0120")
            PRecord.setValue("valid", '0')
            PRecord.setValue("maricule", v[0])
            PRecord.setValue("date_j", v[1])
            PRecord.setValue("date_time", v[1])
            if not self.insertRecord(-1, PRecord):
                sqlErr=self.lastError()
                if sqlErr.ErrorType()!='0':
                    return False
            

    @pyqtSlot()
    def transformData(self, table_model):
        print("data transformation")
        result={}
        for row in range(self.rowCount()):
            record=self.record(row)
            result[record.value("matricule")]=result.get(record.value("matricule"), 0)\
                +record.value("dateheurentree").secsTo(record.value("dateheursortie"))/3600
        row=0
        for k,  v in result.items():
            table_model.insertRows(row)
            table_model.setData(table_model.index(row, 0), k)
            table_model.setData(table_model.index(row, 1), v)
            row+=1


