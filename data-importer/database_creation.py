import os
import csv
from database_connection import connect_db


def create_database_from_csv(files_path, schema):
    conn = connect_db()
    schema = schema
    cur = conn.cursor()
    create_schema = f"CREATE SCHEMA IF NOT EXISTS {schema};"
    cur.execute(create_schema)

    for file in os.listdir(files_path):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            with open(file, "r") as f:
                reader = csv.reader(f, delimiter=',')
                header = next(reader)
                create_table_sql = f"CREATE TABLE IF NOT EXISTS {schema}.{table_name} ({', '.join([f'{col} VARCHAR(200)' for col in header])});"
                cur.execute(create_table_sql)
                insert_sql = f"INSERT INTO {schema}.{table_name} ({', '.join(header)}) VALUES ({', '.join(['%s' for _ in header])})"
                cur.executemany(insert_sql, reader)
                cur.close()

    conn.close()
