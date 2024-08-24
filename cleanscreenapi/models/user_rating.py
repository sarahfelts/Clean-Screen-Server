from django.conf import settings
from django.db import models
from .movie import Movie

class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='user_ratings')
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user.email} rated {self.movie.title}: {self.rating}'
