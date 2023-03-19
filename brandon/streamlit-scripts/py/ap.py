import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load data
data = pd.read_csv('./archive/movies_metadata.csv')

# Compute similarity matrix
similarities = cosine_similarity(data.iloc[:, 2:])

# Define recommend_movies function


def recommend_movies(title, num_recommendations=5):
    # Get movie index
    idx = data[data['title'] == title].index[0]

    # Get similarity scores
    scores = list(enumerate(similarities[idx]))

    # Sort scores in descending order
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Get top similar movies
    top_movies = [data.iloc[i]['title']
                  for i, s in scores[1:num_recommendations+1]]

    return top_movies


# Set up Streamlit app
st.title('Movie Recommendation App')

# Get user input
movie_title = st.text_input('Enter a movie title', 'The Lion King')

# Get recommended movies
recommended_movies = recommend_movies(movie_title)

# Display recommended movies in Streamlit app
st.write('Recommended movies:')
for i, movie in enumerate(recommended_movies):
    st.write(f"{i+1}. {movie}")
