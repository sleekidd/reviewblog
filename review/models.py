from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='category_pics')

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='cast_pics')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(
    #     upload_to='upload/', blank=True, null=True, default='static/img/aquaman.jpg')
    image = models.ImageField(default='default.jpg', upload_to='movie_pics')
    cast = models.ManyToManyField(Cast)
    category = models.ManyToManyField(Category)
    director = models.ManyToManyField(Director)
    trailer = models.CharField(max_length=50)
    duration = models.CharField(max_length=20)
    release_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
