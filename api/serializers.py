from rest_framework import serializers
from .models import TodoApi


class ApiSerializers(serializers.ModelSerializer):
    class Meta:
        model   = TodoApi
        fields  = ['id', 'title', 'memo', 'created', 'complete', 'important']

