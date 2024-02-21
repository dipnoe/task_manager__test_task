from django.core.management import BaseCommand

from task_manager.models import Executor


class Command(BaseCommand):
    help = "Creating Executor object"

    def handle(self, *args, **options):
        if options['name']:
            name = options['name']
        else:
            name = "Executor name"

        try:
            executor = Executor.objects.get(name=name)
            print('Executor exists, you can use his id "%s" for creating a task.' % executor.pk)
        except Executor.DoesNotExist:
            executor = Executor.objects.create(
                name=name
            )
            executor.save()
            print('Executor "%s" was created successfully.' % executor.name)

    def add_arguments(self, parser):
        parser.add_argument(
            '--name', action='store', type=str
        )
