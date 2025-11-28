from django.urls import path
from deal.views import (
    TaskListView,
    TaskCreateView,
    update_task,
    TaskUpdateView,
    TaskDeleteView,

    TagsListView,
    TagsUpdateView,
    TagsCreateView,
    TagsDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="tasks"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/update-complete/", update_task, name="task-update-complete"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "deal"
