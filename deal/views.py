from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task


class TagsListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()