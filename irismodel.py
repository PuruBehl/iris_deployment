import pickle
import numpy as np
import streamlit as st
from sklearn.tree import DecisionTreeClassifier



# Adding title to the project
st.title("Iris species Detection")

st.markdown("Sepal length :")

sl=st.text_input('1')


st.markdown("Sepal Width :")

sw=st.text_input("2")


st.markdown("Petal Length :")

pl=st.text_input("3")


st.markdown("Petal Width :")

pw=st.text_input("4")


path='C:/Users/PURU/Desktop/Python/Model Deployment/Iris model deployment/models/Tree_model_iris.pkl'

# Loading the model (Decision Tree Model)


flowers=['setose','versicolor','virginica']

if st.button("Get Prediction"):
	model=pickle.load(open(path,'rb'))

	pw=float(pw)

	pl=float(pl)
	sw=float(sw)
	sl=float(sl)



	prediction=model.predict([[sl,sw,pl,pw]])
	answer='The Type of the iris species is :  '+flowers[prediction[0]][0].upper()+flowers[prediction[0]][1:]
	st.info(answer)



