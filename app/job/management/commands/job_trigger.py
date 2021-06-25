import logging

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from job.models import Job
from job.kafka_ import JobProducer

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Initial command for superuser creation'

    def handle(self, *args, **options):
        logging.info("Job Trigger Handler started.")
        jobs_to_execute = Job.objects.filter(is_active=True, next_execution__lte=now())
        if not jobs_to_execute.exists():
            logging.info("No Jobs to execute.")
            return
        logging.info(f"Number of jobs to execute: {jobs_to_execute.count()}")
        with JobProducer() as producer:
            for job in jobs_to_execute:
                producer.send(job=job)
