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
from PyQt5.QtWidgets import QMessageBox

class SessionHelper():
    def __init__(self, user,  parent=None):
        self.user_name=user
        self.is_dirty=False
        self.parent=parent
        
    def getUserName(self):
        return self.user_name
        
    def hasCredential(self, credential=str):
        if self.user_name=="admin":
            return True
        return False
        
    def setDirty(self, window="self", dirty=False):
        self.is_dirty=dirty
        
    def isDirty(self, window=None):
        return self.is_dirty
    
    def echoDirty(self):
        ret = QMessageBox.warning(self.parent, "PyPointage",
                               "The document has been modified.\n"
                                "Exit Without Saving?",
                               QMessageBox.Ok | QMessageBox.Cancel,
                               QMessageBox.Cancel)
        if ret== QMessageBox.Ok:
            return True
        return False
