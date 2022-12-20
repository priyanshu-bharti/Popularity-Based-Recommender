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


# ============================================================================ #
#          Creating the Model for Popularity Based Recommender System          #
# ============================================================================ #

# We will be displaying the highest rated books (Top 50)

# For this, we will consider the following criteria:
# 1. Choose only those books that have been rated by 250+ people.
# 2. Choose only those people who have rated more than 5 books.

# ········· 1. Merge the books and ratings csv based on "ISBN Column" ········ #
books_with_ratings = ratings.merge(books, on='ISBN')

# ··················· 2. Check the Shape of the merged set ··················· #
# print(books_with_ratings.shape)

# ·············· 3. Calculate the number of ratings on each book ············· #
num_rating_df = books_with_ratings.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={"Book-Rating": "#-of-Ratings"}, inplace=True)
# print(num_rating_df.head())

# ··············· 4. Calculate the average ratings on each book ·············· #
avg_rating_df = books_with_ratings.groupby('Book-Title').mean()['Book-Rating'].reset_index()
avg_rating_df.rename(columns={"Book-Rating": "Average-Ratings"}, inplace=True)
# print(avg_rating_df.head())

# ···· 5. Create a popular dataframe by merging both num and avg rating df ··· #
popular_df = num_rating_df.merge(avg_rating_df, on="Book-Title")
# print(popular_df.head())

# ·· 6. Filter only those rows that have more than 250 ratings in desc order · #
popular_df = popular_df[popular_df['#-of-Ratings'] >=250].sort_values('Average-Ratings', ascending=False)
# print(popular_df.head())

# ·· 7. Merge the popular books with the original books df to get more info. · #
popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Image-URL-M']]
print(popular_df.head())