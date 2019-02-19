import asyncio
import logging

import asyncpool
from aioch import Client
import datetime
import time
from scripts import inserter_config
from scripts.inserter_config import generate_random_event
from scripts.utils import format_date_from_timestamp

total_inserted_events = 0
pool = {}


def create_pool():
    for i in range(inserter_config.WORKERS):
        client = Client(inserter_config.HOST)
        pool[i] = {"c": client, "a": True}


def get_connection():
    for i, val in pool.items():
        if val['a']:
            val['a'] = False
            return i, val['c']


async def write_to_event(data: list, _):
    global total_inserted_events
    print(f"writing to {inserter_config.TABLE_NAME} {len(data)} rows; total count: {total_inserted_events}")
    conn_id, conn = get_connection()
    await conn.execute(f'INSERT INTO {inserter_config.DB_NAME}.{inserter_config.TABLE_NAME} VALUES', data)

    total_inserted_events += len(data)

    return_connection(conn_id)


def return_connection(connection_id):
    pool[connection_id]['a'] = True


def generate_random_events(event_date: datetime.datetime, number_events: int) -> list:
    return [generate_random_event(event_date) for _ in range(number_events)]


async def fill_events(_loop, number_per_day, bulk_size):
    async with asyncpool.AsyncPool(
            _loop,
            num_workers=inserter_config.WORKERS,
            worker_co=write_to_event,
            max_task_time=300,
            log_every_n=10,
            name="CHPool",
            logger=logging.getLogger("CHPool")) as p:

        insert_time = datetime.datetime(2018, 1, 1)
        for i in range(365):
            for _ in range(int(number_per_day / bulk_size)):
                events = generate_random_events(insert_time, bulk_size)
                await p.push(events, None)

            insert_time = insert_time + datetime.timedelta(days=1)


def log_experiment(experiment_took):
    with open("inserter_experiments_log.txt", 'a') as f:
        text = f"{format_date_from_timestamp(time.time())} - " \
            f"table: {inserter_config.TABLE_NAME} - " \
            f"db: {inserter_config.DB_NAME} - " \
            f"inserted: {total_inserted_events} - " \
            f"took: {round(experiment_took, 2)} - " \
            f"bulk size: {inserter_config.BULK_SIZE} - " \
            f"events per day: {inserter_config.EVENTS_PER_DAY} - " \
            f"workers: {inserter_config.WORKERS}\n"
        f.write(text)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    create_pool()

    start = time.time()
    print("inserter started at", format_date_from_timestamp(start))
    loop.run_until_complete(fill_events(loop, inserter_config.EVENTS_PER_DAY, inserter_config.BULK_SIZE))
    end = time.time()
    took = end - start
    print(f"inserter ended at {format_date_from_timestamp(end)}; took: {took} seconds")
    log_experiment(took)
