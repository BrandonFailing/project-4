import csv
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load the dataset
data = pd.read_csv('./dataset/u-r1-movies-reordered.csv')

# Transform the data into a pivot table
pivot = data.pivot_table(
    index='name', columns='user_id', values='rating').fillna(0)

# Train the model using the pivot table
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(pivot)

# Choose a movie name
input_movie = 'Toy Story (1995)'

# Find the index of the input movie name
movie_idx = pivot.index.get_loc(input_movie)

# Get the distances and indices of the nearest neighbors
distances, indices = model.kneighbors(
    pivot.iloc[movie_idx, :].values.reshape(1, -1), n_neighbors=10)

# Loop through the nearest neighbors and find a movie that is similar but different
for i in range(len(distances.flatten())):
    if i == 0:
        print(f"Recommendations for {input_movie}:")
    else:
        print(
            f"{i}: {pivot.index[indices.flatten()[i]]} (distance: {distances.flatten()[i]})")
        break
