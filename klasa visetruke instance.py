class MyClass:
    def __init__(self, name, count=0):
        self.name = name
        self.count=count
        self.pretty_print_name()

    def __str__(self):
        return f"{self.name}({self.count})"    

    def pretty_print_name(self):
        print("This object's name is {}.".format(self.name))
  

my_objects = {}
count=0
for i in range(1,11):
    name = 'obj_{}'.format(i)
    my_objects[i]=MyClass(name,i)

print(my_objects[4].count) 
