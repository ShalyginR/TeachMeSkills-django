from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 'data_create', 'deadline']
        read_only_fields = ['id', 'data_create', 'user_connection']