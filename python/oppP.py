class Animal:
    def __init__(self, name, phrase):
        self.name = name
        self.phrase = phrase


animal = Animal("bob", "hi")

print(animal.phrase)