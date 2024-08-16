USE bikeshare_project;

-- Drop table if exists
IF OBJECT_ID('dbo.fact_trip') IS NOT NULL
    DROP EXTERNAL TABLE dbo.fact_trip;

-- Create fact_trip table using the corresponding staging one
CREATE EXTERNAL TABLE dbo.fact_trip WITH (
    LOCATION = 'starSchema/fact_trip',
    DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
    FILE_FORMAT = [SynapseDelimitedTextFormat]
) AS (
    SELECT
        T.[trip_id],  -- Primary Key: Unique identifier for each trip

        R.rider_id AS [rider_id], -- Foreign key to dim_rider, links trip to the rider

        T.[start_station_id] AS [start_station_id],  -- Foreign key to dim_station, links to start station
        T.[end_station_id] AS [end_station_id],  -- Foreign key to dim_station, links to end station
        
        D.date_id AS [trip_date_id],  -- Foreign key to dim_date, links to the trip date
        
        -- Calculate duration in minutes using the truncated datetime strings
        DATEDIFF(MINUTE, 
            CONVERT(DATETIME, LEFT(T.[start_at], 19), 120), 
            CONVERT(DATETIME, LEFT(T.[ended_at], 19), 120)
        ) AS [duration],

        -- Calculate rider age at the time of the trip
        DATEDIFF(YEAR, CONVERT(DATE, R.[birthday], 120), CONVERT(DATE, LEFT(T.[start_at], 19), 120)) AS [rider_age]

    FROM
        dbo.staging_trip AS T

        -- Join with dim_rider to ensure the rider exists in dim_rider
        INNER JOIN dbo.dim_rider AS R 
            ON T.[rider_id] = R.[rider_id]

        -- Join with dim_date to get the trip date_id
        INNER JOIN dbo.dim_date AS D 
            ON CONVERT(DATE, LEFT(T.[start_at], 19), 120) = D.[date]
);

-- Query to verify the first 10 records
SELECT TOP 10 * FROM dbo.fact_trip;
