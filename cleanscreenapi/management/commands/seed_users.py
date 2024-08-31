from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from cleanscreenapi.models import User

class Command(BaseCommand):
    help = 'Seed the database with users'

    def handle(self, *args, **kwargs):
        users = [
            {
                'email': 'john.doe@example.com',
                'username': 'johndoe',
                'password': 'password123',
                'first_name': 'John',
                'last_name': 'Doe'
            },
            {
                'email': 'jane.smith@example.com',
                'username': 'janesmith',
                'password': 'securepassword',
                'first_name': 'Jane',
                'last_name': 'Smith'
            },
            {
                'email': 'admin@example.com',
                'username': 'admin',
                'password': 'adminpassword',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        ]

        for user_data in users:
            # Create user with hashed password
            user_data['password'] = make_password(user_data['password'])
            User.objects.create(**user_data)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with users'))
