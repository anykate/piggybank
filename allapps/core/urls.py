from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = "core"

router = routers.SimpleRouter()
router.register("categories", views.CategoryModelViewSet, basename="category")
router.register("transactions", views.TransactionModelViewSet, basename="transaction")

urlpatterns = [
    path("login/", obtain_auth_token, name='obtain_auth_token'),
    path("", views.index, name="index"),
    path("currencies/", views.CurrencyListAPIView.as_view(), name="currencies"),
] + router.urls
