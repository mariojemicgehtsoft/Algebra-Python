class Person:
 #__init__(), which is always executed when the class is being initiated.  
 #Use the __init__() function to assign values to object properties,
  def __init__(self, name, age):
    self.name = name
    self.age = age

    #The __str__() function controls what should be returned when the class object is represented as a string.
    #If the __str__() function is not set, the string representation of the object is returned:
  def __str__(self):
    return f"{self.name}({self.age})"

  #Objects can also contain methods. Methods in objects are functions that belong to the object.
  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
  #It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
  def myfunc(self):
    print("Hello my name is " + self.name)      

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#koristi __str__
print(p1) #John(36)  

#koristi myfunc
p1.myfunc() #Hello my name is John

#Set the age of p1 to 40:
p1.age = 40

#Delete the age property from the p1 object:
del p1.age

#Delete the p1 object:
del p1
