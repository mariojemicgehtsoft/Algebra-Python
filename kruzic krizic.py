import os
vracanje_stanja=[[1,2,3],[4,5,6],[7,8,9]]
stanje=[[1,2,3],[4,5,6],[7,8,9]]
adresa={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
def provjera():
    
    if stanje[0][0]== stanje[0][1] and stanje[0][1]== stanje[0][2]:
       return stanje[0][0]
    elif stanje[1][0]== stanje[1][1] and stanje[1][1]== stanje[1][2]:
       return stanje[1][0]   
    elif stanje[2][0]== stanje[2][1] and stanje[2][1]== stanje[2][2]:
       return stanje[2][0] 

    elif stanje[0][0]== stanje[1][0] and stanje[1][0]== stanje[2][0]:
       return stanje[0][0]    
    elif stanje[0][1]== stanje[1][1] and stanje[1][1]== stanje[2][1]:
       return stanje[0][1]  
    elif stanje[0][2]== stanje[1][2] and stanje[1][2]== stanje[2][2]:
       return stanje[0][2] 

    elif stanje[0][0]== stanje[1][1] and stanje[1][1]== stanje[2][2]:
       return stanje[0][0]    
    elif stanje[0][2]== stanje[1][1] and stanje[1][1]== stanje[2][0]:
       return stanje[0][2]                  
    else:
       return 0  

def ispis():

    print ("-------")
    for red in stanje:
        n=0        
        for stupac in red:
            n=n+1
            if  n==1 or n== 4 or n== 7:
                 print(  "|" +str(stupac) + "|", end="") 
            elif n==3: 
                  print(str(stupac) + "|" ) 
            else:  
                   print(str(stupac) + "|" , end="") 
        print ("-------")             
               
os.system('cls')

tko="x"
while (True): 
      os.system('cls')
      ispis()         
      izbor= int(input(tko +" Izaberi Index : ")) 
      #y=adresa[izbor][0] x=adresa[izbor][1] 
      #stanje[       y       ][        x       ]=tko 
      stanje[adresa[izbor][0]][adresa[izbor][1]]=tko
      if tko=="x":
         tko="o"
      elif tko=="o":
         tko="x"      
      pobjednik=provjera()
      if pobjednik != 0:
         os.system('cls')
         ispis()
         print(str(pobjednik) + " pobjeduje")
         nova_igra=  input( " Za novu igru upisi New : ")
         if nova_igra != "New": 
            break
         else:
            stanje=vracanje_stanja
