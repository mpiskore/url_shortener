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
            "username": f"janedoe_{i}",
            "first_name": f"Jane_{i}",
            "last_name": f"Do{i}e",
            "password": f"johndoelovelove{i}",
            "date_joined": f"20{i}-10-22 21:37:11",
        }
        test_data.update(template_dict.copy())
    return json.dumps(test_data)


def test_command_output(mocker):
    mocked_get = mocker.patch.object(requests, "get")
    mocked_get.json.return_value["results"] = faked_users
    out = StringIO()
    call_command("create_fake_users", FAKE_USERS_COUNT, stdout=out)
    assert f"Successfully created {FAKE_USERS_COUNT} users!" in out.getvalue()
