import logging
import json
from contextlib import AbstractContextManager

from django.conf import settings
from kafka import KafkaProducer


logger = logging.getLogger(__name__)


class Producer(AbstractContextManager):
    def __enter__(self):
        logging.info("Init Kafka Producer")
        self.producer = KafkaProducer(
            bootstrap_servers=settings.KAFKA["bootstrap_servers"],
            value_serializer=lambda msg: json.dumps(msg).encode('utf-8'),
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info("Close Kafka Producer")
        self.producer.close()

    def send(self, topic: str, message: dict):
        self.producer.send(topic=topic, value=message)
        logging.info(f"Message sended // {message}")
