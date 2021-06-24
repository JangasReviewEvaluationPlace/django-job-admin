import logging
import os

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Initial command for superuser creation'

    def handle(self, *args, **options):
        username = os.getenv("INITIAL_SUPERUSER_NAME", "root")
        password = os.getenv("INITIAL_SUPERUSER_PASSWORD", "secure_pw_123")

        User = get_user_model()
        try:
            User.objects.create_superuser(username=username, password=password)
            logging.info(f"Superuser with username {username} and password {password} created.")
        except IntegrityError:
            logging.warning(f"Superuser with username {username} already exists.")
