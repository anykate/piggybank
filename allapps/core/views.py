from allapps.core.models import Currency
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, viewsets

from .models import Category, Currency, Transaction
from .serializers import (
    CurrencySerializer,
    ReadCategorySerializer,
    ReadTransactionSerializer,
    WriteCategorySerializer,
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
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Category.objects.select_related("user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadCategorySerializer
        return WriteCategorySerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class TransactionModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ["description"]
    ordering_fields = ["amount", "created"]
    filterset_fields = ["currency__code"]

    def get_queryset(self):
        return Transaction.objects.select_related("category", "currency", "user").filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadTransactionSerializer
        return WriteTransactionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)
