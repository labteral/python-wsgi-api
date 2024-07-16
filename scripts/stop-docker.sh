#!/bin/bash
cd $(dirname $0)/..
source env.sh
cd docker

docker compose down --remove-orphans
