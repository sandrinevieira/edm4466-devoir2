#coding: utf-8

import csv
import json 
import requests

#Ceci sera le nom de mon ficher csv final (w+ efface le fichier csv lorsqu'on run le code à nouveau, pour pas que ça s'accumule)
fichier = "devoirlobby.csv"
fraise = open(fichier, "w+")

#Ceci est l'URL json du registre du lobby
url = "http://jhroy.ca/uqam/lobby.json" 

#Requête pour accéder à l'URL json
req = requests.get(url)
#print(req)

#Ceci est mon loop
if req.status_code==200:
     #print ("Ça fonctionne")
     lobby= req.json()
     for variable in lobby["registre"]:

          #Condition pour viser les sujets en lien avec le climat seulement
          if "limat" in variable[1][0]["objet"] or "limat" in variable[1][0]["objet_autre"]:

               #Définir les variables
               resultat = []
               NomFR= variable[0]["fr_client_org_corp_nm"]
               NomANG= variable[0]["en_client_org_corp_nm"]
               CodeLobby =variable[0]["client_org_corp_num"]
               DateCom = variable[0]["date_comm"]
               SujetPremier = variable[1][0]["objet"]
               SujetDeuxieme = variable[1][0]["objet_autre"]

               resultat.append(SujetPremier)
               resultat.append(SujetDeuxieme)
               resultat.append(NomFR)
               resultat.append(NomANG)
               resultat.append(CodeLobby)
               resultat.append(DateCom)

               print(resultat)
          
               #Écriture du fichier csv
               framboise = csv.writer(fraise)
               framboise.writerow(resultat)


