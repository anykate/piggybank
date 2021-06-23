from django.contrib.auth import get_user_model
from django.db.models import query
from rest_framework import serializers

from .models import Category, Currency, Transaction


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]
        read_only_fields = fields


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["id", "code", "name"]


class WriteCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ["name", "user"]


class ReadCategorySerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", queryset=get_user_model().objects.all())

    class Meta:
        model = Category
        fields = ["id", "name", "user"]
        read_only_fields = fields


class WriteTransactionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(slug_field="code", queryset=Currency.objects.all())
    category = serializers.SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ["amount", "currency", "created", "updated", "description", "category", "user"]


class ReadTransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()
    category = ReadCategorySerializer()
    user = ReadUserSerializer()

    class Meta:
        model = Transaction
        fields = ["id", "amount", "currency", "created", "updated", "description", "category", "user"]
        read_only_fields = fields
