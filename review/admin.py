from django.contrib import admin
from .models import Category, Cast, Director, Movie

# Register your models here.
admin.site.register(Category)
admin.site.register(Cast)
admin.site.register(Director)
admin.site.register(Movie)
