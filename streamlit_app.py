import streamlit as st
import pandas as pd
import requests

# OMDB API - Add your OMDB API key here
OMDB_API_KEY = '55012f93'  # Replace with your actual OMDB API key

# Load movies, ratings, and links data
def load_data():
    movies = pd.read_csv('ml-latest-small/movies.csv')
    links = pd.read_csv('ml-latest-small/links.csv')
    return movies, links

def load_ratings():
    ratings = pd.read_csv('ml-latest-small/ratings.csv')
    return ratings

# Fetch movie poster using OMDB API and IMDb ID
def fetch_poster_url(imdb_id):
    # Format imdb_id with leading zeros (7 digits)
    imdb_id_str = f"{imdb_id:07d}"
    search_url = f"http://www.omdbapi.com/?i=tt{imdb_id_str}&apikey={OMDB_API_KEY}"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        data = response.json()
        if 'Poster' in data and data['Poster'] != 'N/A':
            return data['Poster']
    return None  # Return None if no poster found or if poster is 'N/A'


# Get movie recommendations
from scipy.spatial.distance import cosine

def get_movie_recommendations(movie_id, ratings_matrix, movies, links, k=5):
    # Get the index of the movie in the DataFrame
    movie_idx = list(ratings_matrix.columns).index(movie_id)
    
    # Create an array to hold the similarities
    movie_similarities = []
    
    # Compute cosine similarities
    for idx in range(ratings_matrix.shape[1]):
        if idx != movie_idx:  # Skip the same movie
            similarity = 1 - cosine(ratings_matrix.iloc[:, movie_idx], ratings_matrix.iloc[:, idx])
            movie_similarities.append((idx, similarity))
    
    # Sort similar movies by similarity
    similar_movies = sorted(movie_similarities, key=lambda x: x[1], reverse=True)
    
    # Get top k recommendations (excluding the selected movie)
    recommendations = []
    for i in similar_movies[:k]:
        recommended_movie_id = ratings_matrix.columns[i[0]]
        movie_title = movies[movies['movieId'] == recommended_movie_id]['title'].values[0]
        
        # Get IMDb ID from links.csv for the recommended movie
        imdbID = links[links['movieId'] == recommended_movie_id]['imdbId'].values[0]
        poster_url = fetch_poster_url(imdbID)  # Fetch poster using IMDb ID
        recommendations.append((movie_title, poster_url, imdbID))
    return recommendations


# Streamlit app
st.title('Movie Recommendation App')

# Load movies, links, and ratings
movies, links = load_data()
ratings = load_ratings()

# Create user-movie matrix
user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Streamlit interface for movie selection
st.subheader('Get movie recommendations')
selected_movie = st.selectbox('Select a movie:', movies['title'])
selected_movie_id = movies[movies['title'] == selected_movie]['movieId'].values[0]

# When user clicks 'Recommend', show recommendations
if st.button('Recommend'):
    recommendations = get_movie_recommendations(selected_movie_id, user_movie_matrix, movies, links)
    
    st.write('Recommended movies:')
    columns = st.columns(len(recommendations))  # Create a column for each recommendation

    for i, (movie, poster_url, imdbID) in enumerate(recommendations):
        with columns[i]:
            if poster_url:
                st.image(poster_url, width=100) 
            st.write(movie)  # Display the movie title below the poster