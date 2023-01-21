import streamlit as st

st.write("""
# TDS week 8 assignnment
## For the Division of two given numbers using streamlit and deploying on Heroku
""")
#Get Input
st.header('Input two numbers')

a= st.number_input('Enter first number')
b= st.number_input('Enter second number')
Division= a/b 

st.write('The Division of given numbers is', Division)
st.write('By Kanika Maheshwari (22ds1000263)')

