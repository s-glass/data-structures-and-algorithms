from data_structures.queue import Queue

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Cat(Animal):
    def __init__(self, name=""):
        super().__init__('cat', name)

class Dog(Animal):
    def __init__(self, name=""):
        super().__init__('dog', name)

class AnimalShelter:
    def __init__(self):
        self.cat_queue = Queue()
        self.dog_queue = Queue()

    def enqueue(self, animal):
        if animal.species == 'cat':
            self.cat_queue.enqueue(animal)
        elif animal.species == 'dog':
            self.dog_queue.enqueue(animal)
        else:
            return "Please choose either a cat or dog."

    def dequeue(self, pref):
        if pref == 'cat':
            return self.cat_queue.dequeue()
        elif pref == 'dog':
            return self.dog_queue.dequeue()
        else:
            return None
