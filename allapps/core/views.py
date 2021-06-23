from allapps.core.models import Currency
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets

from .models import Category, Currency, Transaction
from .serializers import (
    CategorySerializer,
    CurrencySerializer,
    ReadTransactionSerializer,
    WriteTransactionSerializer,
)


# Create your views here.
def index(request):
    return render(request, "core/index.html", {})


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = None


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None


class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related("category", "currency")
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["description"]
    ordering_fields = ["amount", "created"]
    filterset_fields = ["currency__code"]

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer
