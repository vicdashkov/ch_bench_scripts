#!/usr/bin/env bash

export QUERY="SELECT count() from sampling.bench_pokemon_event_sampling group by toYYYYMM(time)"
python selecter.py

export QUERY="SELECT count() from sampling.bench_pokemon_event_non_sampling group by toYYYYMM(time)"
python selecter.py
