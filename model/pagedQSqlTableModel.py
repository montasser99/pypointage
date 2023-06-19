#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#paged table model
#adds limit and pagintion to qsqltablemodel

from PyQt5.QtSql import QSqlTableModel

class PagedQSqlTableModel(QSqlTableModel):
    def __init__(self):
        super(PagedQSqlTableModel,self).__init__()
        
    def setPageSize(self):
        """
        Public method 
        
        @return DESCRIPTION
        @rtype TYPE
        """
        #set page size
        return True
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    sys.exit(app.exec())
    
    
