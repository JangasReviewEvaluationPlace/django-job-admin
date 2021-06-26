import threading
import os
from worker import Worker


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
