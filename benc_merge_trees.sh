#!/usr/bin/env bash

export TABLE_NAME=event_time_batch
export BULK_SIZE=10
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=0
python inserter.py

export TABLE_NAME=event_time_single
export BULK_SIZE=1
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=0
python inserter.py

export TABLE_NAME=even_time_order_func_batch
export BULK_SIZE=10
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=0
python inserter.py

export TABLE_NAME=even_time_order_func_single
export BULK_SIZE=1
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=0
python inserter.py

export TABLE_NAME=event_date_batch
export BULK_SIZE=10
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=1
python inserter.py

export TABLE_NAME=event_date_single
export BULK_SIZE=1
export DB_NAME=merge_tree
export HAS_DATE_COLUMN=1
python inserter.py