import streamlit as st
import pandas as pd
import os
import requests
from dotenv import load_dotenv

# Load HuggingFace API
load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
headers = {"Authorization": "Bearer " + os.getenv('API_KEY')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


# Display form

st.title('Text emotion detector !')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

# 

if submit_button:
    try:
        output = query({"inputs": text})[0]
        st.subheader('Data')
        li = []
        for out in output:
            li.append([out["label"], out["score"]])
        df = pd.DataFrame(li)
        df.columns = ["Emotion", "Score"]
        df = df.sort_values(ascending=False, by="Score")
        st.table(df.assign(hack='').set_index('hack'))
    except:
        st.write("Model is loading, please try again later")