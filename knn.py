# 1) Import necessary libraries: To begin, you'll need to import the necessary libraries to read in your CSV file and build your nearest neighbor model. The most commonly used libraries for this purpose are Pandas, NumPy, and Scikit-Learn. You can use the following code to import them:
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


# 2) Load the CSV data: Next, you'll need to load your CSV data into a Pandas dataframe. You can use the read_csv() function to accomplish this. Here's an example code to read a CSV file named data.csv:
data = pd.read_csv('./dataset/u-r1-movies-reordered.csv')

# 3) Prepare the data: Before building the model, you'll need to prepare the data. This involves separating the features and the target variable. In addition, you'll need to split the data into training and testing sets. Here's an example code to accomplish this:

# Use all columns as features
X = data
# Extract the target variable column
y = data['name']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 4) Build the model: Once you've prepared the data, you can build the nearest neighbor model using the KNeighborsClassifier class from Scikit-Learn. Here's an example code to build a model with k=5 neighbors:

# Create a KNN classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
# Fit the model to the training data
knn.fit(X_train, y_train)

# 5) Evaluate the model: Finally, you can evaluate the performance of the model by making predictions on the test data and comparing the predicted values to the actual values. You can use the accuracy_score() function from Scikit-Learn to calculate the accuracy of the model. Here's an example code to do this:

# Make predictions on the test data
y_pred = knn.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# 6) Save the training data to a CSV file
#train_data = pd.concat([X_train, y_train], axis=1)
#train_data.to_csv('./dataset/trained_data.csv', index=False)

# 7) Save the training data to a Pickle  file
with open('./dataset/model-r1.pkl', 'wb') as f:
    pickle.dump(knn, f)
