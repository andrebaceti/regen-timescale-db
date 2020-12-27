#!/bin/bash
set -e
psql -v --username "$POSTGRES_USER" --dbname "postgres" -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '$POSTGRES_DB' AND pid <> pg_backend_pid();"
psql -v --username "$POSTGRES_USER" --dbname "postgres" -c "CREATE DATABASE backup WITH TEMPLATE $POSTGRES_DB"
