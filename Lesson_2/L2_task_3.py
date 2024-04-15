def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False

# Пример использования функции
year = 2020
if is_year_leap(year):
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")