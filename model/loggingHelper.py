#!/usr/bin/env python3 
#coding:utf-8 

#
#  loggingHelper.py
#  
#  Copyright 2021 Fares Tounsi <fares.tounsi@makeursoft.com>
#  
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  
#  

import logging
import os
from PyQt5.QtCore import  QDate

#log events in a log file
class loggingHelper(object):
    def __init__(self):
        logfile="pointeuse"+QDate.currentDate().toString("yyyy-MM-dd")+".log"
        logging.basicConfig(format='%(asctime)s %(message)s',filename=os.getcwd() + os.sep + logfile,level=logging.DEBUG) 
        
    def info(self, infostr):
        logging.info(infostr)
        
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    logger=loggingHelper()
    logger.info("test")
    sys.exit(main(sys.argv))
