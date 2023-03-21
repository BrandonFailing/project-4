# Create a Flask app and import the necessary modules:
import flask
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = flask.Flask(__name__, template_folder='templates')

data = pd.read_csv('./model/final.csv')

# Create model
cv = CountVectorizer()

# Construct the count vectorizer matrix by fitting & transforming the data
count_matrix = cv.fit_transform(data['combined_text'])
print("Count Matrix:", count_matrix.toarray())

# Construct cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix)

# Create array with all movie titles
all_titles = [data['title'][i] for i in range(len(data['title']))]


def get_recommendations(title):
    # Get the index of the movie that matches the title
    movie_index = data[data.title == title].index.values[0]
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[movie_index]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    # Create returns_df for use in app route
    name_list = []

    for movie in movie_indices:
        name = data[data.index == movie]["title"].values[0]
        name_list.append(name)

    returns_df = pd.DataFrame(name_list, columns=['Title'])
    return returns_df

# Set up the main route


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('index.html'))

    if flask.request.method == 'POST':
        m_name = " ".join(flask.request.form['movie_name'].split())
        if m_name not in all_titles:
            return(flask.render_template('movie-not-found.html', name=m_name))
        else:
            result_final = get_recommendations(m_name)
            names = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])

            return flask.render_template('movie-found.html', movie_names=names, search_name=m_name)


# Run Flask app w/ debugging.
if __name__ == '__main__':
    app.run(debug=True)
