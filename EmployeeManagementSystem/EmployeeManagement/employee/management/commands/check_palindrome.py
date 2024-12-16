from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'checks string is palindrome or not'

    def add_arguments(self, parser):
        parser.add_argument("data", type=str, help='')
        parser.add_argument('--option', type=bool, help='A custom option')
        # parser.add_argument('--option2', type=int, help='A custom option')

    def handle(self, *args, **options):
        self.stdout.write('This is my custom management command!')
        if options["option"]:

            s = options["data"].replace(" ", "").lower()
            result = s[::-1]
            if result == s:
                self.stdout.write(f"{options['data']} is a palindrome")
            else:
                self.stdout.write(f"{options['data']} is not a palindrome")
        else:
            # string reverse
            self.stdout.write(options["data"][::-1])
