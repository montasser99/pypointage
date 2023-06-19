#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Pointage2 employer Model
#CREATE TABLE public.employer
#(
#  matricule integer NOT NULL,
#  matriculedrh integer,
#  nom character varying,
#  prenom character varying,
#  sexe character varying,
#  etat_civil character varying,
#  "position" character varying(20),
#  date_embauche date,
#  date_fincontrat date,
#  societe integer,
#  formation integer,
#  dateresilier date,
#  recup integer,
#  resiliation integer,
#  departement integer,
#  typedepaie integer,
#  cin character varying,
#  plus integer DEFAULT 0,
#  CONSTRAINT employer_pkey PRIMARY KEY (matricule)
#)

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtSql import QSqlRelation
#from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)

from .ptQSqlTableModel import PtQSqlTableModel

class employerPtModel(PtQSqlTableModel):
    def __init__(self):
        super(employerPtModel,self).__init__()
        
        self.setTable("employer")
        #self.select()
        self.setHeaderData(0, Qt.Horizontal, "Matricule")
        self.setHeaderData(11, Qt.Horizontal, "Date Resiliation")
        self.setTabelsToFilter(["matricule", "nom", "prenom"])
        self.filter_date_field="date_embauche"
        self.setLimit("10")
        print(self.selectStatement())
        self.initFieldTypes()
        self.field_types[4]=self.F_ComboBox
        self.field_types[5]=self.F_ComboBox
        self.field_types[6]=self.F_ComboBox
        self.field_types[7]=self.F_Date
        self.field_types[8]=self.F_Date
        self.field_types[9]=self.F_ComboBox
        self.field_types[11]=self.F_Date
        self.field_types[13]=self.F_ComboBox
        self.field_types[14]=self.F_ComboBox
        self.field_types[15]=self.F_ComboBox
        self.setRelation(4, QSqlRelation("sexe", "sexe_designation", "sexe_designation"))
        self.setRelation(5, QSqlRelation("etat_civil", "etat_civil_designation", "etat_civil_designation"))
        self.setRelation(6, QSqlRelation("position", "position_designation", "position_designation"))
        self.setRelation(9, QSqlRelation("societe", "code", "societe"))
        self.setRelation(14, QSqlRelation("departement", "num_departement", "des"))
        self.setRelation(13, QSqlRelation("ouinon", "ouinon_id", "ouinon_designation"))
        self.setRelation(15, QSqlRelation("typedepaie", "code", "des"))
        self.select()

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


