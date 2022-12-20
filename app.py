# ============================================================================ #
#                             Importing the dataset                            #
# ============================================================================ #

# ····························· Import Libraries ····························· #
import numpy as np
import pandas as pd

# ···························· Open the CSV Files ···························· #
books = pd.read_csv('datasets/Books.csv')
users = pd.read_csv('datasets/Users.csv')
ratings = pd.read_csv('datasets/Ratings.csv')


# ============================================================================ #
#                               Checking the data                              #
# ============================================================================ #


# ····················· Print the headers of the datasets ···················· #
# print(books.head())
# print(users.head())
# print(ratings.head())

# ······················· Show the shape of the dataset ······················ #
# print(books.shape)
# print(users.shape)
# print(ratings.shape)

# ············ Check how many null rows are present in the dataset ··········· #
# print(books.isnull().sum())
# print(users.isnull().sum())
# print(ratings.isnull().sum())

# ········· Check how many duplicate rows are present in the dataset ········· #
# print(books.duplicated().sum())
# print(users.duplicated().sum())
# print(ratings.duplicated().sum())
