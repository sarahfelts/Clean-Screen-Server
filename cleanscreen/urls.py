from django.contrib import admin
from django.urls import path
from cleanscreenapi.views import (
    user_views, movie_views, warning_views, tag_views, 
    warning_detail_views, warning_tag_views, saved_movie_views
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User URLs
    path('users/create/', user_views.create_user, name='create_user'),
    path('users/<int:user_id>/', user_views.read_user, name='user_detail'),
    path('users/<int:user_id>/update/', user_views.update_user, name='update_user'),
    
    # Movie URLs
    path('movies/create/', movie_views.create_movie, name='create_movie'),
    path('movies/', movie_views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_id>/update/', movie_views.update_movie, name='update_movie'),
    path('movies/<int:movie_id>/delete/', movie_views.delete_movie, name='delete_movie'),
    
    # Warning URLs
    path('warnings/create/', warning_views.create_warning, name='create_warning'),
    path('warnings/', warning_views.warning_list, name='warning_list'),
    path('warnings/<int:warning_id>/', warning_views.warning_detail, name='warning_detail'),
    path('warnings/<int:warning_id>/update/', warning_views.update_warning, name='update_warning'),
    path('warnings/<int:warning_id>/delete/', warning_views.delete_warning, name='delete_warning'),
    
    # Tag URLs
    path('tags/create/', tag_views.create_tag, name='create_tag'),
    path('tags/', tag_views.tag_list, name='tag_list'),
    
    # WarningDetail URLs
    path('warning_details/create/', warning_detail_views.create_warning_detail, name='create_warning_detail'),
    path('warning_details/', warning_detail_views.warning_detail_list, name='warning_detail_list'),
    path('warning_details/<int:detail_id>/update/', warning_detail_views.update_warning_detail, name='update_warning_detail'),
    
    # WarningTag URLs
    path('warning_tags/create/', warning_tag_views.create_warning_tag, name='create_warning_tag'),
    path('warning_tags/', warning_tag_views.warning_tag_list, name='warning_tag_list'),
    path('warning_tags/<int:tag_id>/delete/', warning_tag_views.delete_warning_tag, name='delete_warning_tag'),
    
    # SavedMovie URLs
    path('saved_movies/create/', saved_movie_views.create_saved_movie, name='create_saved_movie'),
    path('saved_movies/', saved_movie_views.saved_movie_list, name='saved_movie_list'),
    path('saved_movies/<int:saved_movie_id>/delete/', saved_movie_views.delete_saved_movie, name='delete_saved_movie'),
]
