from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'New user create'

    def handle(self, *args, **options):

        print(User.objects.all())
