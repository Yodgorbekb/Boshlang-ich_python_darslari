# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 11:33:12 2022

@author: Ogabek
"""
               #PYTHON.05-DARS.
#ism = 'Anvar'
#print("Mening ismim " + ism)
#ism = "Yodgorbek"
##familya = "Boltayev"
#viloyat = "Xorazm"
#print(f"Salom mening ismim  {familya}  {ism}.  {viloyat} viloyatida   yashayman")
#print("Hello world!!")
#print("Hello \tworld")
#print("Hello \nworld")
#ism = "yodgorbek"
#familya = "boltaev"
#ism_sharif = f"{ism} {familya}"
#ism_sharif = ism_sharif.upper()
#print(ism_sharif.lower())
#print(ism_sharif.title())
#print(ism_sharif.capitalize())
#meva = "     olmani     "
#print(meva)
#print("Men " + meva.lstrip() + " yaxshi ko'raman")
#print("Men " + meva.rstrip() + " yaxshi ko'rman")
#print("Men " + meva.strip() + " yaxshi ko'raman")
#INPUT
#ism = input("Ismingiz nima?")
#print("Assalomu alaykum, " + ism)
#ism = input("Ismingiz nima?>>>")
#print("Assalomu alaykum, " + ism.title())
                    #AMALIYOT
#kocha = "Bog'bon" 
#mahalla = "Sog'bon" 
#tuman = "Bodamzor"
#viloyat = "Samarqand"
#print(kocha + " ko'chasi,\n " + mahalla + " mahallasi,\n " + tuman + " tumani,\n " + viloyat + " viloyati" )
#manzil = (f"{kocha}, {mahalla}, {tuman}, {viloyat}")                  
kocha = input("Ko'changizni nomini kiriting:\n>>>")                   
mahalla = input("Mahallangizni nomini kiriting:\n>>>")
tuman = input("Tumaningizni nomini kiriting:\n>>>")
viloyat = input("Viloyatingizni noini kiriting:\n>>>")
malumot = [kocha.title(), mahalla.title(), tuman.title(), viloyat.title()]
print(malumot)