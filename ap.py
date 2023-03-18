import csv
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the machine learning model from the pickle file
with open('./dataset/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the home route that displays the prediction form


@app.route('/', methods=['GET'])
def home():
    with open('./dataset/movies-cleaned.csv', 'r') as f:
        reader = csv.DictReader(f)
        movies = [row for row in reader]

    return render_template('./templates/prediction-form.html', movies=movies)

# Define the prediction route that makes a prediction based on the user's selection


@app.route('/predict', methods=['POST'])
def predict():
    selected_movie = request.form.get('dropdown')

    # Perform some preprocessing on the user's selection
    # ...
    # Call the machine learning model to make a prediction
    prediction = model.predict(selected_movie)

    return render_template('./templates/prediction-result.html', prediction=prediction)


if __name__ == '__main__':
    app.run()
