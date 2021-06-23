from django.urls import path
from rest_framework import routers

from . import views

app_name = "core"

router = routers.SimpleRouter()
router.register("categories", views.CategoryModelViewSet, basename="category")
router.register("transactions", views.TransactionModelViewSet, basename="transaction")

urlpatterns = [
    path("", views.index, name="index"),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
] + router.urls
