# Reference Code
# Simple object-oriented programming example with a basic Animal class.

class Animal:
    def __init__(self, name, phrase):
        self.name = name
        self.phrase = phrase


animal = Animal("bob", "hi")

print(animal.phrase)