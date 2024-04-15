from address import Address
from mailing import Mailing

to_address = Address("123456", "Moscow", "Lenin Street", "10", "5A")
from_address = Address("654321", "Saint Petersburg", "Pushkin Street", "20", "10")
mailing = Mailing(to_address, from_address, 100, "ABC123")

print(f"Отправление {mailing.track} из {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment} в {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment}. Стоимость {mailing.cost} рублей.")