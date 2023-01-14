import pickle
import streamlit as st
import requests
import pandas as pd



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
#patoolib.extract_archive("similarity.rar", outdir=os. getcwd())
def recommend(movie):
    movie_lower = movie
    index = movies[movies['title'] == movie_lower].index[0]
    distances = list(similarity[index])
    L=[]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in range(6):
        movie_id = movies["movie_id"].iloc[distances.index(max(distances))]
        L.append(distances.index(max(distances)))
        recommended_movie_posters.append(fetch_poster(movie_id))
        distances[distances.index(max(distances))] = 0
    for i in L:
        recommended_movie_names.append(movies['title'][i])
    recommended_movie_names=recommended_movie_names[1:]
    recommended_movie_posters =recommended_movie_posters[1:]
    return recommended_movie_names, recommended_movie_posters
        


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movie_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl",'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])





