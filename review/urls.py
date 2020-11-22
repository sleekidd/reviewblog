from django.urls import path
from . import views
from .views import MovieListView, MovieDetailView

urlpatterns = [
    path('', views.index, name='review-index'),
    path('movies', MovieListView.as_view(), name='review-all'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='review-detail'),
]
