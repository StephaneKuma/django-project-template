from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **options):
        new_project_name = options['new_project_name']

        # logic to rename the project

        files_to_rename = ['demo/settings/base.py', 'demo/wsqi.py', 'manage.py']
        folder_to_rename = 'demo'

        # for file in files_to_rename:
