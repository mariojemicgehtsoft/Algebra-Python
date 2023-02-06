import os
import time
from datetime import datetime
os.system('cls')

 

baza_korisnika = {}
baza_transkacija = {} 

def otvaranje_racuna(): 
         naziv=input("Naziv Tvrtke :")
         ulica_i_broj=input("Ulica i broj :")     
         postanski_broj=input("Postanski broj :")       
         mjesto=input("Sjediste :") 
         while (True):  
            oib=int(input("OIB :")) 
            if len(str(oib)) == 8 : 
               break
         odgovorna_osoba=input("Ime i prezime odgovorne osobe :") 

      
 
         currentYear = datetime.now().year
         currentMonth = datetime.now().month 


         novi_broj=len(baza_korisnika)+1
         baza_korisnika.update({novi_broj: [naziv, ulica_i_broj,postanski_broj, mjesto, oib,odgovorna_osoba, currentMonth, currentYear ]})
         baza_transkacija.update({novi_broj: []}) 
 
def prikaz_stanja():
    broj_racuna=provjera_broj_racuna()
    if broj_racuna!=0:
       baza= baza_transkacija[broj_racuna]
       stanje=0
       for unos in baza:
           stanje=stanje+int(unos[0])

       txt = "BA-" + str(baza_korisnika[broj_racuna][6]) + "-" + str(baza_korisnika[broj_racuna][7] )+  "-" + str(broj_racuna)
       print(f"Stanje racuna {txt} : {stanje}")
 
  
 

def provjera_broj_racuna():  
    
    while(True):
        
        broj_racuna=int(input("Unesi broj racuna :"))
        if  baza_korisnika.get(int(broj_racuna), "nepostojeci")=="nepostojeci":  
            print("Nepostojeci racun")
            broj_racuna=0
        else:    
            break

    return broj_racuna      
       

def prikaz_prometa():
    broj_racuna=provjera_broj_racuna()
    if broj_racuna!=0:
       baza= baza_transkacija[broj_racuna] 

       txt = "BA-" + str(baza_korisnika[broj_racuna][6]) + "-" + str(baza_korisnika[broj_racuna][7] )+  "-" + str(broj_racuna)
       print(f"Prometi po racunu {txt}")
       for unos in baza:
           print(f" {unos[1]} : {unos[0]}")
      


def uplata_novca():
    broj_racuna=provjera_broj_racuna()

    while(True):
        if broj_racuna!=0:
           uplata= int(input("Koliko zelite uplatiti : "))
 

           if uplata > 0:
                baza=baza_transkacija.get(int(broj_racuna))   
                baza.append([uplata, datetime.now()])  
                #baza.append(uplata)      
                baza_transkacija.update({broj_racuna: baza}) 
                break
           else:
                print("Unesite pozitivni broj") 


def podizanje_novca():
    broj_racuna=provjera_broj_racuna()
    while(True):
         if broj_racuna!=0:
            isplata= int(input("Koliko zelite podignuti : "))
            if isplata > 0:
        
               baza=baza_transkacija.get(int(broj_racuna))
               baza.append([-1*isplata, datetime.now()])     
              #baza.append(-1*isplata)      
               baza_transkacija.update({broj_racuna: baza}) 
               break
            else:
             print("Unesite pozitivni broj") 
 
os.system('cls')  

while(True):    
    #os.system('cls')       
    print("1. Kreiranje racuna")
    print("2. Prikaz stanja racuna")
    print("3. Prikaz prometa na racuna")
    print("4. Uplata novca s racuna")
    print("5. Podizanje novca s racuna")
    print("6. Izlaz") 
    izbor=input("Vas Izbor :" )  
 

    if izbor== "1":
        otvaranje_racuna()
    elif izbor== "2": 
        prikaz_stanja()
    elif izbor== "3":
        prikaz_prometa()
    elif izbor== "4":  
        uplata_novca()         
    elif izbor== "5":  
        podizanje_novca()  
    elif izbor== "6":
       break
    else:
        print("Nepodrzani unos")
             
