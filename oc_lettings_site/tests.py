
import pytest

from django.urls import reverse
from django.test import Client
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_holiday_homes():
    client = Client()
    path = reverse('home')
    response = client.get(path)
    assert "<title>Holiday Homes</title>" in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "oc_lettings_site/home.html")
