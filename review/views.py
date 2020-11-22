from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Category, Movie, Cast, Director
from django.utils import timezone

# Create your views here.

# Movie.objects.filter(
#     release_date__lte=timezone.now()).order_by('release_date')[:3]


def index(request):
    context = {
        'movies': Movie.objects.filter(release_date__lte=timezone.now()).order_by('release_date')[:6],
        'title': 'Movie App',
        'categories': Category.objects.all()[:8]
    }
    return render(request, 'review/index.html', context)


class MovieListView(ListView):
    model = Movie
    template_name = 'review/movies.html'
    context_object_name = 'movies'
    ordering = ['-release_date']


class MovieDetailView(DetailView):
    model = Movie
    # template_name = 'review/movies.html'
    # context_object_name = 'movies'
    # ordering = ['-release_date']
