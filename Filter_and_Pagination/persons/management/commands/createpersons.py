from django.core.management.base import BaseCommand, CommandError
from persons.models import Person
from faker import Faker
from faker.providers import person, phone_number
from random import randint

fake = Faker()
fake.add_provider(person)
fake.add_provider(phone_number)



class Command(BaseCommand):
    help = 'Populate the database with Person data'

    def handle(self, *args, **options):
        """ Do your work here """
        for i in range(10000):
            Person.objects.create(firstname=fake.first_name(), lastname=fake.last_name(), phone=fake.phone_number(), age=randint(20,80))
        self.stdout.write('There are {} persons in the database!'.format(Person.objects.count()))