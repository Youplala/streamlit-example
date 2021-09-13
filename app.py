import streamlit as st

from transformers import pipeline
classifier = pipeline("text-classification",model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)


st.title('Hello World!')

form = st.form(key='my_form')
text = form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    prediction = classifier(text, )
    st.subheader('Data')
    st.write({"text": prediction})
