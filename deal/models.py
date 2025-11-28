from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.CharField(max_length=512)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    boolean_field = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
