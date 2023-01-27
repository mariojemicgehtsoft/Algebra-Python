import random
izbor= int(random.randint(1,100))   
broj_pokusaja=0
while True: 

      odgovor=int(input("Unesi Broj od 1 do 100 :"))
      broj_pokusaja=broj_pokusaja+1

      if odgovor == izbor :
         print("pogodeno iz " + str(broj_pokusaja) + ". pokusaja" )
         break

      elif odgovor > izbor :  
            print("zamisljeni broj je manji" ) 
      elif odgovor < izbor :  
            print("zamisljeni broj je veci" ) 
