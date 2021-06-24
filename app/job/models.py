import uuid
from django.db import models


class JobType(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(
        max_length=40,
        blank=True,
        unique=True,
        help_text=(
            "The Title does not have any effect for the job execution. "
            "It's just an identifier for finding specific jobs.\n"
            "If it's blank it will get an auto created string."
        )
    )
    description = models.TextField(
        blank=True,
        help_text=(
            "The description does not have any effect for the job execution. "
            "It's just a help for understanding the job."
        )
    )
    job_type = models.ForeignKey(
        to=JobType,
        on_delete=models.PROTECT,
        related_name="jobs"
    )
    configs = models.JSONField()
    frequency = models.IntegerField(
        default=1440,
        help_text=(
            "In which time intervalls should the job be executed?\n"
            "Time in Minutes."
        )
    )
    is_one_time_job = models.BooleanField(
        default=False,
        help_text=(
            "If True job will be just executed once and then deleted.\n"
            "If False job will be executed in given frequency."
        )
    )
    last_execution = models.DateTimeField(
        auto_now=True
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ('-last_execution', )

    def save(self, *args, **kwargs):
        self.set_title()
        super().save(*args, **kwargs)

    def set_title(self):
        if self.title:
            pass
        title = uuid.uuid4().hex[:6]
        while Job.objects.filter(title=title).exists():
            title = uuid.uuid4().hex[:6]
        self.title = title

    def __str__(self):
        return self.title


class JobExecutionLog(models.Model):
    job = models.ForeignKey(
        to=Job,
        on_delete=models.SET_NULL,
        related_name="execution_logs",
        null=True,
        editable=False
    )
    title = models.CharField(
        max_length=40,
        editable=False
    )
    description = models.TextField(
        editable=False
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ('-timestamp', )

    def save(self, *args, **kwargs):
        self.set_description()
        self.set_title()
        super().save(*args, **kwargs)

    def set_title(self):
        if not self.job:
            return
        self.title = self.job.title

    def set_description(self):
        if not self.job or self.description:
            return

        self.description = (
            f"Title: {self.job.title}\n"
            f"Job-Type: {self.job.job_type.name}\n"
            f"Inserted at: {self.job.timestamp.strftime('%Y-%m-%d %H:%M')}\n\n"
            f" - Description - \n{self.job.description}\n\n"
            f" - configs - \n\n{self.job.configs}"
        )

    def __str__(self):
        return f"{self.title} - {self.timestamp}"
