from django.urls import path
from deal.views import (
    TaskListView,
    TagsListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("tags/", TagsListView.as_view(), name="tags"),
]

app_name = "deal"
