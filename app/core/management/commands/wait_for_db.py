"""
Django command to wait for db to be available
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # django command to wait for db

    def handle(self, *args, **options):
        # enry point for command.
        self.stdout.write('waiting for db...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('db unavailbale, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('db ready!'))