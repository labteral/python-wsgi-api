#!/bin/bash
cd $(dirname $0)/..
source env.sh
cd src

uwsgi \
--master \
--http :8080 \
--wsgi-file main.py \
--callable app \
--processes $API_PROCESSES_COUNT \
--threads $API_THREADS_COUNT \
--unbuffered
