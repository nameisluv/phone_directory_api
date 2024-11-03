from django.core.management.base import BaseCommand
from api.models import User, Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Create 10 sample users
            user = User.objects.create_user(
                username=fake.name(),
                email=fake.email(),
                password='password123'
            )
            for _ in range(5):  # Each user has 5 contacts
                Contact.objects.create(
                    user=user,
                    name=fake.name(),
                    phone_number=fake.phone_number()
                )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database!'))
