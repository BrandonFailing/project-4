<h1 align="center">Project 4: Movie Recommender Web App</h1)
<br>
<p>
<p align="center">
<img src= "https://cdn.technadu.com/wp-content/uploads/2017/12/Create-a-library-in-kodi-Featured.jpg">  
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
<li>Scikit Count Vectorizer
<li>Scikit Cosime Similarity 
<li>Scikit TL-IDF Vectorizer
<li>NLTK Snowball Stemmer
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
<li>Download the data from Grouplens</li>
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
<ol>
<li>Load dataset to AWS S3</li>
</ol>
  
<li>Visualize Database Diagram
<ol>
<li>Create a diagram database using QuickDBD</li>
</ol>
  
<li>Feature Extraction
<ol>
<li>Processes dataset using PySpark</li>
<li>Load tags data, and drop all tags under 80% relevance</li>
<li>Combine all tags for each movie into a single value
<li>Load ratings data</li>
<li>Calculate average ratings and ratings count for each movie</li>
<li>Assign average ratings and ratings counts to categories to be 
used in text analysis</li>
<li>Load movies data</li>
<li>Extract year from title and strip delimiter from genres</li>
<li>Combine tags, average rating category, ratings count category, 
year, and genres into a single text column for analysis.</li>
</ol>
  

<li>Create Model
<ol>
<li>Using Scikit Count Vectorizer</li>
<ol>
<li>Create count matrix using Count Vectorizer to create 
feature vectors</li>
<li>Calculate cosine similarity</li>
<li>Create input variable with movie</li>
<li>Extract and print ten most similar movies to input movie</li>
</ol>
<li>Using Count Vectorizer after being stemmed
<ol>
<li>Use NLTK Snowball Stemmer to stem combined text 
column</li>
<li>Repeat steps above</li>
<li>The stemmed text provides slightly higher similarity 
scores, and a different set of recommendations</li>
</ol>
<li>Using a TF-IDF vector
<ol>
<li>Use stemmed field for analysis, and use Scikit TL-IDF 
Vectorizer to create feature vector</li>
<li>Repeat calculating cosine similarity and finding ten most 
similar movies to input movie</li>
<li>There is no significant difference between the Count
Vectorizer and TL-IDF Vectorizer after stemming text field</li>
</ol>
  </ol>

  
<li>Recommendation model
<ol>
<li>Build a recommendation model using Flask app</li>
<li>Create the Machine Learning model using count vectorizer</li>
<ol>
<li>Construct count vectorizer matrix by fitting and 
transforming data</li>
<li>Construct cosine similarity matrix</li>
</ol>

<li>Create a Get Recommendations function
<li>Run the Flask app</li>
<li>Create a web page for the movie recommender using HTML and CSS </li>
<li>Return HTML through Python script using the flask render_template method </li>
<li>Create a movie-found.html that would render similar movie recommendations </li>
 <li>Create a movie-not-found.html that would return <strong>"Error, movie("NAME")"</strong> not found if no movie recommendations are found </li>
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

- [X] The model optimization and evaluation process showing iterative changes made to the model and the resulting changes in model performance is documented in either a CSV/Excel table or in the Python script itself (15 points)

- [X] Overall model performance is printed or displayed at the end of the script (10 points)

<b>GitHub Documentation (25 points)</b>

- [X] GitHub repository is free of unnecessary files and folders and has an appropriate .gitignore in use (10 points)

- [X] The README is customized as a polished presentation of the content of the project (15 points)

<b>Group Presentation (25 points)</b>
- [X] All group members speak during the presentation. (5 points)

- [X] Content, transitions, and conclusions flow smoothly within any time restrictions. (5 points)

- [X] The content is relevant to the project. (10 points)

- [X] The presentation maintains audience interest. (5 points)


