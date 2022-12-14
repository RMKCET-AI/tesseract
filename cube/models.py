from django.db import models
from django.contrib.auth.models import User
import secrets


# Create your models here.
class cubeUser(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user_name = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50, unique=True)
    contact_number = models.TextField(max_length=14)
    address = models.TextField()

    def __str__(self):
        return self.user_name


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.TextField(blank=True, null=True, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.title}'


class APIkey(models.Model):
    name = models.CharField(max_length=100)
    key = models.TextField(default=secrets.token_urlsafe(16))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'APIkeys'
        verbose_name = 'APIkey'
