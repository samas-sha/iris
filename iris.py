import streamlit as st
import numpy as np
import pickle

with open("model.pickle","rb") as f :
    model = pickle.load(f)

st.title("iris species prediction app")
sepal_length = st.number_input("sepal legth",0.0,10.0,5.0)
sepal_width = st.number_input("sepal width",0.0,10.0,5.0)
petal_length = st.number_input("petal length",0.0,10.0,5.0)
petal_width = st.number_input("petal width",0.0,10.0,5.0)
predict = st.button("predict species")

if predict:
    input_data = np.array([[sepal_length,sepal_width,petal_length,petal_width]])

    prediction = model.predict(input_data)

    species=["setosa","yersicolor","virginica"]
    st.success("predicted species is ",species[prediction[0]])