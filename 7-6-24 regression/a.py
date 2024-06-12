import pandas as pd;
import streamlit as st;
import joblib;

model = joblib.load('model_joblib')
st.title("House price prediction")
 

area = st.number_input("enter the area")
def prediction(area):
    p = model.predict([[area]])
    return p 

if(st.button("predict")):
    result = prediction(area)
    st.success("The predicted price is {}".format(result))

    