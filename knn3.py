import pandas as pd
from flask import Flask, render_template, request
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load the dataset
movies = pd.read_csv('./dataset/u-r1-movies-reordered.csv',
                     usecols=['movieId', 'name', 'user_id', 'rating', 'timestamp'])
movie_list = pd.read_csv('./dataset/u-movie-list.csv', usecols=['name'])

# Fit the KNN model
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
knn_model.fit(X=movies.pivot_table(
    index='name', columns='user_id', values='rating').fillna(0))


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_movie = request.form['input_movie']
        distances, indices = knn_model.kneighbors(X=movies.pivot_table(
            index='name', columns='user_id', values='rating').loc[input_movie].values.reshape(1, -1), n_neighbors=5)
        recommended_movies = [movies.loc[movies['name'] == movie]['name'].iloc[0]
                              for movie in movies.loc[indices.flatten()]['name'].unique()]
        return render_template('index.html', recommended_movies=recommended_movies)
    return render_template('index.html', movie_list=movie_list['name'].values)


if __name__ == '__main__':
    app.run(debug=True)
