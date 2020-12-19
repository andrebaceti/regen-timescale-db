# Regenerative Postgres DB for unit-tests

This image works for **postgres:12** and have postgis and timescale extenssion avaiable.

## Development and support
This image was developed by Murabei Data Science to addresss the problem of building test databases for data science. It is hard to make unit-test for DS systems and update database as migrations occorur.

![www.murabei.com](murabei-logo.png "Murabei Data Science")
www.murabei.com

## General description
This is the source code used to build the image regen-timescale-db. This image runs a Postgres with timescale-db extenssion at port 5432 and a Flask server listening at 5000. Calling the port 5000 with a get request at `/reload-db/$APP_NAME/` leads to the regeneration of the database.

This image can be used to regenerate the database after unit tests, an example of a nosetest implementation can be checked at `nosetest-example`.

This image is mostly based on postgres oficial Docker image and timescale db instalation scripts.

https://hub.docker.com/_/postgres/
https://docs.timescale.com/latest/getting-started/installation/debian/installation-apt-debian

You can check the source codes on githib, it have the image and also an example for building and creating a nosetest using regen end-point.

https://github.com/andrebaceti/regen-timescale-db

## Environment variables
During the build or usage variables should be set:
- **APP_NAME:** Sets the url that will be used to regenerate the database `/reload-db/$APP_NAME/`.
- **DISPOSE_CONECTIONS:** This url may be called many times to dispose conections at Flask or Django. The database during the regen is droped and rebuild what can leads to database errors. Usualy an end-point can be implemented, an example:

```
@app.route('/pool-conections-dispose/')
def dispose_conections():
    if app.debug:
        logging.warning('disposing conections...')
        db.session.close()
        db.engine.dispose()
        return 'True'
    else:
        return 'False'
```

## Build database
To build a database it is necessary to make a dump of a previus one and copy to `docker-entrypoint-initdb.d/`. An example of a possible docker file:
```
FROM andrebaceti/regen-timescale-db:0.0

############################################
# Use the same values of the dumped database
ENV POSTGRES_USER="murabei"
ENV POSTGRES_DB="murabei"
ENV POSTGRES_PASSWORD="is_very_nice!"

###############################################
# Name of the app, this will be used to set the
# regen end-point
ENV APP_NAME="regen-test"

#################################################################
# Copy the dumpfile to docker-entrypoint-initdb.d so
# the dumped database will be recriated when the container starts
COPY database/database.sql /docker-entrypoint-initdb.d/database.sql
RUN chmod 777 -R /docker-entrypoint-initdb.d/
```

## Examples
### Build image
`image-build-example`

### Create a nosetest with database regen between tests
`nosetest-example`
