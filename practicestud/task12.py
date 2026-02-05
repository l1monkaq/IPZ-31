class Car:
    def __init__(self, brand, year, mileage):
        self.brand, self.year, self.mileage = brand, year, mileage

    def drive(self, km):
        self.mileage += km

    def info(self):
        print(self)

    def __str__(self):
        return f"Авто: {self.brand} | Рік: {self.year} | Пробіг: {self.mileage} км"

car1 = Car("Audi", 2022, 12500)
car2 = Car("Hyundai", 2019, 45000)

car1.drive(250)
car1.info()

print(car2)