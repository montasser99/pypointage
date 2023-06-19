#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#paged table model
#adds limit and pagintion to qsqltablemodel

from PyQt5.QtCore import pyqtSlot, QMetaType,  Qt
from PyQt5.QtSql import QSqlRelationalTableModel

class PtQSqlTableModel(QSqlRelationalTableModel):
    #define field types for QItemEditorFactory
    F_ComboBox=QMetaType.Bool
    F_Double=QMetaType.Double
    F_Int=QMetaType.Int
    F_Date=QMetaType.QDate
    F_DateTime=QMetaType.QDateTime
    F_String=QMetaType.QString
    F_Tine=QMetaType.QTime
    
    def __init__(self):
        super(PtQSqlTableModel,self).__init__()
        
        self.tabels_to_filter=[self.record().fieldName(1)]
        self.field_names=[]
        self.field_types=[]
        self.qry_str="1=1"
        self.limit=""
        self.filter_date_field=""
        self.exec_button=""
        
    def getFieldNames(self):
        #returns fild names in an Array
        if self.field_names:
            return self.field_names
        else:
            rc=self.record()
            for i in range(rc.count()):
                self.field_names.append(self.record().fieldName(i))
            return self.field_names

    def initFieldTypes(self):
        rc=self.record()
        for i in range(rc.count()): 
            self.field_types.append(self.F_String)
            
    def getFieldType(self, field_index):
        #returns widget type to use in QItemEditorFactory
        if field_index < len(self.field_types):
            return self.field_types[field_index]
        return  self.F_String
            
    def setTabelsToFilter(self,  tabels=[]):
        #tabels to query for MultiFilter
        self.tabels_to_filter=tabels
        
    @pyqtSlot(str)
    def setMultiFilter(self, filter_str="", date1=None,  date2=None):
        #set multiple filters from string
        self.qry_str=""
        if filter_str=="" and  date1==None and date2==None:
            self.setFilter("")
            self.select()
            return True
        sub_filter_str=filter_str
        fisrt=True
        for table_name in self.tabels_to_filter:
            if fisrt:
                fisrt=False
                self.qry_str+="(CAST("+table_name+" AS TEXT) ILIKE '%"+sub_filter_str+"%'"
            else:
                self.qry_str+=" OR CAST("+table_name+" AS TEXT) ILIKE '%"+sub_filter_str+"%'"
        self.qry_str+=") "
        if self.filter_date_field!="":
            if date1!=None:  #use Qt.ISODate format for sql query
                self.qry_str+=" AND "+self.filter_date_field+"> '"+date1.toString(Qt.ISODate)+"'"
            if date2!=None:
                self.qry_str+=" AND "+self.filter_date_field+"<'"+date2.toString(Qt.ISODate)+"'"
        self.setFilter(self.qry_str)
        #print(self.selectStatement())
        return True
        
    def setLimit(self,  limit=""):
        if limit=="0":
            limit=""
        self.limit=limit
        
    def selectStatement(self):
    #reimplemented method to set limit
        query=super(PtQSqlTableModel,self).selectStatement()
        if self.limit!="":
            query+=" LIMIT "+self.limit
        return query
        
    def buildQryStr(self, filter_str="1=1", limit="100"):
        pass

    @pyqtSlot(int)
    def setPageSize(self,  limit):
        #set page size
        self.setLimit(limit)
        self.setFilter(self.qry_str)
        
    @pyqtSlot()
    def transformData(self, table_model):
        return True
