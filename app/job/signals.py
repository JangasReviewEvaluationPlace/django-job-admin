from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Job, JobExecutionLog


@receiver(post_save, sender=Job)
def initial_job_command(instance, created, *args, **kwargs):
    JobExecutionLog.objects.create(job=instance)
