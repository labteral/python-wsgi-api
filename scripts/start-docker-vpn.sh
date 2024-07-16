#!/bin/bash
cd $(dirname $0)/..
source env.sh
cd docker

docker compose up -f docker-compose-vpn.yaml --build $@
