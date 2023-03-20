# ## Bring in initial dependencies
from pyspark.sql import SparkSession
import pandas as pd
from pyspark import SparkFiles
import findspark
import os
# Find the latest version of spark
# spark_version = 'spark-3.2.2'
spark_version = 'spark-3.2.3'
os.environ['SPARK_VERSION'] = spark_version
# Install Spark and Java
!apt-get update
!apt-get install openjdk-8-jdk-headless - qq > /dev/null
!wget - q http: // www.apache.org/dist/spark /$SPARK_VERSION /$SPARK_VERSION-bin-hadoop2.7.tgz
!tar xf $SPARK_VERSION-bin-hadoop2.7.tgz
!pip install - q findspark
# Set Environment Variables
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = f"/content/{spark_version}-bin-hadoop2.7"
# Start a SparkSession
findspark.init()

# %%
#import dependencies

# %%
# Start Spark session
spark = SparkSession.builder.appName("movieRecommender").getOrCreate()

# %% [markdown]
# ## Bring in data from .csv's and join

# %%
# Load in genome score data
url = "https://movie-lens-data-p4t1.s3.amazonaws.com/genome-scores.csv"
spark.sparkContext.addFile(url)
gs_df = spark.read.csv(SparkFiles.get("genome-scores.csv"),
                       sep=",", header=True, inferSchema=True)
gs_df.show()

# %%
# drop all tags under 80% significance
relevant_tags = gs_df.filter(gs_df['relevance'] >= .80)

# %%
# Load in tags data
url = "https://movie-lens-data-p4t1.s3.amazonaws.com/genome-tags.csv"
spark.sparkContext.addFile(url)
tags_df = spark.read.csv(SparkFiles.get(
    "genome-tags.csv"), sep=",", header=True, inferSchema=True)
tags_df.show()

# %%
# Join tags into dataframe for use in model, drop tagID and relevance as they are no longer needed
join_tags = relevant_tags.join(tags_df, ['tagID'], 'left')
join_tags = join_tags.drop('tagId', 'relevance')
rows = join_tags.count()
print(f'{rows}')

# %%
# Change to pandas dataframe for more transformation
pd_tags = join_tags.toPandas()
pd_tags.head()

# %%
# combine all tags for each movie into a single value
grouped_tags = pd_tags.groupby('movieId')['tag'].transform(
    lambda x: ' '.join(map(str, x)))
pd_tags = pd.merge(pd_tags, grouped_tags, left_index=True, right_index=True)
pd_tags = pd_tags.drop('tag_x', axis=1)
pd_tags = pd_tags.drop_duplicates()
pd_tags = pd_tags.rename(columns={'tag_y': 'tag'})
pd_tags.head()
# pd_tags.dtypes

# %%
# bring in ratings data
url = "https://movie-lens-data-p4t1.s3.amazonaws.com/ratings.csv"
spark.sparkContext.addFile(url)
ratings_df = spark.read.csv(SparkFiles.get(
    "ratings.csv"), sep=",", header=True, inferSchema=True)
ratings_df.show()

# %%
# find the average ratings for each movie
ratings_avg = ratings_df.groupBy('movieID').avg('rating')

# %%
# find how many people have reviewed each movie
ratings_count = ratings_df.groupBy('movieID').count()
ratings_count = ratings_count.withColumnRenamed('count', 'ratings_count')

# %%
# join new ratings fields
ratings_join = ratings_count.join(ratings_avg, ['movieID'])
rows = ratings_join.count()
print(f'{rows}')

# %%
pd_ratings = ratings_join.toPandas()
pd_ratings.dropna(inplace=True)
pd_ratings.head()

# %%
# Look at ratings counts to create classification
pd_ratings['ratings_count'].value_counts()
pd_ratings.dtypes

# %%
# rename avg(rating) column
pd_ratings.rename({'avg(rating)': 'avg_rating'}, axis=1, inplace=True)
pd_ratings.head()

# %%
ratings_count_cat = pd.cut(pd_ratings.ratings_count, bins=[0, 100, 500, 1000, 5000, 50000], labels=[
                           'under one hundred', 'under five hundred', 'under one thousand', 'under five thousand', 'over five thousand'])
pd_ratings['ratings_count_category'] = ratings_count_cat
pd_ratings.head()

# %%
# Change number to classification bins
avg_ratings_cat = pd.cut(pd_ratings.avg_rating, bins=[0, .75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5], labels=[
                         '1/2 star', '1 star', '1 1/8 star', ' 2 stars', '2 1/2 stars', '3 stars', '3 1/2 stars', '4 stars', ' 4 1/2 stars', ' 5 stars'])
pd_ratings['avg_ratings_category'] = avg_ratings_cat
pd_ratings.head()

# %%
# Join tags and ratings dataframes
tags_ratings_df = pd.merge(
    pd_tags, pd_ratings, left_on="movieId", right_on="movieID")
tags_ratings_df = tags_ratings_df.drop('movieID', axis=1)
tags_ratings_df.head()
tags_ratings_df.dtypes


# %%
# Change categories to strings and replace NaN with empty string
tags_ratings_df = tags_ratings_df.astype(
    {'ratings_count_category': 'string', 'avg_ratings_category': 'string'})
tags_ratings_df[['ratings_count_category', 'avg_ratings_category']] = tags_ratings_df[[
    'ratings_count_category', 'avg_ratings_category']].fillna('')
tags_ratings_df.dtypes
tags_ratings_df.head()

# %%
# Load in movie data
url = "https://movie-lens-data-p4t1.s3.amazonaws.com/movies.csv"
spark.sparkContext.addFile(url)
movie_df = spark.read.csv(SparkFiles.get(
    "movies.csv"), sep=",", header=True, inferSchema=True)
movie_df.show()

# %%
# Convert movies to pandas for further processing
pd_movies = movie_df.toPandas()
pd_movies.head()
# pd_movies.dtypes

# %%
# remove pipe delimiter freom genres
pd_movies['genres'] = pd_movies['genres'].str.split('|')
pd_movies['genrestring'] = [','.join(map(str, l)) for l in pd_movies['genres']]
pd_movies = pd_movies.drop('genres', axis=1)
pd_movies.head()

# %%
#  Split year from title
pd_movies['title_date'] = pd_movies['title'].str.split(
    '(').str[1].str.replace(')', '')
pd_movies.head()
# pd_movies.dtypes

# %%
#  Change year to string and fill all NaN
pd_movies['title_date'] = pd_movies['title_date'].astype(str)
pd_movies['title_date'] = pd_movies['title_date'].fillna('')
pd_movies.dtypes
# tags_ratings_df.head()

# %%
# Combine movies dataframe into tags_ratings dataframe for analysis
final = pd.merge(pd_movies, tags_ratings_df)
# final.head()
# Write the resulting dataframe to a new CSV file
final.to_csv('./edith/testing/final.csv', index=False)
