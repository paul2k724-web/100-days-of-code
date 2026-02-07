import time
import logging
import random

# ---------- LOGGING SETUP ----------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Scheduler started")

# ---------- TASK ----------
def task():
    logging.info("Task running")

    # simulate random failure
    if random.randint(1, 5) == 1:
        raise Exception("Random failure occurred")

    logging.info("Task completed successfully")

# ---------- SCHEDULER LOOP ----------
while True:
    try:
        task()
    except Exception as e:
        logging.error(f"Error: {e}")

    logging.info("Waiting 10 seconds\n")
    time.sleep(10)
