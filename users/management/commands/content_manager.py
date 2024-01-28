from django.core.management.base import BaseCommand
from users.models import User  # Замените 'users.models' на правильный путь к вашей пользовательской модели
from django.contrib.auth.models import Group


class CommandGroup(BaseCommand):
    help = 'Create a group of managers'

    def handle(self, *args, **options):
        try:
            managers_group = Group.objects.get(name='Blog_Managers')
            self.stdout.write(self.style.SUCCESS('Managers group already exists.'))
        except Group.DoesNotExist:
            managers_group = Group.objects.create(name='Blog_Managers')
            self.stdout.write(self.style.SUCCESS('Managers group created successfully.'))


class Command(BaseCommand):

    def handle(self, *args, **options):
        email = input('Enter email address: ')
        password = input('Enter password: ')

        user = User.objects.create(
            email=email,
            is_staff=True,
            is_active=True
        )

        user.set_password(password)
        user.save()

        try:
            managers_group = Group.objects.get(name='Blog_Managers')
            self.stdout.write(self.style.SUCCESS('Managers group already exists.'))
        except Group.DoesNotExist:
            managers_group = Group.objects.create(name='Blog_Managers')
            self.stdout.write(self.style.SUCCESS('Managers group created successfully.'))

        # Добавьте пользователя в группу Blog_Managers
        user.groups.add(managers_group)
