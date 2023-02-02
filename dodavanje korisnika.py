import os
os.system('cls')

baza_korisnika = {
  "admin":["admin", "Admin"]}
 


def korisnicko_ime(): 
    user_name=0
    user_name= input("Unesi Korisnicko Ime :")
    if  baza_korisnika.get(user_name, "nepostojeci")=="nepostojeci":
        print("Korisnik ne postoji")
        user_name=0
  
    return user_name

def lozinka(user_name): 
    password= input("Unesi lozinku :")
    os.system('cls') 
    if baza_korisnika[user_name][0]!=password:
       print("Netocna Lozinka") 
       password=0 
    return password
def unos_korisnika():
    user_name=0
    while True:
          user_name= input("Unesi Korisnicko Ime :") 
          if baza_korisnika.get(user_name, "nepostojeci")=="nepostojeci":
             break
    return user_name
def unos_lozinka():
    lozinka=0
    while True:
          lozinka= input("Unesi Lozinku :") 
          if len(lozinka)>7:
             break
          else:             
             print("Lozinka moza imati najmanje 8 znakova")   

    return lozinka    
def unos_ovlasti():    
    ovlast=0
    while True:
          ovlast= int(input("Unesi 1 za Administratora 2 za Korsinika :"))
          if  ovlast== 1:
            break
          elif  ovlast== 2: 
            break   

    return ovlast    
def dodavanje_korisnika(): 
    user_name=0
    passwod=0
    ovlasti=0
    while True:
        
        user_name=unos_korisnika() 
        passwod=unos_lozinka() 
        ovlasti=unos_ovlasti()         
        if user_name!=0 and passwod!= 0 and ovlasti!= 0:
           baza_korisnika.update({user_name: [passwod, ovlasti]}) 
           break
        
     
def brisanje_korisnika(): 
     while True:
          user_name= input("Unesi Korisnicko Ime :") 
          print("Exit za Izlaz :") 
          if user_name=="Exit":
            break
          elif baza_korisnika.get(user_name, "nepostojeci")=="nepostojeci": 
             print("Nepostojeci Korisnika")
          else:
              baza_korisnika.pop(user_name, "")    
              print("Korisnik je Obrisan")

def administracija(): 
    izbor=int(input("1: Dodavanje 2: Brisanje 3: Izlaz"))
    if izbor== 1:
       dodavanje_korisnika() 
    elif izbor== 2:
       brisanje_korisnika()
    else:
        pass
 

while(True): 
      user_name=korisnicko_ime()
      if user_name!=0:
         password=lozinka(user_name)  

      if user_name != 0 and password != 0 :
         if baza_korisnika[user_name][1]=="Admin":
            print("Dobrodosli u Administratorski Izbornik")
            administracija()
         if baza_korisnika[user_name][1]!="Admin":
            print("Dobrodosli u Korisnicki Izbornik")
