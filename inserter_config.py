import os

HOST = os.getenv("HOST", "localhost")
TABLE_NAME = os.getenv("TABLE_NAME")
BULK_SIZE = int(os.getenv("BULK_SIZE", 1))
EVENTS_PER_DAY = int(os.getenv("EVENTS_PER_DAY", 100000))
WORKERS = int(os.getenv("WORKERS", 10))
DB_NAME = os.getenv("DB_NAME")
HAS_DATE_COLUMN = False if int(os.getenv("HAS_DATE_COLUMN", 0)) == 0 else True
