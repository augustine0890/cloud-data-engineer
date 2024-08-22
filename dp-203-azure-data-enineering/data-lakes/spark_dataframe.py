#!/usr/bin/env python
# coding: utf-8

"""
Answer Key to the Data Wrangling with DataFrames Coding Quiz

Helpful resources:
https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html
"""

import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.window import Window

# 1) Import necessary libraries (done above)
# 2) Instantiate a Spark session
spark = SparkSession.builder.appName("DataFrames Practice").getOrCreate()

# 3) Read in the data set
df = spark.read.json("data/sparkify_log_small.json")

# # Question 1: Which page did user id "" (empty string) NOT visit?

# Print schema for inspection
df.printSchema()

# Filter for users with blank user id and get unique pages they visited
blank_pages = (
    df.filter(F.col("userId") == "")
    .select(F.col("page").alias("blank_pages"))
    .dropDuplicates()
)

# Get a list of all possible pages that could be visited
all_pages = df.select("page").dropDuplicates()

# Find pages that the blank user did not visit
non_visited_pages = all_pages.subtract(blank_pages)

# Display the pages that were not visited by the blank user
non_visited_pages.show()

# # Question 2: What type of user does the empty string user id most likely refer to?
#
# Answer: It likely represents users who have not signed up yet or who are signed out and are about to log in.

# # Question 3: How many female users do we have in the dataset?

num_female_users = (
    df.filter(F.col("gender") == "F").select("userId").dropDuplicates().count()
)

print(f"Number of female users: {num_female_users}")

# # Question 4: How many songs were played from the most played artist?

most_played_artist = (
    df.filter(F.col("page") == "NextSong")
    .groupBy("Artist")
    .agg(F.count("Artist").alias("ArtistCount"))
    .orderBy(F.desc("ArtistCount"))
    .show(1)
)

# # Question 5 (challenge): How many songs do users listen to on average between visiting our home page? Please round your answer to the closest integer.

# Define a UDF to mark home page visits
is_home_page_udf = F.udf(lambda page: int(page == "Home"), IntegerType())

# Define a window to partition by user and order by timestamp
user_window = (
    Window.partitionBy("userId")
    .orderBy(F.desc("ts"))
    .rangeBetween(Window.unboundedPreceding, 0)
)

# Calculate cumulative sum for each user, and count the number of songs between 'Home' page visits
cusum = (
    df.filter((F.col("page") == "NextSong") | (F.col("page") == "Home"))
    .select("userId", "page", "ts")
    .withColumn("homeVisit", is_home_page_udf(F.col("page")))
    .withColumn("period", F.sum("homeVisit").over(user_window))
)

# Calculate the average number of songs listened to between home page visits
average_songs_between_home = (
    cusum.filter(F.col("page") == "NextSong")
    .groupBy("userId", "period")
    .agg(F.count("period").alias("songCount"))
    .agg(F.avg("songCount").alias("avgSongsBetweenHome"))
    .collect()[0]["avgSongsBetweenHome"]
)

# Print the rounded result
print(
    f"Average number of songs between home page visits: {round(average_songs_between_home)}"
)
