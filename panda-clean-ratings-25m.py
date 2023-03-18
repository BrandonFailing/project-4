import csv
import pandas as pd


def clean_csv(input_file, output_file):
    # Read the csv file
    df = pd.read_csv(input_file)

    # Drop the userId and timestamp columns
    df = df.drop(['userId', 'timestamp'], axis=1)

    # Save the cleaned dataframe to a new csv file
    df.to_csv(output_file, index=False)


# Example usage
clean_csv('./dataset/ratings-25m.csv', './dataset/ratings-25m-cleaned.csv')
