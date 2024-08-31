import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_create_warning(api_client, user, movie):
    url = reverse('warning-list')
    data = {'timestamp': '00:15:00', 'description': 'Another Test Warning', 'tag': 'Another Test Tag', 'severity': 'Leave the room', 'movie': movie.id, 'user': user.id}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_warning_list(api_client):
    url = reverse('warning-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_warning_detail(api_client, warning):
    url = reverse('warning-detail', args=[warning.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK