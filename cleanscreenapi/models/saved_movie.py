from django.db import models
from .user import User
from .movie import Movie

class SavedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_movies')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='saved_movies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.movie.title}"
