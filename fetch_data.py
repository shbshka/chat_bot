from database_data import conn

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
    question[row[0]] = row[1]

cur.close()
conn.close()


