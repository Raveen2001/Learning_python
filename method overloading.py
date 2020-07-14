class Animal:
    def __init__(self):
        print("Animal constructor!!")

    def eat(self):
        print("Animal is eating")


class Mammal(Animal):
    def __init__(self):  # which constructor declared last is taken as a constructor after inheritence
        super().__init__()
        print("Mammal constructor!!")


dog = Mammal()
