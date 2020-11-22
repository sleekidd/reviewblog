from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Category, Movie, Cast, Director, Review
from django.utils import timezone
from .forms import ReviewForm

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

    def get_queryset(self):
        """Filter by price if it is provided in GET parameters"""
        queryset = super(MovieListView, self).get_queryset()
        if 'category' in self.request.GET:
            queryset = queryset.filter(category=self.request.GET['category'])
        return queryset


class MovieDetailView(DetailView):
    model = Movie
    # template_name = 'review/movies.html'
    # context_object_name = 'movies'
    # ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = Review.objects.filter(
            movie=self.get_object()).order_by('-created_date')
        data['comments'] = comments_connected
        if self.request.user.is_authenticated:
            data['comment_form'] = ReviewForm(instance=self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = Review(content=request.POST.get(
            'content'), author=self.request.user, movie=self.get_object())

        new_comment.save()
        return self.get(self, request, *args, **kwargs)
