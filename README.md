admin:
6f62890ab7fbf9bf5925dbf0bddcd96ff1b87cb2
8 - Shoot - 1
5 - Blog - 1
4 - Travel - 1
3 - Pets - 1



aniket:
5c1abfae5b9f40e1e82f8c33f334cac845a8c825
7 - Recipes - 2
6 - Vlog - 2
2 - Medical - 2
1 - Home - 2





Currency.objects.bulk_create([
	Currency(code="USD", name="United States Dollar"),
	Currency(code="INR", name="Indian Rupee"),
	Currency(code="AUD", name="Australian Dollar"),
	Currency(code="EUR", name="United Kingdom Pound")
])


User 1:
import random
from decimal import Decimal

currencies = list(Currency.objects.all())
categories = list(Category.objects.filter(user_id=1))
users=list(User.objects.filter(id=1))

txs = []

for i in range(1000):
	tx = Transaction(
		amount=random.randrange(Decimal(1), Decimal(1000)),
		currency=random.choice(currencies),
		category=random.choice(categories),
		user=random.choice(users)
	)
	txs.append(tx)

Transaction.objects.bulk_create(txs)

User 2:
import random
from decimal import Decimal

currencies = list(Currency.objects.all())
categories = list(Category.objects.filter(user_id=2))
users=list(User.objects.filter(id=2))

txs = []

for i in range(1000):
	tx = Transaction(
		amount=random.randrange(Decimal(1), Decimal(1000)),
		currency=random.choice(currencies),
		category=random.choice(categories),
		user=random.choice(users)
	)
	txs.append(tx)

Transaction.objects.bulk_create(txs)
