import datetime
import os
import random
import sys

HOST = os.getenv("HOST", "localhost")
TABLE_NAME = os.getenv("TABLE_NAME")
BULK_SIZE = int(os.getenv("BULK_SIZE", 1))
EVENTS_PER_DAY = int(os.getenv("EVENTS_PER_DAY", 100000))
WORKERS = int(os.getenv("WORKERS", 10))
DB_NAME = os.getenv("DB_NAME")
HAS_DATE_COLUMN = False if int(os.getenv("HAS_DATE_COLUMN", 0)) == 0 else True

def generate_random_event(event_date: datetime.datetime) -> dict:
    event_id = random.randint(0, sys.maxsize)
    event_type = random.randint(0, 3)
    pokemon_id = random.randint(0, 10)
    event_datetime = event_date.replace(
        hour=random.randint(0, 23),
        minute=random.randint(0, 59))

    return_value = {
        "id": event_id,
        "time": event_datetime,
        "type": event_type,
        "pokemon_id": pokemon_id
    }

    if HAS_DATE_COLUMN:
        return_value["date"] = event_datetime.date()

    return return_value
