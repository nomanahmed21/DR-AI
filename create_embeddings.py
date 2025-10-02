import pandas as pd
import joblib
import requests
import json 

# function for Creating embeddings for "data.json"
def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json= {
        "model" : "bge-m3",
        "input": text_list
    })
    return r.json()['embeddings'] 

# Reading "data.json"
with open("data.json", "r") as f:
    data =json.load(f)

my_dict = []
chunk_id = 0

# creating embeddings 
embeddings = create_embeddings([chunks["text"] for chunks in data])

# adding embedding to single chunk and appending all chunks to list 
for i,chunk in enumerate(data):
    chunk["chunk_id"] = chunk_id
    chunk["embedding"] = embeddings[i]
    chunk_id +=1
    my_dict.append(chunk)
print(my_dict)

# Creating DataFrame of the list of chunks
df = pd.DataFrame.from_records(my_dict)
print(df)

# saving the DataFrame in joblib file
joblib.dump( df,"data_embeddings.joblib")