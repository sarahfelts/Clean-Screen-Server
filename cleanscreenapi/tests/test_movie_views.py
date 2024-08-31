import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_create_movie(api_client, user):
    url = reverse('movie-list')
    data = {'title': 'New Movie', 'year': 2024, 'rating': 'PG'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_movie_list(api_client):
    url = reverse('movie-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_movie_detail(api_client, movie):
    url = reverse('movie-detail', args=[movie.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
