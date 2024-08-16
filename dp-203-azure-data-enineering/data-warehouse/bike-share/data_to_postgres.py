import os

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Load environment variables from .env file
load_dotenv()

########################################
# Update connection string information #
########################################
host = os.getenv("HOST")
user = os.getenv("DB_USER")
password = os.getenv("PASSWORD")
# Create a new DB
sslmode = "require"
dbname = "postgres"
conn_string = (
    f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}"
)
conn = psycopg2.connect(conn_string)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
print("Connection established")

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS udacityproject")
cursor.execute("CREATE DATABASE udacityproject")
# Clean up initial connection
conn.commit()
cursor.close()
conn.close()

# Reconnect to the new DB
dbname = "udacityproject"
conn_string = (
    f"host={host} user={user} dbname={dbname} password={password} sslmode={sslmode}"
)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()


# Helper functions
def drop_recreate(c, tablename, create):
    c.execute(f"DROP TABLE IF EXISTS {tablename};")
    c.execute(create)
    print(f"Finished creating table {tablename}")


def populate_table(c, filename, tablename):
    with open(filename, "r") as f:
        try:
            cursor.copy_from(f, tablename, sep=",", null="")
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error: {error}")
            conn.rollback()
            cursor.close()
    print(f"Finished populating {tablename}")


# Create Rider table
table = "rider"
filename = "./data/riders.csv"
create = """CREATE TABLE rider (
    rider_id INTEGER PRIMARY KEY,
    first VARCHAR(50),
    last VARCHAR(50),
    address VARCHAR(100),
    birthday DATE,
    account_start_date DATE,
    account_end_date DATE,
    is_member BOOLEAN
);"""

drop_recreate(cursor, table, create)
populate_table(cursor, filename, table)

# Create Payment table
table = "payment"
filename = "./data/payments.csv"
create = """CREATE TABLE payment (
    payment_id INTEGER PRIMARY KEY,
    date DATE,
    amount MONEY,
    rider_id INTEGER
);"""

drop_recreate(cursor, table, create)
populate_table(cursor, filename, table)

# Create Station table
table = "station"
filename = "./data/stations.csv"
create = """CREATE TABLE station (
    station_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(75),
    latitude FLOAT,
    longitude FLOAT
);"""

drop_recreate(cursor, table, create)
populate_table(cursor, filename, table)

# Create Trip table
table = "trip"
filename = "./data/trips.csv"
create = """CREATE TABLE trip (
    trip_id VARCHAR(50) PRIMARY KEY,
    rideable_type VARCHAR(75),
    start_at TIMESTAMP,
    ended_at TIMESTAMP,
    start_station_id VARCHAR(50),
    end_station_id VARCHAR(50),
    rider_id INTEGER
);"""

drop_recreate(cursor, table, create)
populate_table(cursor, filename, table)

# Clean up
conn.commit()
cursor.close()
conn.close()

print("All done!")
