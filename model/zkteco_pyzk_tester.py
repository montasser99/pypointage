#!/usr/bin/env python 
#coding:utf-8 

import logging
import os

from zk import ZK

from PyQt5.QtCore import  QDateTime, QDate
from PyQt5.QtWidgets import QErrorMessage

from .loggingHelper import loggingHelper

# class des pointeuses ZKTeco base sur lib pyzk
class PointeuseZK(object):
    #initialisation
    def __init__(self, donneesProgressBar , donneesLabel, ip, port, mn=1, Type=2):
        self.ip=ip
        self.pointeuse=ZK(ip, port, timeout=2)
        self.pointages= []
        #QT widgets
        self.donneesProgressBar = donneesProgressBar
        self.donneesProgressBar.setMinimum(1)
        self.donneesLabel = donneesLabel
        self.donneesLabel.setText("Ready to import Data")
        
        #ficher log contien un backup de l'importation pointage
        self.logger=loggingHelper()
        logfile="pointeuse"+QDate.currentDate().toString("yyyy-MM-dd")+".log"
        logging.basicConfig(format='%(asctime)s %(message)s',filename=os.getcwd() + os.sep + logfile,level=logging.DEBUG) 

    #ce  connecter a la pointeuese 
    def connect(self):

        try:   
            self.pointeuse.connect()
            return self.pointeuse.is_connect
        except:
            self.donneesLabel.setText("Erreur de connexion, vérifier la connexion avec la pointeuse %s" %(self.ip)) #.append(self.ip))
            self.logger.info("Erreur de connexion a la pointeuse :"+str(self.ip))
            em = QErrorMessage(self.donneesLabel)
            em.showMessage("Erreur de connexion a la pointeuse :"+str(self.ip))
            return False
    
    #deconnecter la pointeuse
    def disconnect(self):
        if self.pointeuse.is_connect:
            self.pointeuse.disconnect()
    
    #Lire toutes les données du journal
    def create_data(self):
        try:
            self.logger.info("lancement de l'importation du pointage")
            self.connect()
            #arreter la pointeuse
            self.pointeuse.disable_device()
            #importer les données de la pointeuse
            ZKattendances=self.pointeuse.get_attendance()
            # activer la pointeuse
            self.pointeuse.enable_device()
            self.disconnect()
        except:
            self.donneesLabel.setText("Erreure de lecture de la pointeuse")
            self.logger.info("Erreure de lecture de la pointeuse")
        else:
            try:
                self.donneesProgressBar.setMaximum(len(ZKattendances))
                Progres_val=1
                #Transformation de données
                if ZKattendances:
                    for ZKattendance in ZKattendances:
                        self.pointages.append((ZKattendance.user_id, QDateTime(ZKattendance.timestamp)))
                        logstr="|"+ZKattendance.user_id+" | "+QDateTime(ZKattendance.timestamp).toString("yyyy-MM-dd HH:mm:ss")
                        self.logger.info(logstr)
                        self.donneesProgressBar.setValue(Progres_val)
                        Progres_val=Progres_val+1
                    self.donneesLabel.setText("Lecture Terminé")
                else :
                    self.donneesLabel.setText("Pointeuse est Vide")
                    self.logger.info("Pointeuse est Vide")
            except:
                print("Errreur de transformation de données")
            else:
                self.logger.info("Transfert resussi")
                if __name__ != '__main__':
                    #self.clear_log()    
                    self.logger.info("Pointage a ete purgé de la pointeuse")

        
        
        if self.pointages:
            return self.pointages
        else:
            return False
            
        
    #Effacer tout les présences du journal de la pointeuse
    def clear_log(self):
        if self.pointeuse.is_connect:
            self.pointeuse.clear_attendance()
            self.logger.info("Purge du pointage")
        
    #Activer ou désactiver le dispositif
    def enabled(self, state=1):
        print("start")
        
    #Activer ou désactiver le matricule
    def enabledUser(self, matricule=0,  state=1):
        print("start")

    #liser les utilisateur de la pointeuse
    def get_users(self):
        return self.pointeuse.get_users()
    
    #cree ou MASJ ustilisateur
    def set_user(self, name, user_id):
#        self.pointeuse.set_user( uid=None, name, privilege=0, password='', group_id=None, user_id=user_id, card=None)
        self.pointeuse.set_user( None, name, 0, '', 0, user_id, 0)
        
#Test de la class        
if __name__ == '__main__':
    
    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWidgets import QWidget, QProgressBar, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem
    
    print("teste"+" unitaire")
    #cearte test Widget
    app = QApplication(sys.argv)
    mainw= QWidget()
    mainw.resize(600, 600)
    vlayout=QVBoxLayout()
    mainw.setLayout(vlayout)
    lable=QLabel(mainw)
    progressbar=QProgressBar(mainw)
    tab1=QTableWidget( 1, 7, mainw)
    tab2=QTableWidget( 1, 2, mainw)
    
    vlayout.addWidget(lable)
    vlayout.addWidget(progressbar)
    vlayout.addWidget(tab1)
    vlayout.addWidget(tab2)
    
    mainw.show()

    pointeuse=PointeuseZK(progressbar, lable, "192.168.1.219", 4370)
    print("connection pointeuse is : "+str(pointeuse.pointeuse.is_connect))
    #pointeuse.connect()
    pointages=pointeuse.create_data()
    #print(pointages)
    tab2.setHorizontalHeaderLabels(("Matricule", "Temp"))
    row=0
    if pointages:
        for pointage in pointages:        
            tab2.setItem(row,0,QTableWidgetItem(pointage[0]))
            tab2.setItem(row,1,QTableWidgetItem(pointage[1].toString()))
            row+=1
            tab2.insertRow(row)
    tab2.resizeColumnsToContents()
    
    #pointeuse.connect()
    #pointeuse.set_user("FT34",34)
    usersList=[]
    #usersList=pointeuse.get_users()
    #pointeuse.disconnect()
    tab1.setHorizontalHeaderLabels(("uid", "name", "privilege", "password", "group_id", "user_id", "card"))
    row=0
    for user in usersList:        
        tab1.setItem(row,0,QTableWidgetItem(user.uid))
        tab1.setItem(row,1,QTableWidgetItem(user.name))
        tab1.setItem(row,2,QTableWidgetItem(user.privilege))
        tab1.setItem(row,3,QTableWidgetItem(user.password))
        tab1.setItem(row,4,QTableWidgetItem(user.group_id))
        tab1.setItem(row,5,QTableWidgetItem(user.user_id))
        tab1.setItem(row,6,QTableWidgetItem(user.card))
        row+=1
        tab1.insertRow(row)
    tab1.resizeColumnsToContents()
            
    sys.exit(app.exec_())
    
