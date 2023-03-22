<h1 align="center">Project 4: Movie Recommender Web App</h1)
<br>
<p>
<p align="center">
<img src=https://cdn.technadu.com/wp-content/uploads/2017/12/Create-a-library-in-kodi-Featured.jpg>
<h2 align="center">Team 1: Edith Lotterman, Chloe Li, Brandon Failing and Wei Kent Chen</h2></center>
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
<li>Download the data from movie lens</li>
</ol>
<ol>
<li>Compile the csv files with movie Id, title, user assigned tags, unique tag, ratings, genome scores, and imdb/tmdb score</li>
</ol>  
<li>Data Pre-processing 
<ol>
<li>Identify disrepancies</li>
</ol>
<ol>
<li>Replace and eliminate duplicate data</li>
</ol>
<ol>
<li>Remove missing data</li>
</ol>
<ol>
<li>Merge and adjusting data using pandas</li>
</ol>
<li>Visualize Database Diagram
<ol>
<li>Create a diagram database using QuickDBD</li>
</ol>
<li>Feature Extraction
<ol>
<li>Extract relevant features from the pre-processed data and create a set of features that will be used to create movie profiles</li>
<li>Train the recommendation model</li>
</ol>
<li>Load Dataset to AWS S3
<ol>
<li>Processed dataset using PySpark </li>
<li>Calculate and analyze the dataset</li>
<li>Drop all tagId under 80% significance </li>
<li>Load tags data and join tags into dataframe for use in model</li>
<li>Combine all tags for each movie into a single value </li>
<li>Load all other relevant data(ratings, genre, title_date, title</li>
<li>Clean the data and analyze the data, replacing null value</li>
<li>Combine the dataset into a single data frame</li>
</ol>
<li>Create Model and visualize:
<ol>
<li>As a count vector </li>
<li>A count vector after being stemmed </li>
<li>A TF-IDF vector</li>
</ol>
<li>Recommendation model
<ol>
<li>Build a recommendation model using the clustered data</li>
<li>This project utilize Content-Based Filtering model</li>
<li>Deploy the model on the web application using Flask and HTML</li>
</ol>
<li>Deploy the model 
<ol>
<li>Deploy the model(web application)</li>
<li>Test the web application to ensure that it works</li>
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


