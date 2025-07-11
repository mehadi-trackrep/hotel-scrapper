from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"