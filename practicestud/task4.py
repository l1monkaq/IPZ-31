import math

v0 = float(input("Введіть швидкість (м/с): "))
angle = float(input("Введіть кут (градуси): "))

g = 9.81
rad = math.radians(angle)
v0y = v0 * math.sin(rad)
v0x = v0 * math.cos(rad)

total_time = 2 * v0y / g
max_height = (v0y**2) / (2 * g)
distance = v0x * total_time

print("--- Результати ---")
print(f"Дальність: {distance:.2f} м")
print(f"Макс. висота: {max_height:.2f} м")
print(f"Час польоту: {total_time:.2f} с")

print("--- Висота по секундах ---")
for t in range(int(total_time) + 1):
    h = v0y * t - (g * t**2) / 2
    print(f"Секунда {t}: {h:.2f} м")