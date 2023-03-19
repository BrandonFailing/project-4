from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load the machine learning model
with open("./dataset/model-r1.pkl", "rb") as f:
    model = pickle.load(f)

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("./dataset/u-r1-movies-reordered.csv",
                 usecols=["name", "movieId"])

# Drop the "movieId" column
df.drop("movieId", axis=1, inplace=True)

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage


@app.route("/")
def index():
    # Get a list of all the names in the DataFrame
    names = sorted(list(set(df["name"])))

    # Render the template with the names list
    return render_template("index.html", names=names)

# Define a route for the prediction result page


@app.route("/predict", methods=["POST"])
def predict():
    # Get the user's selection from the form
    name = request.form["name"]

    # Get the subset of the DataFrame with only the selected name
    subset = df[df["name"] == name]

    # Make a prediction using the machine learning model
    X = subset
    y_pred = model.predict(X)

    # Format the prediction as a string
    prediction = f"The predicted value for {name} is {y_pred[0]:.2f}."

    # Render the template with the prediction result
    return render_template("predict.html", name=name, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
