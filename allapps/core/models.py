from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # USD
    name = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.code


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name="transactions")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="transactions"
    )

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return str(self.amount)
