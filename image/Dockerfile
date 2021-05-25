FROM postgres:12

########################
# ENV DISPOSE_CONECTIONS
# ENV APP_NAME
# ENV KONG_API
# ENV SERVICE_URL
# ENV DISPOSE_CONECTIONS
########################

EXPOSE 5432
EXPOSE 5000

RUN apt-get update

#####################
# Updating repository
# Postgres repository
RUN apt-get install -y wget lsb-release curl
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Timescale repository
RUN sh -c 'wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | apt-key add -'
RUN sh -c 'echo "deb https://packagecloud.io/timescale/timescaledb/debian/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/timescaledb.list'
RUN apt-get update
#####################

################################################
# Now install appropriate package for PG version
RUN apt-get install -y timescaledb-postgresql-12
###############################################

################################################
# Installing Partman
RUN apt-get install -y postgresql-12-partman
################################################

###############################################
# Install postgis
RUN apt install -y postgis postgresql-12-postgis-3
###############################################

###############################################
# Install flask dependencies to backup database
RUN apt-get install -y g++ python3-dev libffi-dev curl && \
    apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip setuptools==45

COPY requirements/ /requirements
RUN pip3 install -r requirements/python_requirements.txt
###############################################

COPY app/ /app
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x ./docker-entrypoint.sh

###################################################
# Copia os scripts para a criação da base de backup
COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/
###################################################

COPY start_container.bash /start_container.bash
COPY wait-for-kong.bash /wait-for-kong.bash
RUN chmod +x ./start_container.bash
RUN chmod +x ./wait-for-kong.bash
ENV FLASK_APP app/app.py

CMD ["./start_container.bash"]
