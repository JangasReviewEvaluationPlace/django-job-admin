#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import threading
import logging
from dotenv import load_dotenv
from worker import Worker

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(LOG_LEVEL))


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if os.getenv("WORKER_ENABLED", "True").lower() == "true":
        if os.path.isfile("worker.tmp"):
            os.remove("worker.tmp")
        else:
            worker = Worker()
            thread = threading.Thread(daemon=True, target=worker.run)
            thread.setName("Python Worker")
            thread.start()
            with open("worker.tmp", "w") as f:
                f.write("Worker is running")
    main()
