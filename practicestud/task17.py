class Car:
    def __init__(self, brand, year, mileage):
        self.brand, self.year, self._m = brand, year, mileage

    @property
    def mileage(self): return self._m

    @mileage.setter
    def mileage(self, v):
        if v < self._m: raise ValueError("Mileage rollback denied")
        self._m = v

car = Car("Mazda", 2024, 15000)
try:
    car.mileage = 20000
    print(f"{car.brand}: {car.mileage} km")
    car.mileage = 5000
except ValueError as e:
    print(f"Error: {e}")