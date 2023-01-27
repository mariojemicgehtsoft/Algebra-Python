abeceda=["C","C#","D","D#","E","F","F#","G", "G#", "A", "A#", "H" ]
dur=[1,4,7]
mol=[1,3,7]

def unos_dus_ili_mol():
 
   while True:  
      dus_ili_mol= input("Unesi 1 za Dur, 2 za Mol ili 3 za prekid : " )
      
      if dus_ili_mol=="1":
         break  
      elif dus_ili_mol=="2":  
         break 
      elif dus_ili_mol=="3":  
         break      
      else:
         print(dus_ili_mol, "unos nije valjan")
   return dus_ili_mol 

def unos_pocetni_ton():         
    
   provjera=False 
   while True: 


      pocetni_ton= input("Unesi pocetni ton : " )
      
      for i in range(0,  len(abeceda)):
         if abeceda[i]== pocetni_ton:
            provjera=True

      if provjera== False:
         print(pocetni_ton, "unos nije valjan")
      else:
         break
   return pocetni_ton  


def loop(izbor,pocetni_ton):
   element=abeceda.index(pocetni_ton) #pozicija elementa   
   #Dur 1 4 7
   #Mol 1, 3, 7,  
   for shift in izbor:
            if element+shift > 12:    
               print(abeceda[element+shift-12])
            else:
               print(abeceda[element+shift])

def ispis(dus_ili_mol, pocetni_ton):

   if dus_ili_mol=="1": loop(dur,pocetni_ton) 
   if dus_ili_mol=="2": loop(mol,pocetni_ton) 


while True:
   dus_ili_mol=unos_dus_ili_mol()
   if dus_ili_mol=="3":
      break
   else:
      pocetni_ton= unos_pocetni_ton()
      ispis(dus_ili_mol, pocetni_ton)
