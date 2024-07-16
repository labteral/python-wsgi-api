#!/bin/bash
cd $(dirname $0)/..
source env.sh
cd docker

export COMPOSE_PROJECT_NAME=${COMPOSE_PROJECT_NAME}-vpn
docker compose -f docker-compose-vpn.yaml down --remove-orphans
