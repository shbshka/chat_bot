import psycopg2

conn = psycopg2.connect(
    database="chat_bot",
    user="postgres",
    password="S0siRv3h1e5",
    host="127.0.0.1",
    port="1234"
)