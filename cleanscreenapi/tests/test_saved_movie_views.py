import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_create_saved_movie(api_client, user, movie):
    url = reverse('savedmovie-list')
    data = {'user': user.id, 'movie': movie.id}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_saved_movie_list(api_client, user):
    url = reverse('savedmovie-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
