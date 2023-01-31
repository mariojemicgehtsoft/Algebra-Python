import os
vracanje_stanja=[[1,2,3],[4,5,6],[7,8,9]]
stanje=[[1,2,3],[4,5,6],[7,8,9]]
adresa={1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
pobjednicki_uvjet=[[1,2,3],[4,5,6],[7,8,9], [1,4,7], [2,5,8],   [3,6,7]    ,[3,5,7], [1,5,9]  ]
def provjera():
    winer=0
    for uvjet in pobjednicki_uvjet:
        x1=adresa[uvjet[0]][1]    
        y1=adresa[uvjet[0]][0] 

        x2=adresa[uvjet[1]][1]    
        y2=adresa[uvjet[1]][0]

        x3=adresa[uvjet[2]][1]    
        y3=adresa[uvjet[2]][0]

        if stanje[y1][x1]== stanje[y2][x2] and stanje[y2][x2]== stanje[y3][x3]:
          winer = stanje[y1][x1]
          break 
    return winer  

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
