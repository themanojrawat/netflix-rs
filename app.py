import pickle
import streamlit as st
import pandas as pd
import requests


def recommendation(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []

    for i in distances[1:6]:

        recommended_movie_names.append(movies.iloc[i[0]].Title)

    return recommended_movie_names
movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Netflix Recommendation System')
selected_movie = st.selectbox(
    'Enter movie/TV show name',
    movies['Title'].values)
if st.button('Show Recommendation'):
    recommended_movie_names = recommendation(selected_movie)
    for i in recommended_movie_names:
        st.write(i)

