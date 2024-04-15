import math

def square(side):
    area = side ** 2
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

# Пример использования функции
side_length = 4.5
area = square(side_length)
print("Площадь квадрата с стороной", side_length, "равна", area)