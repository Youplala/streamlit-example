import streamlit as st
import pandas as pd
import requests

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
headers = {"Authorization": "Bearer api_OKvBwwcmNPTBaVNmvzmfSrWAmvpJZshtJE"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


st.title('Text emotion detector !')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    output = query({"inputs": text})[0]
    st.subheader('Data')
    li = []
    for out in output:
        li.append([out["label"], out["score"]])

    df = pd.DataFrame(li)
    df.columns = ["Emotion", "Score"]
    st.table(df.assign(hack='').set_index('hack'))
