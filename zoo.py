class Animal:
    def __init__(self,name,age,health_level,hapiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.hapiness_level = hapiness_level
        self.type_of_animal = None
    def feed_animal(self):
        self.health_level += 10
        self.hapiness_level += 10
        return self
    def display_info(self):
        print(f"Animal: {self.type_of_animal} - Name: {self.name} - Age: {self.age} - health_level: {self.health_level} - hapiness_level: {self.hapiness_level}")
        

class Lion(Animal):
    def __init__(self,name,age=1,health_level=0,hapiness_level=0):
        super().__init__(name,age,health_level,hapiness_level)
        self.type_of_animal = "Lion"

class Tiger(Animal):
    def __init__(self,name,age=1,health_level=0,hapiness_level=0):
        super().__init__(name,age,health_level,hapiness_level)
        self.type_of_animal = "Tiger"

class Bear(Animal):
    def __init__(self,name,age=1,health_level=0,hapiness_level=0):
        super().__init__(name,age,health_level,hapiness_level)
        self.type_of_animal = "Bear"

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_animal(self, *Animals):
        for newAnimal in Animals:
            self.animals.append(newAnimal)
        return self
    def print_all_info(self):
        print("\n")
        print("-"*35, self.name, "-"*35)
        for animal in self.animals:
            animal.display_info()
        print("\n")
        return self

# I) Create the instance of a Zoo
my_zoo = Zoo("Super Zoo")

# II) Create instances for animals of my Zoo

# Lions - We define them with specific name, age, healthe_level and hapiness_level
simba = Lion("Simba",age=2,health_level=10,hapiness_level=30)
scar = Lion("Scar",age=10,health_level=15,hapiness_level=0)
nala = Lion("Nala",age=1,health_level=10,hapiness_level=20)
mufasa = Lion("Mufasa",age=12,health_level=15,hapiness_level=15)

# Tigers - We define them with specific name and age. Healthe_level and hapiness_level use their default levels, which are 0 and 0 respectivetly
rajah = Tiger("Rajah",age=5)
shere_khan = Tiger("Shere Khan",age=15)

# Bears - We define them with specific name. Age, healthe_level and hapiness_level use their default levels, which are 1, 0 and 0 respectivetly
baloo = Bear("Baloo")
yoghi = Bear("Yoghi")

# III) We add the animals to the Zoo
my_zoo.add_animal(simba,scar,nala,mufasa,rajah,shere_khan,baloo,yoghi)

# IV) We print all our animals to check their information
my_zoo.print_all_info()

# V) We feed bears and the check again their information. After feeding bears their health_level and hapiness_level should increase in 10, each one

baloo.feed_animal()
yoghi.feed_animal()
print("Baloo and Yoghi are fed!! They look now healthier and happier than they used to be!!!" )

my_zoo.print_all_info()
