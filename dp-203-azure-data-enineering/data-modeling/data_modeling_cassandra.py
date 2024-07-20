#!/usr/bin/env python
# coding: utf-8

# # Part I. ETL Pipeline for Pre-Processing the Files

# #### Import Python packages 

# In[1]:


import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv


# #### Creating list of filepaths to process original event csv data files

# Print the current working directory: Shows the current directory path, e.g., '/home/user/project'.

# In[2]:


print(os.getcwd())


# Get the path of the 'event_data' directory: Creates the path to the 'event_data' folder within the current directory.

# In[3]:


filepath = os.getcwd() + '/event_data'


# Walk through the 'event_data' directory: Goes through the 'event_data' folder and its subfolders.
# Generate a list of file paths: Makes a list of all file paths in the current folder and its subfolders.

# In[4]:


for root, dirs, files in os.walk(filepath):
    file_path_list = glob.glob(os.path.join(root, '*'))


# #### Processing the files to create the data file csv that will be used for Apache Casssandra tables

# - Creates an empty list `full_data_rows_list` to store data rows from each file.
# - Loops through each file path in `file_path_list`.
# - Opens each CSV file with UTF-8 encoding and initializes a CSV reader.
# - Moves to the next line to skip the header.
# - Reads each row and appends it to `full_data_rows_list`.

# In[5]:


full_data_rows_list = [] 

for f in file_path_list:
    with open(f, 'r', encoding = 'utf8', newline='') as csvfile:
        csvreader = csv.reader(csvfile) 
        next(csvreader)

        for line in csvreader:
            full_data_rows_list.append(line)


# - Defines a custom CSV dialect named 'myDialect' for consistent formatting.
# - Creates a new CSV file `event_datafile_new.csv` and writes the header and rows from `full_data_rows_list`.

# In[6]:


csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
    writer = csv.writer(f, dialect='myDialect')
    writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',                'level','location','sessionId','song','userId'])
    for row in full_data_rows_list:
        if (row[0] == ''):
            continue
        writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


# Opens the CSV file `event_datafile_new.csv` and counts the number of lines, printing the total.

# In[7]:


with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
    print(sum(1 for line in f))


# # Part II. The Apache Cassandra Coding Challenge
# **Now you are ready to work with the CSV file titled <font color=red>event_datafile_new.csv</font>, located within the Workspace directory.  The event_datafile_new.csv contains the following columns:**
# - artist 
# - firstName of user
# - gender of user
# - item number in session
# - last name of user
# - length of the song
# - level (paid or free song)
# - location of the user
# - sessionId
# - song title
# - userId
# 
# The image below is a screenshot of what the denormalized data should appear like in the <font color=red>**event_datafile_new.csv**</font> after the code above is run:<br>
# 
# <img src="images/image_event_datafile_new.jpg">

# #### Creating a Cluster

# Connect to a local Cassandra instance at `127.0.0.1` by importing the `Cluster` class from `cassandra.cluster`, initializing a `Cluster` object, and establishing a session to execute queries.

# In[8]:


from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()


# #### Create Keyspace

# Create a keyspace named `udacity` with a replication strategy

# In[9]:


try:
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS udacity
        WITH REPLICATION = { 'class': 'SimpleStrategy', 'replication_factor': 1 }
        """)
except Exception as error:
    print(error)


# #### Set Keyspace

# Set the keyspace to `udacity`, handling any exceptions that occur.

# In[10]:


try:
    session.set_keyspace('udacity')
except Exception as error:
    print(error)


# ## Create queries to ask the following three questions of the data
# 
# ### 1. Give me the artist, song title and song's length in the music app history that was heard during  sessionId = 338, and itemInSession  = 4
# 

# Define a table named song_by_session with columns for `session_id`, `item_in_session`, `artist_name`, `song`, and `song_length`. The primary key is composed of `session_id` (partition key) and `item_in_session` (clustering column) that allowing efficient retrieval of items within a session.
# 
# Column names: `session_id`, `item_in_session`, `artist_name`, `song`, `song_length`.

# In[11]:


try:
    session.execute("""
        CREATE TABLE IF NOT EXISTS song_by_session (
            session_id INT,
            item_in_session INT,
            artist_name TEXT,
            song TEXT,
            song_length FLOAT,
            PRIMARY KEY (session_id, item_in_session)
        )
    """)
except Exception as error:
    print(error)


# Inserts data into `song_by_session` table from a CSV file. The table stores information about songs heard during specific sessions and items in sessions.

# In[12]:


file = 'event_datafile_new.csv'

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for line in csvreader:
        query = "INSERT INTO song_by_session (session_id, item_in_session, artist_name, song, song_length)"
        query = query + "VALUES (%s, %s, %s, %s, %s)"
        session.execute(query, (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))
    


# #### Do a SELECT to verify that the data have been inserted into each table

# In[13]:


query = """
    SELECT * FROM song_by_session
    LIMIT 5
"""
try:
    rows = session.execute(query)
except Exception as error:
    print(error)

pd.DataFrame(list(rows))


# **The query requests the artist, song title, and song length from the music app history for `sessionId` = 338 and `itemInSession` = 4.**

# In[14]:


query = """
    SELECT artist_name, song, song_length FROM song_by_session
    WHERE session_id = 338 AND item_in_session = 4
"""
try:
    row = session.execute(query)
except Exception as error:
    print(error)

pd.DataFrame(list(row))


# ### 2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

# Create a table to store user and session-based song information, with `user_id` and `session_id` as the composite partition key and `item_in_session` as the clustering column.
# - Partition Key (`user_id`, `session_id`): Groups data by user and session to allow querying by these identifiers.
# - Clustering Column (`item_in_session`): Sorts data within each partition, enabling efficient ordered retrieval.
# 
# Column names: `user_id`, `session_id`, `item_in_session`, `artist_name`, `song`, `first_name`, `last_name`.

# In[15]:


try:
    session.execute("""
        CREATE TABLE IF NOT EXISTS artist_by_user_and_session (
            user_id INT,
            session_id INT,
            item_in_session INT,
            artist_name TEXT,
            song TEXT,
            first_name TEXT,
            last_name TEXT,
            PRIMARY KEY ((user_id, session_id), item_in_session)
        )
    """)
except Exception as error:
    print(error)


# Inserts data into `artist_by_user_and_session` table from a CSV file.

# In[16]:


file = 'event_datafile_new.csv'

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for line in csvreader:
        query = "INSERT INTO artist_by_user_and_session (user_id, session_id, item_in_session, artist_name, song, first_name, last_name)"
        query = query + "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        session.execute(query, (int(line[10]), int(line[8]), int(line[3]), line[0], line[9], line[1], line[4]))


# **The query requests the name of the artist, song (sorted by itemInSession), and user (first and last name) for `userid` = 10 and `sessionid` = 182**

# In[17]:


query = """
    SELECT artist_name, song, item_in_session, first_name, last_name FROM artist_by_user_and_session
    WHERE user_id = 10 AND session_id = 182
"""
try:
    row = session.execute(query)
except Exception as error:
    print(error)

pd.DataFrame(list(row))
                    


# ### 3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

# Create a `user_by_song` table to store user information for each song, with the `song` as the partition key and `user_id` as the clustering column.
# - Partition Key (`song`): Groups data by song to allow querying by song title.
# - Clustering Column (`user_id`): Ensures uniqueness within the partition and allows for efficient data retrieval.
# 
# The table should allow for efficient retrieval of user names for a specific song.
# 
# Column names: `song`,`user_id`, `first_name`, `last_name`.

# In[18]:


try:
    session.execute("""
        CREATE TABLE IF NOT EXISTS user_by_song (
            song TEXT,
            user_id INT,
            first_name TEXT,
            last_name TEXT,
            PRIMARY KEY (song, user_id)
        )
    """)
except Exception as error:
    print(error)


# Inserts data into `user_by_song` table from a CSV file.

# In[19]:


file = 'event_datafile_new.csv'

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for line in csvreader:
        query = "INSERT INTO user_by_song (song, user_id, first_name, last_name)"
        query = query + "VALUES (%s, %s, %s, %s)"
        session.execute(query, (line[9], int(line[10]), line[1], line[4]))


# **The query requests the first and last names of every user who listened to the song 'All Hands Against His Own'.**

# In[20]:


query = """
    SELECT first_name, last_name FROM user_by_song
    WHERE song = 'All Hands Against His Own'
"""
try:
    row = session.execute(query)
except Exception as error:
    print(error)

pd.DataFrame(list(row))              


# ### Drop the tables before closing out the sessions

# In[21]:


try:
    session.execute("DROP TABLE IF EXISTS song_by_session")
except Exception as error:
    print(error)

try:
    session.execute("DROP TABLE IF EXISTS artist_by_user_and_session")
except Exception as error:
    print(error)

try:
    session.execute("DROP TABLE IF EXISTS user_by_song")
except Exception as error:
    print(error)


# ### Close the session and cluster connection¶

# In[22]:


session.shutdown()
cluster.shutdown()


# In[ ]:





# In[ ]:




