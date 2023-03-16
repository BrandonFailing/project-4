import csv
import pickle
from flask import Flask, render_template, request

# create a dropdown query menu from csv
with open('./dataset/movies-cleaned.csv', 'r') as f:
    reader = csv.DictReader(f)
    data = [row for row in reader]

# load the trained model using a pickle file
# with open('model.pkl', 'rb') as f:
    #model = pickle.load(f)

# create flask app
app = Flask(__name__)

# create a flask route and actions


@app.route('/predict', methods=['POST'])
def predict():
    # get the selected value from the drop-down list
    input_value = request.form['dropdown']

    # make a prediction using the model
    prediction = model.predict(input_value)

    # return the prediction to the HTML page
    return render_template('prediction-result.html', prediction=prediction)
