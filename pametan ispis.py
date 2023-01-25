#Printa {data} popunjava do _max s space 
def smart_tab(data,_max): 
    #ispisuje {space} od zadnjeg {data} stringa do {_max}
    prored=" " * (_max-len(data))  
    #ispisuje {data} +{prored}        
    print(data+prored, end="")

 
 
stavke =[
  "brand" ,
  "model",  
  "registracija", 
  "godina",
  "cijena"
]

baza={} 

number=0
loop=True 

while loop:
         
      unos={} 
      for i in range(0, len(stavke)):
          unos[i]= input ("Unesi "+ stavke[i] + " : "  )
          if i== len(stavke)-1:
             print("Upisi Exit za Kraj ")
          #prekida unos ako je unesen {Exit}
          if str(unos[i]) ==  "Exit": 
             loop=False
             break
      if loop:
         baza[number] =unos 
         number=number+1      

_max=0
# postavlja {_max} na duzinu najduzek elementa {stavke}
for element in stavke:
    _max=max(_max, len(element))

# postavlja {_max} na duzinu najduzek elementa {baza}
for i in range(len(baza)): 
        for j  in range ( 0, len(stavke)):  
            _max=max(_max, len(baza[i][j]))        
# uvcava {_max} za 1, sprecava sljepljicanje dva unosa iz base            
_max=_max+1


smart_tab("Key", _max)

# ispis {stavki} 
for i in range(0, len(stavke)): 
      smart_tab(stavke[i], _max)
print ("")

line= "."*_max*(len(stavke)+1) 
# ispis {........................................} 
smart_tab(line, _max)
print ("") 

# ispis elemenata {baza} 
for key  in baza.keys():  
    # ispis {baza} key-a
    smart_tab( str(key) , _max)   
    for i in range(0, len(stavke)):  
        # ispis {baza} elemenata
        smart_tab(baza[key][i], _max)
    print()   
