import json
import mock
import requests

from django.core.management import call_command
from django.test import TestCase
from django.utils.six import StringIO


class UserFakerTest(TestCase):
    def faked_users(self, user_count=10):
        test_data = {}
        for i in range(user_count):
            i = "0" + str(i) if i < 10 else str(i)
            template_dict = {
                "username": f"janedoe_{i}",
                "first_name": f"Jane_{i}",
                "last_name": f"Do{i}e",
                "password": f"johndoelovelove{i}",
                "date_joined": f"20{i}-10-22 21:37:11",
            }
            test_data.update(template_dict.copy())
        return json.dumps(test_data)

    @mock.patch.object(requests, "get")
    def test_command_output(self, request_mock):
        user_count = 10
        request_mock.json.return_value["results"] = self.faked_users(user_count)
        out = StringIO()
        call_command("create_fake_users", str(user_count), stdout=out)
        self.assertIn("Successfully created 10 users!", out.getvalue())
