"""
Module app.py.

Flask aplication to reload database.
"""

import os
import subprocess
import requests
import logging
from flask import Flask
app = Flask(__name__)
dispose_conections_url = os.environ.get(
    'DISPOSE_CONECTIONS')
app_name = os.environ.get(
    'APP_NAME')


def dispose_conections():
    """Call end-point to dispose connections from flask or Django or etc..."""
    if dispose_conections_url is not None:
        logging.warning('request app conections pool dispose')
        for i in range(20):
            requests.get(dispose_conections_url)


@app.route('/reload-db/' + app_name + '/')
def reload_database():
    """
    Reload database to original state.

    Drops the public schema and reload the orinal dump file of the database
    """
    password = os.environ.get('POSTGRES_PASSWORD')
    username = os.environ.get('POSTGRES_USER')
    database = os.environ.get('POSTGRES_DB')

    base_psql = "PGPASSWORD={password} psql -h 0.0.0.0 -p 5432 -U " +\
        "{username} postgres"
    base_psql = base_psql.format(
        password=password,
        username=username,
        database=username)

    # Kill all conections
    cmd_noconection_database = base_psql +\
        """ -c "UPDATE pg_database SET datallowconn = 'false' WHERE datname = '{database}';" """.format(
            database=database)
    with open(os.devnull, 'w') as fp:
        pipe = subprocess.Popen(cmd_noconection_database, stdout=fp,
                                shell=True)
    ret_code = pipe.wait()

    cmd_dropconection_database = base_psql +\
        ''' -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = '{database}' AND pid <> pg_backend_pid();" '''.format(
            database=username)
    with open(os.devnull, 'w') as fp:
        pipe = subprocess.Popen(cmd_dropconection_database, stdout=fp, shell=True)
    ret_code = pipe.wait()

    cmd_drop_database = base_psql +\
        ''' -c "DROP DATABASE {database};"'''.format(
            database=username)
    with open(os.devnull, 'w') as fp:
        pipe = subprocess.Popen(cmd_drop_database, stdout=fp, shell=True)
    ret_code = pipe.wait()

    cmd_create_database = base_psql +\
        " -c 'create database {database} WITH TEMPLATE backup'".format(
            database=username)
    with open(os.devnull, 'w') as fp:
        pipe = subprocess.Popen(cmd_create_database, stdout=fp, shell=True)
    ret_code = pipe.wait()

    dispose_conections()

    if ret_code > 0:
        return 'false'
    else:
        return 'true'
