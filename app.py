import streamlit as st
import numpy as np

st.title("""
Division of two given numbers 
""")
#Get Input
st.header('Input two numbers')

a= st.number_input('Enter first number')
b= st.number_input('Enter second number')
if b==0.0:
  print('Zero error')
else:
  Division= np.divide(a,b)
  st.write('The Division of given numbers is', Division)
st.write('By Kanika Maheshwari')

