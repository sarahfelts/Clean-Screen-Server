from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(null=True, blank=True)
    rating = models.CharField(max_length=50, null=True, blank=True)  # For MPA rating or similar
    genre = models.CharField(max_length=255, null=True, blank=True)
    user_rating_total = models.FloatField(default=0)  # Total of all user ratings
    user_rating_count = models.IntegerField(default=0)  # Number of user ratings
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def user_rating(self):
        if self.user_rating_count == 0:
            return None
        return self.user_rating_total / self.user_rating_count

    def __str__(self):
        return str(self.title)
