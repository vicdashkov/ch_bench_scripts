#!/usr/bin/env bash

export TABLE_NAME=bench_pokemon_event_sampling
export BULK_SIZE=10
export DB_NAME=sampling
export HAS_DATE_COLUMN=0
export EVENTS_PER_DAY=10
python inserter.py

export TABLE_NAME=bench_pokemon_event_non_sampling
export BULK_SIZE=10
export DB_NAME=sampling
export HAS_DATE_COLUMN=0
export EVENTS_PER_DAY=10
python inserter.py

