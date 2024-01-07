# WEB143 Assignment 10 Sarah Derr
# Base class of Animal
# 5 derived animal classes
# Zookeeper class
# Create objects based on the animal classes and execute methods


# animal class
# display: prints out name and species
# getters for name and species
# eat, move, and speak default print statements
class Animal:
    def __init__(self, name, species):
        self._name = name
        self._species = species

    def display(self):
        print("My name is ", self._name, "and I am a", self._species)

    def get_species(self):
        return self._species

    def get_name(self):
        return self._name

    def eat(self):
        print(self._name,"is eating")

    def move(self):
        print(self._name, "is moving")

    def speak(self):
        print("The", self._species, "is speaking")


# each inherited class has a name, a species and an overridden "speak" method
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self, "Lucy", "dog")

    def speak(self):
        print("Bark bark!")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self, "Belle", "cat")

    def speak(self):
        print("Meow!")


class Tiger(Animal):
    def __init__(self):
        Animal.__init__(self, "Stripes", "tiger")

    def speak(self):
        print("Roar!")


class Horse(Animal):
    def __init__(self):
        Animal.__init__(self, "Winny", "horse")

    def speak(self):
        print("Neigh!")


class Bird(Animal):
    def __init__(self):
        Animal.__init__(self, "Paulo", "bird")

    def speak(self):
        print("Chirp chirp!")


# zookeeper class feeds the animals
# if animal is a bird, zookeeper will feed it bird feed
# calls the animal's eat class to show that it's eating after being fed
class Zookeeper():
    def __init__(self, animal):
        self._animal = animal

    def feed(self):
        if self._animal.get_species() == "bird":
            print("I am holding out my hand with bird feed")
        print("I am feeding the", self._animal.get_species())
        print("Have a good meal!")
        self._animal.eat()


# creating objects for each animal
# I used random methods for each animal, so it wasn't just the same thing being repeated
# calling two different animals to be fed by zookeeper
def main():
    dog = Dog()
    dog.display()
    dog.speak()
    print()

    cat = Cat()
    cat.display()
    cat.move()
    print()

    tiger = Tiger()
    tiger.display()
    tiger.speak()
    tiger.move()
    print()

    horse = Horse()
    horse.display()
    horse.speak()
    horse.eat()
    print()

    bird = Bird()
    bird.display()
    bird.move()
    print()

    Zookeeper(bird).feed()
    print()
    Zookeeper(tiger).feed()


if __name__ == "__main__":
    main()
