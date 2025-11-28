from django.urls import path
from deal.views import (
    index,
    TagsListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagsListView.as_view(), name="tags"),
]

app_name = "deal"
