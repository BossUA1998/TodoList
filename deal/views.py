from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import TaskForm, TaskSearchForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super().get_context_data(**kwargs)
        _content = self.request.GET.get("content")
        context["search_form"] = TaskSearchForm(
            initial={"content": _content}
        )
        return context

    def get_queryset(self):
        form = TaskSearchForm(self.request.GET)
        self.queryset = Task.objects.all()
        if form.is_valid():
            self.queryset = self.queryset.filter(
                content__icontains=form.cleaned_data["content"]
            )
        return self.queryset


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("deal:tasks")


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.POST.get("complete"):
        task.is_done = True
    elif request.POST.get("undo"):
        task.is_done = False
    task.save()
    return HttpResponseRedirect(reverse("deal:tasks"))


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("deal:tasks")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("deal:tasks")


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
