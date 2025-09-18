from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"

class TodoCreatView(CreateView):
    model = Todo
    fields = ["name", "description", "price"]
    success_url = reverse_lazy("todo_list")