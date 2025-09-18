from django.urls import path
from .views import TodoListView,TodoCreatView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreatView.as_view(), name="todo_create")

]