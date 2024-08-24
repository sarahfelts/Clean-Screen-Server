from django.db import models
from .user import User
from .movie import Movie

class Warning(models.Model):
    SEVERITY_CHOICES = [
        ('Close your eyes'),
        ('Leave the room'),
        ('Leave the theater'),
    ]

    timestamp = models.TimeField()
    description = models.TextField()
    tag = models.CharField(max_length=50)
    severity = models.CharField(max_length=50, choices=SEVERITY_CHOICES)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='warnings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='warnings')

    def __str__(self):
        return f'{self.tag} at {self.timestamp} in {self.movie.title}'
