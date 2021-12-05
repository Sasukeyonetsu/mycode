class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll(self):
        print(f"{self.name} is rolling")

my_dog=Dog('carp',6)

print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll()


