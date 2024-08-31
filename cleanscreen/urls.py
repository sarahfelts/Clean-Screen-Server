from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cleanscreenapi.views import (
    user_views,
    movie_views,
    warning_views,
    tag_views,
    warning_detail_views,
    warning_tag_views,
    saved_movie_views,
)

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'users', user_views.UserView, basename='user')
router.register(r'movies', movie_views.MovieView, basename='movie')
router.register(r'warnings', warning_views.WarningIterableView, basename='warning')
router.register(r'tags', tag_views.TagView, basename='tag')
router.register(r'warning-details', warning_detail_views.WarningDetailView, basename='warningdetail')
router.register(r'warning-tags', warning_tag_views.WarningTagView, basename='warningtag')
router.register(r'saved-movies', saved_movie_views.SavedMovieView, basename='savedmovie')

# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
