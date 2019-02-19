import datetime


def format_date_from_timestamp(posix_time):
    return datetime.datetime.fromtimestamp(posix_time).strftime('%Y-%m-%d %H:%M:%S')
