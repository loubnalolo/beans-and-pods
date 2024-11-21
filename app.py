import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Application d'Analyse des Données : Beans and Pods")


st.sidebar.header("Importer le Dataset")


data = pd.read_csv("C:/Users/GK/Desktop/Projet 2/beans-and-pods/BeansDataSet.csv")


st.subheader("Aperçu des Données")
st.write(data.head())


st.subheader("Statistiques Descriptives")
st.write(data.describe())


st.subheader("Nuage de Points")


col_x = st.selectbox("Choisissez la colonne pour l'axe X", data.columns)
col_y = st.selectbox("Choisissez la colonne pour l'axe Y", data.columns)


if st.button("Afficher le Nuage de Points"):
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=col_x, y=col_y, ax=ax)
    st.pyplot(fig)


st.subheader("Histogramme")


col_hist = st.selectbox("Choisissez une colonne pour l'Histogramme", data.columns)


if st.button("Afficher l'Histogramme"):
    fig, ax = plt.subplots()
    sns.histplot(data[col_hist], kde=True, ax=ax)
    st.pyplot(fig)



    

