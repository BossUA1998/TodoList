from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ["content", "deadline", "tags"]
    success_url = reverse_lazy("deal:tasks")


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.POST.get("complete"):
        task.is_done = True
    elif request.POST.get("undo"):
        task.is_done = False
    task.save()
    return HttpResponseRedirect(reverse("deal:tasks"))


class TagsListView(generic.ListView):
    model = Tag


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("deal:tags")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("deal:tags")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("deal:tags")
