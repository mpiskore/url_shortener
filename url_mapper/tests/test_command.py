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
            i = '0' + str(i) if i < 10 else str(i)
            template_dict = {
                "username": "janedoe_{}".format(i),
                "first_name": "Jane_{}".format(i),
                "last_name": "Do{}e".format(i),
                "password": "johndoelovelove{}".format(i),
                "date_joined": '20{}-10-22 21:37:11'.format(i),
            }
            test_data.update(template_dict.copy())
        return json.dumps(test_data)

    @mock.patch.object(requests, 'get')
    def test_command_output(self, request_mock):
        user_count = 10
        request_mock.json.return_value['results'] = self.faked_users(user_count)
        out = StringIO()
        call_command('create_fake_users', str(user_count), stdout=out)
        self.assertIn('Successfully created 10 users!', out.getvalue())
