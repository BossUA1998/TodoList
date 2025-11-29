from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import TaskForm, TaskSearchForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    def get_context_data(self, *, object_list=..., **kwargs):
        context = super().get_context_data(**kwargs)
        _content = self.request.GET.get("content")
        context["search_form"] = TaskSearchForm(initial={"content": _content})
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


class TaskCompleteView(generic.UpdateView):
    model = Task
    fields = ["is_done"]
    success_url = reverse_lazy("deal:tasks")

    def form_valid(self, form):
        if self.request.POST.get("complete"):
            form.instance.is_done = True
        elif self.request.POST.get("undo"):
            form.instance.is_done = False
        return super().form_valid(form)


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
