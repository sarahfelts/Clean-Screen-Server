import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse('user-list')
    data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'password'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_user_list(api_client, user):
    url = reverse('user-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_get_user_detail(api_client, user):
    url = reverse('user-detail', args=[user.id])
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
