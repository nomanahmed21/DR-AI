import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests
import joblib 

df =joblib.load("data_embeddings.joblib")


def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json= {
        "model" : "bge-m3",
        "input": text_list
    })
    return r.json()['embeddings'] 

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    return r.json()['response']

user_input = input("Ask A Question:")
question_embedding = create_embeddings(user_input)[0]

similarity = cosine_similarity(np.vstack(df["embedding"]), [question_embedding]).flatten()

print(similarity)

top_result = 5
max_indx = similarity.argsort()[::-1][:top_result]
print(max_indx)

new_df = df.loc[max_indx]

prompt = f'''You are a Doctor assistant that guide the user of DiagnoScope Organization acoording to the data provided. Data Provided is from Who factsheet on Who website. Here are chunks which have diseases name, disease heading and text realated to disease heading:

{new_df[["disease", "heading", "text"]].to_json(orient="records")}
------------------------------
"{user_input}"
user asked this question related, you have to explain an assist user and answer in human way(don't mention the above format, it is for you). Only provide the answer from the prvided data. You have to be carefull while generating response as it is reagarding health and it may rise serious consern.If user asks unrelated question, tell him that you can only answer questions related to the known disease.The answer should be in detail and use bullet points if neccessary

'''

# prompt = f'''You are a Doctor assistant that guide the user of DiagnoScope Organization acoording to the data provided. Data Provided is from Who factsheet on Who website. Here are chunks which have diseases name, disease heading and text realated to disease heading:

# {new_df[["disease", "heading", "text"]].to_json(orient="records")}
# ------------------------------
# "{user_input}"
# user asked this question related, you have to explain an assist user and answer in human way(don't mention the above format, it is for you). Only provide the answer from the prvided data. You have to be carefull while generating response as it is reagarding health and it may rise serious consern.If severe symptoms are mentioned in the data, include a warning to seek emergency care immediately.If user asks unrelated question, tell him that you can only answer questions related to the known disease

# '''


with open("prompt.txt", "w") as f:
    f.write(prompt)

response = inference(prompt)
print(response)

# with open("response.txt", "w") as f:
#     f.write(response)