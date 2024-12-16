import csv
from django.core.management.base import BaseCommand

from employee.models import Employee


class Command(BaseCommand):
    help = 'Import data from a CSV file and stores in model'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        # Open and read the CSV file
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Perform data processing
                id = row['emp_id']
                forename = row['forename']
                surname = row['surname']
                gender = row['gender']
                age = row['age']


                # Create a new Employee object and save it
                employee = Employee(
                    emp_id=id,
                    forename=forename,
                    surname=surname,
                    gender=gender,
                    age=age,
                )
                employee.save()


        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
        self.stdout.write(self.style.SUCCESS(f'Records processed: {csv_reader.line_num - 1}'))
        self.stdout.write(self.style.SUCCESS(f'Data successfully added to model : {csv_reader.line_num - 1}'))

