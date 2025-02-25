import dotenv
import requests
import streamlit as st

api_key = dotenv.get_key('.env', 'API_KEY')
url = dotenv.get_key('.env', 'URL')
response = requests.get(f'{url}?api_key={api_key}').json()
date = response['date']
title = response['title']
explanation = response['explanation']
img_url = response['url']

st.title(title)
st.image(img_url)
st.text(explanation)
