import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="sentinelstream",
        user="postgres",
        password="postgres@123",
        port=5434
    )
