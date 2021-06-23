from django.contrib import admin

from .models import Category, Currency, Transaction


# Register your models here.
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass
