import os
os.system('cls')
n = 3

def factorial(fact):
    if fact == 1:
       return 1
    else: 
       return fact*factorial(fact-1) 

      
print(factorial(n))
 
