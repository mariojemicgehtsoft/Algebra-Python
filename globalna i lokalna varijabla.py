import os
os.system('cls')

txt="Globalna"


def moja_fukcija():
    global txt
    
    print(txt) #printa globalnu 

    #Kako definirati txt kao lokalnu varijablu, tako da line 13 ne promjeni globalnu varijablu
    txt="Lokalna"
    print(txt) #printa Lokalna 

 
moja_fukcija() 

print(txt) #printa Lokalna
