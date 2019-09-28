import json
import pytest
import requests

from django.core.management import call_command
from django.utils.six import StringIO

FAKE_USERS_COUNT = 10


@pytest.fixture
def faked_users(user_count=FAKE_USERS_COUNT):
    test_data = {}
    for i in range(user_count):
        i = "0" + str(i) if i < 10 else str(i)
        template_dict = {
            "username": "janedoe_{}".format(i),
            "first_name": "Jane_{}".format(i),
            "last_name": "Do{}e".format(i),
            "password": "johndoelovelove{}".format(i),
            "date_joined": "20{}-10-22 21:37:11".format(i),
        }
        test_data.update(template_dict.copy())
    return json.dumps(test_data)


def test_command_output(mocker):
    mocked_get = mocker.patch.object(requests, "get")
    mocked_get.json.return_value["results"] = faked_users
    out = StringIO()
    call_command("create_fake_users", FAKE_USERS_COUNT, stdout=out)
    assert f"Successfully created {FAKE_USERS_COUNT} users!" in out.getvalue()
