from django.urls import path
from core.views import checkout, success
urlpatterns = [
    path('', checkout, name="checkout"),
    path('success', success, name="success")
]
