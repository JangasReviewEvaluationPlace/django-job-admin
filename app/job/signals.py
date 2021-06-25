from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Job, JobExecutionLog
from .kafka_ import JobProducer


@receiver(post_save, sender=Job)
def initial_job_command(instance: Job, created: bool, *args, **kwargs):
    if created:
        with JobProducer() as producer:
            producer.send(job=instance)
    else:
        JobExecutionLog.objects.create(job=instance)
