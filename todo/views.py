from django.shortcuts import render
from rest_framework import generics
from .models import TodoModel
from .serializers import TodoSerializer,TodoDetailSerializer
from rest_framework.response import Response
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerPermission

class CreateTodo(generics.CreateAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

class CurrentListTodo(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user = self.request.user
        return TodoModel.objects.filter(completed = False,user=user)
    
class CompletedListTodo(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        user = self.request.user
        return TodoModel.objects.filter(completed = True, user=user)
    
class DeleteUpdateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoDetailSerializer
    permission_classes = (IsOwnerPermission,)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.completed = True
        instance.completed_time = datetime.now()
        
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    
    



