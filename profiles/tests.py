import pytest
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed

from profiles.models import Profile


@pytest.mark.django_db
def test_profiles_index():
    client = Client()
    path = reverse('profile_index')
    response = client.get(path)
    assert "<title>Profiles</title>" in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profiles():
    client = Client()
    user = User.objects.create(
        username='username',
        last_name='last name',
        first_name='first name',
        email='aa@abc.com',
        password='password',
    )

    Profile.objects.create(
        favorite_city="Lol city",
        user=user)
    path = reverse('profile', kwargs={'username': 'username'})
    response = client.get(path)
    assert "<title>username</title>" in response.content.decode()
    assert response.status_code == 200
    assertTemplateUsed(response, "profiles/profile.html")
