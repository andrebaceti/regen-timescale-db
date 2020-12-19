#!/bin/bash
set -e
psql -v --username "$POSTGRES_USER" --dbname "postgres" -c "CREATE DATABASE backup WITH TEMPLATE $POSTGRES_DB"
