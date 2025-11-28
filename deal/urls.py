from django.urls import path
from deal.views import (
    index,
)

urlpatterns = [
    path("", index, name="index"),
]

app_name = "deal"
