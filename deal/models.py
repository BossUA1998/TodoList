from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=120)

class Task(models.Model):
    content = models.CharField(max_length=512)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    boolean_field = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
