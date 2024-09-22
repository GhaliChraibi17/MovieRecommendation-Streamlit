# Movie Recommendation System

This is a **Streamlit-based Movie Recommendation System** that uses the MovieLens dataset and integrates with the **OMDB API** to fetch movie posters and plots. The app provides personalized movie recommendations based on user-selected movies.

![App Demo](./App%20Demo.png)

## Setup Running the Movie Recommendation App with Docker

Start by cloning the git repository ```git clone https://github.com/GhaliChraibi17/MovieRecommendation-Streamlit```

Once you're in the root directory of the project (where the `Dockerfile` is located). Run the following commands to build the Docker image and run the container for launching the app:

```docker build -t movie-recommendation-app .```
```docker run -p 8501:8501 movie-recommendation-app```


## Features

- **Movie Selection**: Choose from a list of movies to get recommendations.
- **Recommendations**: The app provides five movie recommendations based on cosine similarity of user ratings from the MovieLens dataset. This system uses a user-based collaborative filtering approach, which means that recommendations are generated by finding similarities between users' rating behaviors. The basic idea is that if two users have rated many movies similarly, they are likely to have similar tastes. The system computes the similarity between users based on the ratings they have given to different movies. Once a similar user or group of users is identified, the system recommends movies that those similar users have liked but that the current user hasn't rated yet.

![Collaborative Filtering](./Collaborative%20Filtering.png)

- **Movie Details**: Each recommended movie displays a poster and can be expanded to show the movie's plot fetched from the OMDB API.
- **Streamlit Interface**: A clean and responsive interface powered by Streamlit.

## Dataset

The app uses the **MovieLens 'ml-latest-small' dataset**, which contains:

- Movies metadata (title, genre)
- Ratings data from users
- Links to IMDb and TMDb for each movie

You can download the dataset from [MovieLens](https://grouplens.org/datasets/movielens/latest/) and find more information inside the data folder.
