import pandas as pd

reviews = pd.read_csv("data/ign.csv")

print reviews.head(5)

print reviews.tail(5)

reviews.shape

reviews.iloc[0:5,:]

reviews.iloc[9,:]

reviews = reviews.iloc[:,1:]
reviews.head()

reviews.loc[0:5,:]

reviews.index

reviews.loc[:5, "score"]

reviews.loc[:5, ["score", "release_year"]]

s1 = pd.Series([1,2])

s2 = pd.Series(['Bangalore', 'Chennai'])

pd.DataFrame([s1,s2])

frame = pd.DataFrame(
    [
        [1,2],
        ['Bangalore', 'Chennai']
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
)
frame

reviews["score"].mean()

reviews.mean()

reviews.mean(axis=1)

reviews['score']

score_filter = reviews['score'] > 7
score_filter

filtered_reviews = reviews[score_filter]
filtered_reviews.head()

xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()

%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()