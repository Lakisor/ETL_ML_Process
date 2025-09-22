import logging
from lib.workers.worker import Worker

def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    logging.info("ETL pipeline started")

    worker = Worker()
    worker.start()

    logging.info("ETL pipeline finished successfully")

if __name__ == "__main__":
    main()
