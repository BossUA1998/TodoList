from django.urls import path
from deal.views import (
    TaskListView,
    TagsListView,

    TaskCreateView,
    TagsUpdateView,
    TagsCreateView,
    TagsDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagsListView.as_view(), name="tags"),

    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "deal"
