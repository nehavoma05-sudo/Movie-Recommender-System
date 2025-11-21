import streamlit as st
import pickle
import requests
from config import API_KEY
st.header("Movie Recommender System")
m=pickle.load(open('movies_list.pkl','rb'))
s=pickle.load(open('similarity_list.pkl','rb'))
list_of_movies=m['title'].values
value=st.selectbox("Select Movie",list_of_movies)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index=m[m['title']==movie].index[0]
    distance=sorted(list(enumerate(s[index])),reverse=True,key=lambda vector:vector[1])
    movies_recommended=[]
    posters_recommended=[]
    for i in distance[0:15]:
        movies_recommended.append(m.iloc[i[0]].title)
        posters_recommended.append(fetch_poster(m.iloc[i[0]].id))
    return movies_recommended,posters_recommended

if st.button("Search"):
    movies_recommended,posters_recommended=recommend(value)
    cols=st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(posters_recommended[i])
            st.text(movies_recommended[i])
    cols=st.columns(5)
    for i in range(5,10):
        with cols[i-5]:
            st.image(posters_recommended[i])
            st.text(movies_recommended[i])
    cols=st.columns(5)
    for i in range(10,15):
        with cols[i-10]:
            st.image(posters_recommended[i])
            st.text(movies_recommended[i])
   
   