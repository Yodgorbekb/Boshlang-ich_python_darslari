# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:27:25 2022

@author: Ogabek
"""
       #TARTIBLASH
#cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
#   cars.sort()
#   print(cars)
# reverse- teskari


#min(), max(), sum()

#narxlar = [12000,23456,9800,5600,9934,32874]
#arzon = min(narxlar)
#qimmat = max(narxlar)
#jami = sum(narxlar)
#print("Eng arzon narh ", arzon, ". Eng qimmati ", qiymat,  "Jami" , jami)

#RO'YXATNI KESISH
#cars = ['bmw', 'mercedez benz', 'volvo', 'general motors', 'tesla', 'audi']
#my_cars = [0:3]
#print(my_cars)
#print(cars[2:5])
#print(cars[:4])

#RO'YXATDAN NUSXA OLISH


# TUPLE
#toys = ('bus', 'car', 'bear', 'dino')
#davlat = ("O'zbekiston", "Rossiya", "Xitoy", "Angliya", "Ozarbayjon", "Tojikiston")
                                       #PYTHON. 09-DARS
                                       #FOR TSIKLI BILAN TANISHAMIZ.
#mehmonlar = ['Ali', 'Vali', 'Husan', 'Hasan', 'Olim']   
#for mehmon in mehmonlar:
#   print("Salom", mehmon)
#   print("Hayr,", mehmon)     
#mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
#for mehmon in mehmonlar:
#       print(f"Hurmatli {mehmon}, sizni 25 Fevral kuni tug'ilgan kunimga taklif qilaman")
#       print("Hurmat bilan, Polonchiyevlar oilasi\n")  
#sonlar = list(range(1,11))
#for son in sonlar:
#        print(f"{son} ning kvadrati {son**2} ga teng")
#sonlar = list(range(11))
#sonlar_kvadrati = []
#for son in sonlar:
#         sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)
#dostlar = []
#print("5 ta eng yaqin do'stingiz kim?")
#for n in range(5):      
#      dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
#print(dostlar)
                              #AMALIYOT
#ismlar = ['Ali', 'Vali', 'Sarvar', 'Jasur', 'Olim']
#for ism in ismlar:
#   print("Salom ",  ism)                             
#   print("Hayr ", ism)
#print(f"Kod {len(ismlar)} marta takrorlandi")                          
#sonlar = list(range(11,100,2))
#kinolar = []
#print("5 ta sevimli kinolaringizni kiriting?")
#for k in range(5):
#     kinolar.append(input(f"{k+1}-kino:"))                        
#print(kinolar)
#print("Bugun necha kishi bilan uchrashdingiz?>>>")
#dostlar = []
#for n in range(5):
#        dostlar.append(input(f"{n+1}-suhabat qilgan odamingiz kim edi: "))                                 
#print(dostlar)                            
                              
                              
                                  #PYTHON DARSLARI.10-DARS
                                  #MAVZU: IF-ELSE shartlari
                                  # va tarmoqlanish
#avtolar = ['audi','bmw','volvo','kia','hyundai']
#for avto in avtolar:
#    if avto == 'bmw':#..agar avto bmw ga teng bo'lsa...
#        print(avto.upper())
#    else:#aks holda...
#        print(avto.title())
#ism = "Ali"        
#ism.lower() == "ali"
#(==) tengmi?
#(!=)teng emasmi?
#ism = input("Ismingiz nima?\n>>>")
#if ism.lower() != 'ali':#Agar ism Aliga teng bo'lmasa..
#   print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
#else:
#    print("Salom, Ali")
#javob = float(input("12x6 nechaga teng?>>>"))
#if javob!=72:
#    print("Javob xato!")
#else:
#    print("Javob to'gri")
#yosh = int(input("Yoshingiz nechada?>>>"))
#if yosh <= 18:
#    print("Xush kelibsiz!")
#else:
#    print("Uzr kirish mumkin emas!")
#login = input("Yangi login tanlng:")
#if len(login)<=5:
#    print("Login 5 ta  harfdan ko'proq bo'lishi shart!")
#yil = int(input("Tug'ilgan yilingizni kiriting:"))
#if 2022-yil<18:
#    print(f"Yoshingiz {2022-yil} da ekan.")
#    print("Kirish mumkin emas!")
#else:
#    print("Xush kelibsiz!")
#yosh = int(input("Yoshingiz nechada?>>>"))
#if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
#x, y = 50, 40
#print("x>y") if x>y else
                               #PYTHON DARSLARI. 11-DARS
                               #MAVZU:IF-ELIF-ELSE. BIR NECHTA
                               #SHARTLARNI TEKSHIRISH
#son = -72
#if son<0:
#    print("Manfiy son")
#else:
#   print("Musbat son")
#   yosh = int(input('Yoshingiz nechada?'))  #YOKI PRINT O'RNIGA>>>>NARX = 4000<<< YOZIB VA OHIRIDA PRINT(F"SIZGA KIRISH {NARX} SO'M") DEYISH MUMKIN!!!
#if yosh<4:
#    print('Sizga kirish bepul.')
#elif yosh<12:
#    print("Sizga kirish 5000 so\'m")
#elif yosh<18:
#    print("sizga kirish 20000 ming so\'m")
#else:
#    print("Sizga kirish 10000 so\'m")
                 #OR OPERATORI
#kun = input("Bugun nima kun?>>")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print('Bugun dam olish kuni')
#else:
#    print('Bugun ish kuni')
                 #AND OPERATORI
#kun = input("Bugun qaysi kun?>>")
#harorat = float(input("Havo harorati qanday?>>"))
#if kun.lower()=='yakshanba' and harorat>=20:
#     print("CHo'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<20:
#     print("Uyda dam olamiz!")      
#kun = input("Bugun nima kun?>>")
#harorat = float(input("Havo harorati qanday?>>"))
#if(kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print("CHo'milgani ketdik")
#elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#    print("Uyda dam olamiz!")    
               #boolean mantiqiy malumotlar turi.
#narh = 15000
#choy = True
#salat = False 

#if choy and salat:
#        narh = narh + 10000
#elif choy or salat:
#      narh = narh + 5000     
#print(f"Jami {narh} so'm")
#narh = 15000
#choy = True   
#salat = False
#non = True   #BU YERDA TRUE O'RNIGA '1' FALSE ORNIGA'0' QO'YSA BO'LADI!!!!
#kompot = False
#tort = True
#if choy:
#     print("Mijoz choy oldi.")
#     narh = narh +3000
#if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
#if non:
#     print("Mijoz non oldi.")
#     narh = narh + 7000
#if kompot:
#     print("Mijoz kompot oldi.")
#if tort:
#     print("Mijoz tort oldi.")
#print(f"Jami {narh} so'm")
                         #IN METODI
#menu = ['osh', 'qozonkabob','shashlik','norin','somsa']
#'manti' in menu #menu da manti bormi
#menu = ['osh','qozonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
#      print('Buyurtma qabul qilindi.')
#else:
#      print('Afsuski bizda bunday ovqat yo\'q')
#menu = ['osh','qozonkabob','shashlik','norin','somsa']
#buyurtmalar = ["osh","somsa","manti","shashlik"]
#for taom in buyurtmalar:
#      if taom in menu:
#          print(f"Menuda {taom}  bor")
#      else:
#          print(f"Kechirasiz, menuda {taom} yo'q")
#else:
#    print("Savatchangiz bo'sh!")













                              