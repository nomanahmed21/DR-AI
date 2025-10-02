import requests

def create_embeddings(text_list):
    r = requests.post("http://localhost:11434/api/embed", json= {
        "model" : "bge-m3",
        "input": text_list
    })
    return r.json().get('embeddings', [])

def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    return r.json().get('response', '')