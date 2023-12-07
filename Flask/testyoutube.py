import psycopg2

hostname = 'localhost'
database = 'hemnet'
username = 'postgres'
password = 'Vanligt123!'
post_id = '5432'

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=password,
    port=post_id
)

conn.close()
