#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2021 fares T <fares@mx>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from PyQt5.QtSql import QSqlDatabase

from model.configHelper import configHelper

#magages connection to databeses
class connectionHelper():
    def __init__(self):
        self.settings=configHelper()
        
    def connect_all(self):
        self.connect_main()
        
    def connect_main(self):
        #default database
        db = QSqlDatabase().addDatabase(self.settings.get_value("Connexion/pilote"))
        db.setDatabaseName(self.settings.get_value("Connexion/database"))
        db.setHostName(self.settings.get_value("Connexion/host"))
        db.setUserName(self.settings.get_value("Connexion/user"))
        db.setPassword(self.settings.get_value("Connexion/password"))
        db.open()
        if db.isOpenError():
            print(db.lastError().text())

    def close_connections(self):
        db=QSqlDatabase()
        db.close()
        
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
