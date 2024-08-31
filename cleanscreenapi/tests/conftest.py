import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from cleanscreenapi.models import Movie, WarningIterable

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return get_user_model().objects.create_user(username='testuser', email='testuser@example.com', password='password')

@pytest.fixture
def movie():
    return Movie.objects.create(title='Test Movie', year=2024, rating='PG')

@pytest.fixture
def warning(movie, user):
    return WarningIterable.objects.create(timestamp='00:10:00', description='Test Warning', tag='Test Tag', severity='Close your eyes', movie=movie, user=user)
