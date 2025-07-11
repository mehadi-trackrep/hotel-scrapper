from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

class SearchResult(models.Model):
    query = models.CharField(max_length=255)  # city name or user query
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.query})"

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=50)
    rating = models.CharField(max_length=50)
    source = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.user.username}"

