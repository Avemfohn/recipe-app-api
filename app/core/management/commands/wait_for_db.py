"""
Django command to wait for database to be available
"""
import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                self.check(databases=['default'])  # Correct parameter name
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
