from django.db import models

class TodoApi(models.Model):
    title       = models.CharField(max_length=100)
    memo        = models.TextField(blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    complete    = models.DateTimeField(null=True, blank=True)
    important   = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title