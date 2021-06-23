from allapps.core.models import Currency
from django.shortcuts import render
from rest_framework import generics, viewsets

from .models import Category, Currency, Transaction
from .serializers import CategorySerializer, CurrencySerializer


# Create your views here.
def index(request):
    return render(request, "core/index.html", {})


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
