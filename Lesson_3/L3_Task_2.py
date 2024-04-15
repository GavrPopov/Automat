from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 12", "+79123456789")
phone2 = Smartphone("Samsung", "Galaxy S21", "+79234567890")
phone3 = Smartphone("Google", "Pixel 5", "+79345678901")
phone4 = Smartphone("OnePlus", "8T", "+79456789012")
phone5 = Smartphone("Xiaomi", "Mi 11", "+79567890123")

catalog.extend([phone1, phone2, phone3, phone4, phone5])

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")