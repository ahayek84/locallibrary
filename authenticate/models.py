from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(User):
    email = User.email
    first_name = User.first_name
    last_name = User.last_name
    fav_colour = models.CharField(max_length=100)

    class Meta:
        ordering = ('first_name', )


