from rest_framework.serializers import ModelSerializer
from .models import TodoModel

class TodoSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id','title', 'memo','important','completed','completed_time']

class TodoDetailSerializer(ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id','title', 'memo','important','completed','completed_time']