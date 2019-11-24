from datetime import datetime
import requests

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = "Creates multiple fake users using randomuser.me API."

    def add_arguments(self, parser):
        parser.add_argument("user_count", nargs="+", type=int)

    def handle(self, *args, **options):
        duplicated_users = 0
        user_count = options["user_count"][0]

        response = requests.get(f"https://randomuser.me/api/?results={user_count}")

        for user in response.json()["results"]:
            kwargs = {
                "username": user["login"]["username"],
                "first_name": user["name"]["first"],
                "last_name": user["name"]["last"],
                "password": user["login"]["password"],
                "date_joined": datetime.strptime(
                    user["registered"]["date"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ),
            }
            try:
                User.objects.create(**kwargs)
            except IntegrityError:
                # This user already exists in our database
                # (This may happen when large amount of users are being
                # populated to our database in multiple tranches).
                # We can handle this by counting the number of fails and re-run
                # the command for missing number of users.
                duplicated_users += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created {user_count - duplicated_users} users!"
            )
        )

        if duplicated_users > 0:
            # run the command again for all the users that were duplicated.
            options["user_count"][0] = duplicated_users
            self.handle(*args, **options)
