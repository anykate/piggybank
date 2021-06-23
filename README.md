Currency.objects.bulk_create([
	Currency(code="USD", name="United States Dollar"),
	Currency(code="INR", name="Indian Rupee"),
	Currency(code="AUD", name="Australian Dollar"),
	Currency(code="EUR", name="United Kingdom Pound")
])


import random
from decimal import Decimal

currencies = list(Currency.objects.all())
categories = list(Category.objects.all())
txs = []

for i in range(1000):
	tx = Transaction(amount=random.randrange(Decimal(1), Decimal(1000)), currency=random.choice(currencies), category=random.choice(categories))
	txs.append(tx)

Transaction.objects.bulk_create(txs)
