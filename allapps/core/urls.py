from django.urls import path
from rest_framework import routers

from . import views

app_name = "core"

router = routers.SimpleRouter()
router.register("categories", views.CategoryModelViewSet, basename="category")

urlpatterns = [
    path("", views.index, name="index"),
    path("currency/", views.CurrencyListAPIView.as_view(), name="currency"),
] + router.urls
