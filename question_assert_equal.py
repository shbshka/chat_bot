from fetch_data import question, answer
import openai
import numpy as np


def assert_equal(text):
    for item in question:
        if text == question[item]:
            return answer[item]
        else:
            resp = openai.Embedding.create(
                input=[text, question[item]],
                engine="text-similarity-davinci-001"
            )
            embedding_text = resp["data"][0]["embedding"]
            embedding_question_item = resp["data"][1]["embedding"]
            similarity_score = np.dot(embedding_text, embedding_question_item)
            if similarity_score >= 0.9:
                return answer[item]





