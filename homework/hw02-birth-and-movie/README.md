# Week 1 HW

The purpose of this assignment is to get comfortable working with a few of the tools we'll be using throughout the course (e.g., git, jupyter notebooks, pandas, matplotlib), and to do some basic data exploration and statistics.

Data sets (in the `data` directory):

[US Births 2000-2014](https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_2000-2014_SSA.csv)

[TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata/data)

NOTE: The TMDB data is hosted on kaggle.  See the host page for details on the data. There are two separate data sets from TMDB, one for movie details and one for credits.  These files include some data in JSON format; see [here](https://www.kaggle.com/sohier/getting-imdb-kernels-working-with-tmdb-data/) for tips on reading the data.

NOTE: The TMDB files in `data/` are stored gzipped (`tmdb_5000_movies.csv.gz`,
`tmdb_5000_credits.csv.gz`).  `pandas` reads them directly — no need to unzip:
`pd.read_csv('data/tmdb_5000_movies.csv.gz')`.


1. Find an interesting feature in the US Birth data set that we didn't find in class.  Be sure to describe clearly the feature you found, and include figures to back it up.

2. In class we found that the total number of births roughly correlated with the rise of the housing bubble and subsequent great recession.  We also found that people were generally superstitious, having fewer babies on Friday the 13th compared to other weekdays.  Does the level of superstition change with the health of the US economy?

3. Download and parse the TMDB data.  Find an interesting feature in the data.  Be sure to describe clearly the feature you found, and include figures to back it up.

## Graduate Students

Extending question 2: find some actual public data on the health of the US economy and see if a particular metric tracks with the annual birth rate in the US.
