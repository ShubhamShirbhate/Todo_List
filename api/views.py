from django.shortcuts import render
from .serializers import ApiSerializers
from rest_framework import generics
from .models import TodoApi
from rest_framework.exceptions import ValidationError

class Apilist(generics.ListCreateAPIView):
    queryset            = TodoApi.objects.all()
    serializer_class    =  ApiSerializers


class RetriveDestApilist(generics.RetrieveDestroyAPIView):
    queryset            = TodoApi.objects.all()
    serializer_class    =  ApiSerializers

    def delete(self, request, *args, **kwargs):
        post = TodoApi.objects.filter(pk=kwargs['pk'])
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('this is no longer')

    def update(self, request, *args, **kwargs):
        post = TodoApi.objects.filter(pk=kwargs['pk'])
        if post.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError('this is no longer')




