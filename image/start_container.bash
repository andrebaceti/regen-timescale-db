#!/bin/bash
source wait-for-kong.bash

echo "Tune for timescale"
timescaledb-tune -yes

echo "Starting Flask server"
flask run --host=0.0.0.0 --port=5000 &

echo "Starting postgres server"
postgres
