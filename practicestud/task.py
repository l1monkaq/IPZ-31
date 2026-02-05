a = 12
b = 3.7

text = "Hello World"
num = int("5")

plus = a + b
minus = a - b
mnozh = a * b
dil = a / b

text_plus = text + " i'm python"
text_mul = (text + " ") * 3

print("додавання a + b:", plus)
print("віднімання a - b:", minus)
print("множення a * b:", mnozh)
print("ділення a / b:", dil)

print("дублювання рядка:", text_mul)
print("з'єднання рядка:", text_plus)

inp = input("введіть число ")

print("ваше число", inp, "тип данних:", type(inp))