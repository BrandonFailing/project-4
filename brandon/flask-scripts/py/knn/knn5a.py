# Create a Flask app and import the necessary modules:
from flask import Flask, render_template, request
import csv
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the dataset
data = pd.read_csv('./dataset/u-r1-movies-reordered.csv')

# Transform the data into a pivot table
pivot = data.pivot_table(
    index='name', columns='user_id', values='rating').fillna(0)

# Train the model using the pivot table
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(pivot)

# Create a Flask route to display a dropdown list of movies CSV column.
app = Flask(__name__)


@app.route('/')
def index():
    movies = pd.read_csv('./dataset/u-movie-list.csv')['name'].tolist()
    return render_template('index.html', movies=movies)

# Create a Flask route that will generate movie recommendations based on the selected movie.


@app.route('/recommendations', methods=['POST'])
def recommendations():
    input_movie = request.form['movie']
    # Get the user_id that rated the selected movie
    user_id = data.loc[data['name'] == input_movie]['user_id'].iloc[0]
    # Get the list of movies rated by the user
    user_ratings = data.loc[data['user_id'] == user_id]
    # Get the movies similar to the selected movie
    if input_movie in pivot.index:
        movie_idx = pivot.index.get_loc(input_movie)
        if movie_idx >= 0 and movie_idx < len(pivot.index):
            distances, indices = model.kneighbors(
                pivot.iloc[movie_idx, :].values.reshape(1, -1), n_neighbors=10)
            similar_movies = []
            for i in range(len(distances[0])):
                if i == 0:
                    continue
                else:
                    movie_title = pivot.index[indices[0][i]]
                    similar_movies.append(movie_title)
            # Get the list of movies rated by the user that are similar to the selected movie
            recommended_movies = []
            for movie in similar_movies:
                if len(recommended_movies) == 0:
                    recommended_movies.append(movie)
                else:
                    # Get the rating of the similar movie by the same user
                    rating = user_ratings.loc[user_ratings['name']
                                              == movie]['rating'].iloc[0]
                    # Check if the movie has not already been recommended and has a higher rating than the selected movie
                    if movie not in recommended_movies and rating > user_ratings.loc[user_ratings['name'] == input_movie]['rating'].iloc[0]:
                        recommended_movies.append(movie)
                if len(recommended_movies) == 3:
                    break
            return render_template('index.html', recommended_movies=recommended_movies)
    else:
        return render_template('index.html', error_message="The selected movie is not in the dataset.")


if __name__ == '__main__':
    app.run(debug=True)
