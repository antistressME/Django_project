from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Delete test products from the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully delete Categories'))

        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Successfully delete Products'))

