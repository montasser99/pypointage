#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#Pointage2 employer Model
#CREATE TABLE public.employer

#)

from PyQt5.QtCore import pyqtSlot,  Qt
from PyQt5.QtSql import QSqlRelation,  QSqlRecord
#from PyQt5.QtCore import (Qt, QAbstractTableModel, QModelIndex)
from PyQt5.QtWidgets import QMessageBox

#from .zkteco_pyzk_tester import PointeuseZK
from .pyzk_zkteco import PointeuseZK
from .ptQSqlTableModel import PtQSqlTableModel
from .ptModelPointeuseO import Pointeuse

class IpPointeuse(PtQSqlTableModel):
    def __init__(self):
        super(IpPointeuse,self).__init__()
        
        self.setTable("ip_pointeuse")
        self.setHeaderData(0, Qt.Horizontal, "Nom")
        self.setHeaderData(1, Qt.Horizontal, "IP")
        #self.setTabelsToFilter(["matricule", "nom", "prenom"])
        #self.filter_date_field="date_embauche"
        self.exec_button="importer"
        self.setLimit("10")
        self.initFieldTypes()
        self.field_types[0]=self.F_String
        self.field_types[1]=self.F_String
        self.field_types[2]=self.F_Int
        self.field_types[3]=self.F_String
        self.field_types[4]=self.F_Int
        self.field_types[5]=self.F_Int
        self.select()

    @pyqtSlot()
    def transformData(self, table_model=None):
        print("importation pointeuse")
        result={}
        for row in range(self.rowCount()):
            record=self.record(row)
            pointeuse=PointeuseZK(None, None, record.value("adress_ip"), record.value("port_pointeuse"))
            #result=pointeuse.create_data()
            result=pointeuse.get_data()
            if result==False:
                ret = QMessageBox.critical(None, "PyPointage",
                           "Erreur Pointeuse.\n"
                            "Exiting",
                           QMessageBox.Ok,
                           QMessageBox.Ok)
            row=0
            ptPointages=Pointeuse()
            success=ptPointages.insert_pointages(pointages=result)
            if not success:
                ret = QMessageBox.critical(None, "PyPointage",
                           "Erreur insertion Pointage.\n"
                            "Saving aborded",
                           QMessageBox.Ok | QMessageBox.Cancel,
                           QMessageBox.Cancel)
                if ret!= QMessageBox.Ok:
                    return False
        return True
#        PRecord=ptPointages.record()
#        PRecord.clearValues()
#        for k,  v in result.items():
#            PRecord.setValue("donnee", "K0120")
#            PRecord.setValue("valid", '0')
#            PRecord.setValue("maricule", v[0])
#            PRecord.setValue("date_j", v[1])
#            PRecord.setValue("date_time", v[1])
#            ptPointages.insertRecord()
#            table_model.insertRows(row)
#            table_model.setData(table_model.index(row, 0), k)
#            table_model.setData(table_model.index(row, 1), v)
#            row+=1


