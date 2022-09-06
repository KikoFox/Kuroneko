from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = 'Run discord bot with django server'

    def handle(self, *args, **options):

        subprocess.Popen('python manage.py runserver')
        subprocess.Popen('python manage.py start_bot')
