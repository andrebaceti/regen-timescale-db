# regen-timescale-db

This is the source code used to build the image regen-timescale-db. This image runs a Postgres with timescale-db extenssion at port 5432 and a Flask server listening at 5000. Calling the port 5000 with a get request at `/reload-db/$APP_NAME/` leads to the regeneration of the database.

This image can be used to regenerate the database after unit tests, an example of a nosetest implementation can be checked at `nosetest-example`
