from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, weight):
        self.name, self.weight = name, weight
        self._energy = 100

    @abstractmethod
    def talk(self): pass

    @abstractmethod
    def move(self): pass

    def feed(self, food):
        self._energy = min(100, self._energy + food)
        print(f">>> {self.name} підкріпився. Енергія тепер: {self._energy}%")

class Tiger(Animal):
    def talk(self): return "Р-р-р-ау! (грізне гарчання)"
    def move(self): return "крадеться крізь високу траву джунглів."

class Elephant(Animal):
    def talk(self): return "Уууу-у! (гучний трубний звук)"
    def move(self): return "повільно йде до водопою."

class ZooGuardian:
    def __init__(self, name):
        self.name = name

    def inspect(self, animal):
        print(f"\n[{self.name}] перевіряє вольєр, де живе {animal.name}:")
        print(f"- Голос: {animal.talk()}")
        print(f"- Поведінка: {animal.name} {animal.move()}")
        
        if animal._energy < 60:
            print(f"- Висновок: {animal.name} виглядає втомленим. Годуємо!")
            animal.feed(35)
        else:
            print(f"- Висновок: {animal.name} у чудовій формі.")

staff = ZooGuardian("Стас")
zoo_list = [Tiger("Шерхан", 220), Elephant("Джамбо", 4500)]

zoo_list[0]._energy = 40 

print("=== РАНКОВИЙ ОБХІД ЗООПАРКУ ===")
for a in zoo_list:
    staff.inspect(a)