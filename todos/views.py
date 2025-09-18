from django.shortcuts import render

from django.views.generic import ListView
from .models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"