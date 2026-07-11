import psycopg2


def get_connection():
    connection = psycopg2.connect(
        database="taskdb",
        user="postgres",
        password="niya11Nilav17$",
        host="localhost",
        port="5432"
    )

    return connection