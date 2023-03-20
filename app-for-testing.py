# Create a Flask app and import the necessary modules:
import flask
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = flask.Flask(__name__, template_folder='templates')

data = pd.read_csv('./edith/final-testing.csv')

tfidf = TfidfVectorizer(stop_words='english', analyzer='word')

# Construct the TF-IDF matrix by fitting & transforming the data
tfidf_matrix = tfidf.fit_transform(data['soup'])
print(tfidf_matrix.shape)

# Construct cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim.shape)

data = data.reset_index()
indices = pd.Series(data.index, index=data['title']).drop_duplicates()

# Create array with all movie titles
all_titles = [data['title'][i] for i in range(len(data['title']))]


def get_recommendations(title):
    global sim_scores
    # Get the index of the movie that matches the title
    idx = indices[title]
    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:11]
    # print similarity scores
    print("\n movieId      score")
    for i in sim_scores:
        print(i)

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # return list of similar movies
    return_df = pd.DataFrame(columns=['Title', 'Homepage'])
    return_df['Title'] = data['title'].iloc[movie_indices]
    return_df['Homepage'] = data['homepage'].iloc[movie_indices]
    return_df['ReleaseDate'] = data['release_date'].iloc[movie_indices]
    return return_df

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
            homepage = []
            releaseDate = []
            for i in range(len(result_final)):
                names.append(result_final.iloc[i][0])
                releaseDate.append(result_final.iloc[i][2])
                if(len(str(result_final.iloc[i][1])) > 3):
                    homepage.append(result_final.iloc[i][1])
                else:
                    homepage.append("#")

            return flask.render_template('movie-found.html', movie_names=names, movie_homepage=homepage, search_name=m_name, movie_releaseDate=releaseDate, movie_simScore=sim_scores)


# Run Flask app w/ debugging.
if __name__ == '__main__':
    app.run(debug=True)
