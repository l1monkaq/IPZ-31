import math

class Rectangle:
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

class Circle:
    def __init__(self, r): self.r = r
    def area(self): return math.pi * (self.r ** 2)

shapes = [Rectangle(6, 7), Circle(10)]
for s in shapes:
    print(f"{s.__class__.__name__}: {s.area():.2f}")
