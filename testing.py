# import library and class
from flask import Flask, render_template

# create flask app
app = Flask(__name__)

# create flask route and action


@app.route('/')
def index():
    return render_template('index.html')


# run flask application
if __name__ == '__main__':
    app.run()
