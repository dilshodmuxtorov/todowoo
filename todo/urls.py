from django.urls import path
from .views import (
    CreateTodo,
    CurrentListTodo,
    CompletedListTodo,
    DeleteUpdateDetailView)

urlpatterns = [
    path('create/',CreateTodo.as_view()),
    path('current/',CurrentListTodo.as_view()),
    path('completed/',CompletedListTodo.as_view()),
    path('todo/<pk>/',DeleteUpdateDetailView.as_view())
]