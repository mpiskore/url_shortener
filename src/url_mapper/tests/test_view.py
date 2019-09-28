import mock

from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client, TestCase

from url_mapper.models import UrlMapper


class UrlMapperViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # create a test user
        User.objects.create(
            **{"username": "test", "email": "test@example.com", "password": "secret"}
        )
        super(UrlMapperViewTest, self).setUp()

    def test_main_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    @mock.patch.object(UrlMapper, "get_shortened_url", return_value="123456")
    @mock.patch.object(messages, "add_message")
    def test_success_message(self, add_message_mock, shortenening_mock):
        response = self.client.post(reverse("home"), {"original_url": "example.com"})
        self.assertEqual(response.status_code, 302)  # redirected to result
        test_url = "http://127.0.0.1:8000/123456"
        add_message_mock.assert_called_once_with(
            response.wsgi_request,
            messages.INFO,
            ('Shortened URL address for example.com is <a href="{0}">{0}</a>').format(
                test_url
            ),
        )
