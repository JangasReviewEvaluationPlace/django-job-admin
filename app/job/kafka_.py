import logging
import json
from contextlib import AbstractContextManager

from django.conf import settings
from kafka import KafkaProducer

from .models import Job


logger = logging.getLogger(__name__)


class JobProducer(AbstractContextManager):
    def __enter__(self):
        logging.info("Init Kafka Producer")
        if not settings.KAFKA['enabled']:
            logging.warning("Kafka is not enabled. The message sending is just a simulation.")
            return self

        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA["bootstrap_servers"],
            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'),
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not settings.KAFKA['enabled']:
            return
        logging.info("Close Kafka Producer")
        self.producer.close()

    def send(self, job: Job):
        message = {
            "title": job.title,
            "job_type": job.job_type.name,
            "configs": job.configs
        }
        if settings.KAFKA['enabled']:
            self.producer.send(topic=settings.KAFKA["job_topic_name"], value=message)
        job.save()
        logging.info(f"Job sended. Details: {message}")
