import psycopg2

conn = psycopg2.connect(
    database="chat_bot",
    user="postgres",
    password="",
    host="127.0.0.1",
    port="1234"
)
answer_id = []
answer = dict()
question = dict()

cur = conn.cursor()
cur.execute('SELECT id, answer FROM public.chat_bot;')
answers = cur.fetchall()
for row in answers:
    answer[row[0]] = row[1]

cur.execute('SELECT id, question FROM public.chat_bot;')
questions = cur.fetchall()
for row in questions:
    questions[row[0]] = row[1]

cur.close()
conn.close()


