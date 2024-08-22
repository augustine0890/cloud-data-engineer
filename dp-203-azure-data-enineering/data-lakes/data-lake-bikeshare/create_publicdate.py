from datetime import datetime, timedelta

import pandas as pd

# Step 1: Read the payments.csv file without headers
payments_df = pd.read_csv("./data/payments.csv", header=None)

# Step 2: Manually assign column names based on the known order
payments_df.columns = ["payment_id", "date", "amount", "rider_id"]

# Step 3: Convert the date column to datetime format and handle any parsing errors
payments_df["date"] = pd.to_datetime(payments_df["date"], errors="coerce")

# Step 4: Drop any rows where date conversion failed
payments_df = payments_df.dropna(subset=["date"])

# Step 5: Extract the minimum and maximum dates
min_date = payments_df["date"].min()
max_date = payments_df["date"].max()

# Step 6: Generate a sequence of dates from min_date to max_date
date_range = pd.date_range(start=min_date, end=max_date)

# Step 7: Create the dim_date DataFrame with date_id starting from 1 to n
dim_date_df = pd.DataFrame(
    {
        "date_id": range(1, len(date_range) + 1),  # date_id from 1 to n
        "date": date_range,  # the actual date
        "day_of_week": date_range.strftime("%A"),  # day of the week
        "month": date_range.month,  # month as integer
        "quarter": date_range.quarter,  # quarter of the year
        "year": date_range.year,  # year as integer
    }
)

# Step 8: Save the dim_date DataFrame to publicdate.csv
dim_date_df.to_csv("./data/publicdate.csv", index=False)

print("publicdate.csv has been created successfully.")
