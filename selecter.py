import time
from clickhouse_driver import Client

import selecter_config
from utils import format_date_from_timestamp

client = Client('localhost')


def select_with_timing() -> float:
    start = time.time()
    client.execute(selecter_config.QUERY)
    end = time.time()
    return end - start


def benchmark_query():
    with open("selecter_experiments_log.txt", 'a') as f:
        text = '\n '
        text += format_date_from_timestamp(time.time())
        text += '\n'
        text += selecter_config.QUERY
        for i in range(selecter_config.NUMBER_BENCHMARK_RUNS):
            text += f"\n attempt {i} took: {round(select_with_timing(), 5)}s"
        text += '\n'
        f.write(text)


if __name__ == '__main__':
    benchmark_query()
