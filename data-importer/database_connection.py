import os
import psycopg2

def get_db_config_variables():
    host = os.environ["LOCAL_HOST"]
    dbname = os.environ["DBNAME"]
    user = os.environ["USER_LOCAL_HOST"]
    password = os.environ["PASSWORD_LOCAL_HOST"]
    return host, dbname, user, password


def connect_db():
    host, dbname, user, password = get_db_config_variables()
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    conn.autocommit = True
    return conn


def get_url():
    # Define the database connection parameters
    host, dbname, user, password = get_db_config_variables()
    url = f"postgresql://{user}:{password}@{host}:5432/{dbname}"
    return url
