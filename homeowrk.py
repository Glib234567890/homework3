import random

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def play(self):
        self.happiness += 10
        print(f"{self.name} грається та стає щаслівішим Рівень щастя: {self.happiness}")

    def feed(self):
        self.happiness += 5
        print(f"{self.name} поїв і почувається краще Рівень щастя: {self.happiness}")


class Human:
    def __init__(self, name):
        self.name = name
        self.pet = None

    def adopt_pet(self, pet):
        self.pet = pet
        print(f"{self.name} взяв собі нового улюбленця: {pet.name} ({pet.species})!")

    def play_with_pet(self):
        if self.pet:
            print(f"{self.name} грається з {self.pet.name}.")
            self.pet.play()
        else:
            print(f"{self.name} не має домашньої тварині щюб пограті")

    def feed_pet(self):
        if self.pet:
            print(f"{self.name} годує {self.pet.name}.")
            self.pet.feed()
        else:
            print(f"{self.name} не має кого годувати.")


human = Human("Гліб")
pet = Pet("Рижик", "кіт")

human.adopt_pet(pet)
human.play_with_pet()
human.feed_pet()
