import streamlit as st
from utils.api import create_embeddings, inference
from utils.search import SearchEngine
import joblib

df = joblib.load("data_embeddings.joblib")
search_engine = SearchEngine(df)

st.title("DR. AI") 
st.write("Ask Question Related TO Cholera, Cancer, Malaria, Covid-19, Rabies")

user_input = st.text_input("Enter your question:")

with st.spinner("Generating Answer..."):
    question_embedding = create_embeddings([user_input])[0]

    new_df = search_engine.find_top_matches(question_embedding)

    prompt = f'''You are a Doctor assistant that guide the user of DiagnoScope Organization acoording to the data provided. Data Provided is from Who factsheet on Who website. Here are chunks which have diseases name, disease heading and text realated to disease heading:

    {new_df[["disease", "heading", "text"]].to_json(orient="records")}
    ------------------------------
    "{user_input}"
    user asked this question related, you have to explain an assist user and answer in human way(don't mention the above format, it is for you). Only provide the answer from the prvided data. You have to be carefull while generating response as it is reagarding health and it may rise serious consern.If user asks unrelated question, tell him that you can only answer questions related to the known disease.The answer should be in detail and use bullet points if neccessary

    '''
    response = inference(prompt)

    st.subheader("Answer:")
    st.write(response)
