import os
os.system('cls')

class  Televizor:
     def __init__(self, je_ukljucen):
          self.je_ukljucen=je_ukljucen

     def ukljuci(self):
         self.je_ukljucen=True

     def iskljuci(self):
         self.je_ukljucen=False

TV_u_dnevnom_boravku=Televizor(True)

TV_u_dnevnom_boravku.ukljuci()

if TV_u_dnevnom_boravku.je_ukljucen== True:
   print("ukljucen")
else:
   print("iskljucen")

TV_u_dnevnom_boravku.iskljuci() 
if TV_u_dnevnom_boravku.je_ukljucen == True:
   print("ukljucen")
else:
   print("iskljucen")
 
