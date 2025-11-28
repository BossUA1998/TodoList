from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import Tag


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "deal/index.html")


class TagsListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()