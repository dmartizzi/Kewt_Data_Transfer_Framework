import os
import psycopg2

def db_connect():
    connection = psycopg2.connect(\
        f"host={os.environ['POSTGRES_HOST']} \
        dbname={os.environ['POSTGRES_DB']} \
        user={os.environ['POSTGRES_USER']} \
        password={os.environ['POSTGRES_PASSWORD']}")
    return(connection)

def check_table(connection, table_name, columns):
    cur = connection.cursor()

    table_query = "SELECT table_name \
                   FROM information_schema.tables \
                   WHERE table_schema='public' AND table_type='BASE TABLE';"
    cur.execute(table_query)
    connection.commit()
    table_list = cur.fetchall()

    table_obj = (table_name,)
    if table_obj not in table_list:
        create_query = f"CREATE TABLE {table_name} (id serial PRIMARY KEY, "
        for i, col in enumerate(columns):
            suffix = ", " if i < len(columns)-1 else ");"
            col_str = f"{col} double precision"+suffix
            create_query += col_str
        cur.execute(create_query)
        connection.commit()
    cur.close()

def insert_data(connection, table_name, data):
    insert_query = f"INSERT INTO {table_name} "
    col_names = "("+", ".join(data.keys())+") "
    col_values = "VALUES ("+", ".join([str(val) for val in data.values()])+");"
    insert_query = insert_query+col_names+col_values
    cur = connection.cursor()
    cur.execute(insert_query)
    connection.commit()
    cur.close()

def db_disconnect(connection):
    connection.close()
