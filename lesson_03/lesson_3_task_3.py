from address import Address
from mailing import Mailing

to_address = Address('11111', 'Санкт-Петербург', 'Манежный переулок', '15-17', '14')
from_address = Address('22222', 'Самара', 'ул. Молодёжная', '2а', '73')

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=999,
    track='RU123456789'
)

print(mailing)
