class Dog:
    def sound(self): return "Пес каже: Гав-гав!"

class Cat:
    def sound(self): return "Кіт каже: Мяу-мяу!"

class Cow:
    def sound(self): return "Коровка каже: Му-у-у!"

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.sound())