#!/usr/bin/env python 
#coding:utf-8 

from zk import ZK

from PyQt5.QtCore import  QDateTime

# class des pointeuses ZKTeco base sur lib pyzk
class PointeuseZK(object):
    #initialisation
    def __init__(self,donneesProgressBar , donneesLabel, ip, port, mn=1, Type=2):
        self.ip=ip
        self.pointeuse=ZK(ip, port, timeout=10)
        self.pointages= []
        
    #ce  connecter a la pointeuese 
    def connect(self):
        try:   
            self.pointeuse.connect()
        except:
            print("Erreur de connexion, vérifier la connexion avec la pointeuse ") #.append(self.ip))

    #Lire toutes les données du journal
    def get_data(self): 
        try:
            print("start")
            #arreter la pointeuse
            #self.pointeuse.disable_device()
            #importer les données de la pointeuse
            ZKattendances=self.pointeuse.get_attendance()
        except:
            print("Erreure de lecture de la pointeuse")
        else:
            try:
                #Transformation de données
                for ZKattendance in ZKattendances:
                    print(ZKattendance)
                    #self.pointages.append(ZKattendance.user_id, ZKattendance.timestamp)
                    self.pointages.append(ZKattendance)
            except:
                print("Errreur d'importation données")
            else:
                print("Transfert resussi")
                #self.clear_log()    
                print("Pointage a ete purgé de la pointeuse")
            #reactiver la pointeuse
            #self.pointeuse.enable_device()     
        if self.pointages:
            return self.pointages
        else:
            return False
        
if __name__ == '__main__':
    print("start")
    pointeuse=PointeuseZK(None, None, "192.168.1.219", 4370)
    pointeuse.connect()
