from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.core import management
import shutil
import os


class Command(BaseCommand):
    help = 'Delete migrations folders'

    def add_arguments(self, parser):
        parser.add_argument('list_apps', nargs='+', type=str)

    def handle(self, *args, **options):
        list_apps = options['list_apps']
        for app_name in list_apps:
            app_dir = os.path.join(settings.BASE_DIR, app_name + "/migrations")
            try:
                if os.path.exists(app_dir) and os.path.isdir(app_dir):
                    shutil.rmtree(app_dir)
                    self.stdout.write(
                        self.style.SUCCESS(
                            'Migrations folder successfully deleted in "%s"' %
                            app_name))
            except OSError as e:
                raise CommandError("Error: %s : %s" % (app_dir, e.strerror))

        for app_name in list_apps:
            management.call_command('makemigrations', app_name)

        management.call_command('migrate')
