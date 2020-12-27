FROM andrebaceti/regen-timescale-db:0.3

############################################
# Use the same values of the dumped database
# ENV KONG_API
ENV POSTGRES_USER="murabei"
ENV POSTGRES_DB="murabei"
ENV POSTGRES_PASSWORD="is_very_nice!"

#################################################################
# Copy the dumpfile to docker-entrypoint-initdb.d so
# the dumped database will be recriated when the container starts
COPY database/database.sql /docker-entrypoint-initdb.d/database.sql
RUN chmod 777 -R /docker-entrypoint-initdb.d/
