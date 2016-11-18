from datetime import datetime
import requests

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    help = 'Creates multiple fake users using randomuser.me API.'

    def add_arguments(self, parser):
        parser.add_argument('user_count', nargs='+', type=int)

    def handle(self, *args, **options):
        user_count = options['user_count'][0]

        response = requests.get("https://randomuser.me/api/?results={}".format(
            user_count
        ))

        for user in response.json()['results']:
            kwargs = {
                'username': user['login']['username'],
                'first_name': user['name']['first'],
                'last_name': user['name']['last'],
                'password': user['login']['password'],
                'date_joined': datetime.strptime(
                    user['registered'], '%Y-%m-%d %H:%M:%S'),
            }
            User.objects.create(**kwargs)

        self.stdout.write(self.style.SUCCESS(
            'Successfully created {} users!'.format(user_count))
        )
