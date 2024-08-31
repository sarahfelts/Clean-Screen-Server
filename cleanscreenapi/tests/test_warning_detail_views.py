import pytest
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db
def test_create_warning_detail(api_client):
    url = reverse('warningdetail-list')
    data = {'name': 'New Warning Detail', 'tag': 'Test Tag'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_get_warning_detail_list(api_client):
    url = reverse('warningdetail-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
