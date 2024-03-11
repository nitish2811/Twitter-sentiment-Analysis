import pickle
import streamlit as st


est = pickle.load(open('analysis.pkl', 'rb'))
st.title("Twitter sentiment analysis")

tweet=st.text_input("Enter your tweet here")
submit=st.button('Predict')

if submit:
    a=est.predict([tweet])
    st.header(a[0])