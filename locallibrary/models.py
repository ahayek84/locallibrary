from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Country(models.Model):
    name = models.CharField(max_length=10)