from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'New user create'

    def handle(self, *args, **options):

        # print(options)
        user = User.objects.create_user(username=options.get('username'), email=options.get('email'))
        user.set_password(raw_password=options.get('password'))
        user.save()
        # print(user)

    def add_arguments(self, parser):

        parser.add_argument('-n', '--name', action='store', dest='username', type=str, help='Input username')
        parser.add_argument('-p', '--password', action='store', dest='password', type=str, help='Input password')
        parser.add_argument('-e', '--email', action='store', dest='email', type=str, help='Input email')


