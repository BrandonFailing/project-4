<h1 align="center">Project 4: Movie Recommender Web App</h1)
<br>
<p>
<p align="center">
<img src=/assets/movie-recommender-header.jpg>
<h2 align="center">Team 1: Edith Lotterman, Chloe Li, Brandon Failing and Wei Kent Chen</h2></center>
</p>
<br>
<p>
Core Pages: <br>

https://brandonfailing.github.io/project-4/index.html <br>
https://brandonfailing.github.io/project-4/templates/index.html <br>
https://brandonfailing.github.io/project-4/templates/prediction-form.html <br>
https://brandonfailing.github.io/project-4/templates/prediction-result.html <br>
</p>
<br>
<p>
<h1>Project Overview</h1>

Our project is to create a flask based movie recommedation web app that uses a machine learning model to predict similar movie recommendations from a list of user selected movies<p>

<h3>Software:</h3>
<ul>
<li>Python
<li>VSCode
</ul>
<h3>Python Libraries:</h3>
<ul>
<li>Pandas
<li>Numpy
<li>Scikit
<li>Flask
<li>PySpark
</ul>
<h3>Unsupervised Machine Learning:</h3>
<ul>
<li>Javascript
<li>Chart.JS
</ul>
<h3>Web App:</h3>
<ul>
<li>HTML
<li>Javascript
<li>CSS
<li>Flask
</ul>
</p>
<br>
<p>
<h1>Steps</h1>
<ol>
<li>Load the Data
<ol>
<li>Download the data</li>
</ol>
<li>Data Pre-processing 
<ol>
<li>Clean the data(Remove duplicates and missing values)</li>
</ol>
<li>Feature Extraction
<ol>
<li>Extract relevant features from the pre-processed data and create a set of features that will be used to create movie profiles</li>
<li>Train the recommendation model</li>
</ol>
<li>Dimensionality reduction
<ol>
<li>Use Principal Component Analysis(PCA) to reduce the dimensionality of the feature space</li>
<li>This will help iprove efficiency and accuracy of the recommendation model</li>
</ol>
<li>Clustering
<ol>
<li>Use unsupervised clustering to group similar movies together based on extracted features</li>
</ol>
<li>Recommendation model
<ol>
<li>Build a recommendation model using the clustered data</li>
<li>This project utilize Content-Based Filtering model</li>
</ol>
<li>Deploy the model 
<ol>
<li>Deploy the model on the web application</li>
</ol>
</p>
<br>
<p>
<h1>Requirements (Grading Rubric)</h1>
<b>Data Model Implementation (25 points)</b>

- [X] A Python script initializes, trains, and evaluates a model (10 points)

- [X] The data is cleaned, normalized, and standardized prior to modeling (5 points)

- [X] The model utilizes data retrieved from SQL or Spark (5 points)

- [X] The model demonstrates meaningful predictive power at least 75% classification accuracy or 0.80 R-squared. (5 points)

<b>Data Model Optimization (25 points)</b>

- [ ] The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)

- [ ] Overall model performance is printed or displayed at the end of the script (10 points)

<b>GitHub Documentation (25 points)</b>

- [X] GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)

- [X] The README is customized as a polished presentation of the content of the project (15 points)

<b>Group Presentation (25 points)</b>
- [X] All group members speak during the presentation. (5 points)

- [X] Content, transitions, and conclusions flow smoothly within any time restrictions. (5 points)

- [X] The content is relevant to the project. (10 points)

- [X] The presentation maintains audience interest. (5 points)


