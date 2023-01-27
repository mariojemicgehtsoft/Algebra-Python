Abeceda=["C","C#","D","D#","E","F","F#","G", "G#", "A", "A#", "H" ]
Dur=[1,4,7]
Mol=[1,3,7]

Loop=True
while Loop: 


    Izbor1= input("Unesi 1 za Dur ili 2 za Mol : " )
    
    if Izbor1=="1":
        break  
    elif Izbor1=="2":  
        break     
    else:
        print(Izbor1, "unos nije valjan")

Loop=True
Provjera=False 
while Loop: 


    Izbor2= input("Unesi pocetni ton : " )
    
    for i in range(0,  len(Abeceda)):
      if Abeceda[i]== Izbor2:
         Provjera=True

    if Provjera== False:
       print(Izbor2, "unos nije valjan")
    else:
       break

#Izbor2 = Izbor2.apper("")

Element=Abeceda.index(Izbor2) #pozicija elementa 
 
#Dur 1 4 7
#Mol 1, 3, 7,

if Izbor1=="1":   
   for Shift in Dur:    

       if Element+Shift > 12:
          print(Abeceda[Element+Shift-12])        
       else:
           print(Abeceda[Element+Shift])
if Izbor1=="2":   
   for Shift in Mol:
        if Element+Shift > 12:    
           print(Abeceda[Element+Shift-12])
        else:
           print(Abeceda[Element+Shift])
