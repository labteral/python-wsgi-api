#!/bin/bash
cd $(dirname $0)/..
source env.sh
cd src

PYTHONUNBUFFERED=1 uwsgi \
--master \
--http :8080 \
--wsgi-file main.py \
--callable app \
--processes $API_PROCESSES_COUNT \
--threads $API_THREADS_COUNT
