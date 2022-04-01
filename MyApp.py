import streamlit as st
st.title("MI PRIMER APP")
click=st.button("Dale click")
st.write("el valor de click es: ",click)
if click==True:
    st.image("https://media.istockphoto.com/photos/maltese-dog-puppy-picture-id961585286?k=20&m=961585286&s=612x612&w=0&h=9pNSBbt1WWTUXRHqzT57FEfh7WoAuWFGIqgLNikwty0=")
import pandas as pd 

#Las siguientes tres lineas eran del primer ejercicio
#df = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
#st.write(df)
#st.map(df)

#st.write("Holaa")
st.text("La siguiente es una integral")
st.latex(" \int ")
st.markdown(" *titulo ")
st.markdown(" **Esta es una viñeta** ")
