import math

print("Equation format: ax^2 + bx + c = 0")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Error: 'a' cannot be zero in a quadratic equation.")
else:
    d = b**2 - 4*a*c
    print(f"Discriminant (D) = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"Two roots: x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = -b / (2*a)
        print(f"One root: x = {x}")
    else:
        print("No real roots (D < 0)")