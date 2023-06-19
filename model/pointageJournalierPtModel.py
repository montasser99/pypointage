#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Pointage2 Pointage journalier Model
#CREATE TABLE public.pointage_journalier
#(
#  num_poste integer NOT NULL,
#  matricule integer NOT NULL,
#  pos integer NOT NULL,
#  date date NOT NULL,
#  dateheurentree timestamp without time zone,
#  dateheursortie timestamp without time zone,
#  utilisateur integer,
#  datemodification timestamp without time zone,
#  om integer,
#  motif_id integer,
#  CONSTRAINT pointage_journalier_pkey PRIMARY KEY (num_poste, matricule, pos, date)
#)

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QTableWidgetItem
#from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from .ptQSqlTableModel import PtQSqlTableModel

class PointageJournalierPtModel(PtQSqlTableModel):
    def __init__(self):
        super(PointageJournalierPtModel,self).__init__()
        
        self.setTable("pointage_journalier")
        self.setTabelsToFilter(["matricule"])
        self.filter_date_field="date"
        self.setLimit("10")
        print(self.selectStatement())
        self.select()

    @pyqtSlot('QAbstractTableModel')
    def transformData(self, table_model):
        result={}
        for row in range(self.rowCount()):
            record=self.record(row)
            result[record.value("matricule")]=result.get(record.value("matricule"), 0)\
            +record.value("dateheurentree").secsTo(record.value("dateheursortie"))/3600
        row=0
        table_model.clearData()
        for k,  v in result.items():
            table_model.insertRows(row)
            table_model.setData(table_model.index(row, 0), k)
            table_model.setData(table_model.index(row, 1), v)
            row+=1

    @pyqtSlot('QAbstractTableModel')
    def getAttendancePerDay(self, table_model):
        result={}
        for row in range(self.rowCount()):
            record=self.record(row)
            result[record.value("date")]=result.get(record.value("date"), 0)+1
        row=0
        table_model.clearData()
        for k,  v in result.items():
            table_model.insertRows(row)
            table_model.setData(table_model.index(row, 0), k)
            table_model.setData(table_model.index(row, 1), v)
            row+=1        
