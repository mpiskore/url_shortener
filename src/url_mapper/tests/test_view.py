import pytest
from django.conf import settings

from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

from url_mapper.models import UrlMapper


@pytest.fixture
def user() -> User:
    return User.objects.create(
        **{"username": "test", "email": "test@example.com", "password": "secret"}
    )


def test_main_page(client):
    response = client.get(reverse("home"))
    assert response.status_code, 200


@pytest.mark.usefixtures("user")
@pytest.mark.usefixtures("db")
def test_success_message(client, mocker):
    mocker.patch.object(UrlMapper, "get_shortened_url", return_value="123456")
    add_message_mock = mocker.patch.object(messages, "add_message")
    response = client.post(reverse("home"), {"original_url": "example.com"})
    assert response.status_code, 302  # redirected to result
    test_url = settings.BASE_URL + "/123456"
    add_message_mock.assert_called_once_with(
        response.wsgi_request,
        messages.INFO,
        f'Shortened URL address for example.com is <a href="{test_url}">{test_url}</a>',
    )
