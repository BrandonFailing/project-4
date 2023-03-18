# Create a Flask app and import the necessary modules:
from flask import Flask, render_template, request
import csv
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the dataset and create a pivot table:
data = pd.read_csv('./dataset/u-r1-movies-reordered.csv')
pivot = data.pivot_table(
    index='name', columns='user_id', values='rating').fillna(0)

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
    movie_idx = pivot.index.get_loc(input_movie)
    model = NearestNeighbors(metric='cosine', algorithm='brute')
    model.fit(pivot)
    distances, indices = model.kneighbors(
        pivot.iloc[movie_idx, :].values.reshape(1, -1), n_neighbors=10)
    recommendations = []
    for i in range(len(distances[0])):
        if i == 0:
            continue
        else:
            movie_title = pivot.index[indices[0][i]]
            recommendations.append(movie_title)
            return render_template('recommendations.html', recommendations=recommendations)


if __name__ == '__main__':
    app.run(debug=True)
