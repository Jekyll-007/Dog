class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name,'says woof')

my_dog=Dog('Rotweiller',7)
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())