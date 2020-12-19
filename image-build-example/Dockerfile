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
