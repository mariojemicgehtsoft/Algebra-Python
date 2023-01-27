def smart_print(data,_max): 
    data_with_dash=""
    count=0
    for slovo in data:
        count=count+1
        if count % 5==0: 
           data_with_dash=  data_with_dash+ slovo
        elif count < _max - 4:  
            data_with_dash=  data_with_dash+ razmak   
        else:
           data_with_dash=  data_with_dash+ slovo
    print( data_with_dash, end="")
 
def add_dash(data,max): 
    data_with_dash=""
    count=0
    for slovo in data:
        count=count+1
        data_with_dash=data_with_dash+slovo
        if count % 4==0 and count!= max: 
           data_with_dash=data_with_dash+"-" 
          
    return data_with_dash

while True:
      razmak=input("Unesi Razmak (*,#):" )
      if razmak== "*" or razmak== "#":
        break


while True:
  
    pin=input("Unesi Pin :" )
    pin=pin.replace('#', '')
    pin=pin.replace('*', '')
    max= len(pin)
    if max< 8:
      print("Minimalni Broj znakova je 8")
    else:  
      novi_pin=add_dash(pin,max) 
      smart_print(novi_pin,len(novi_pin))   
      break 
