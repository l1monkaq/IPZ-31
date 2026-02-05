import math

def get_rect_area(w, h): return w * h
def get_circ_area(r): return math.pi * (r ** 2)

print(get_rect_area(6, 7))
print(f"{get_circ_area(10):.2f}")