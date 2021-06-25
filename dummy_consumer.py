import os
import json
from kafka import KafkaConsumer
from dotenv import load_dotenv

load_dotenv(dotenv_path="./app/.env")


consumer = KafkaConsumer(
    'job',
    bootstrap_servers=os.getenv("KAFKA_BOOTSTRAP_SERVERS").split(),
    value_deserializer=lambda msg: json.loads(msg.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("WAIT FOR MESSAGE")
for message in consumer:
    print(message.value)
