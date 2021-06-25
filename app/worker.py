import logging
import os
from time import sleep
from subprocess import call


logger = logging.getLogger(__name__)


class Worker:
    def __init__(self):
        self.stop = False
        self.path = os.getenv("RELATIVE_PATH_TO_APP", "")

    def run(self):
        logging.info("Start Worker...")
        while not self.stop:
            logging.info("Execute Worker")
            call(["python", f"{self.path}manage.py", "job_trigger"])
            sleep(int(os.getenv("WORKER_EXECUTION_INTERVAL_IN_SECONDS", 15)))

    def stop_worker(self):
        self.stop = True
