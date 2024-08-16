USE bikeshare_project;

-- Drop table if exists
IF OBJECT_ID('dbo.fact_payment') IS NOT NULL
    DROP EXTERNAL TABLE dbo.fact_payment;

-- Create fact_payment table using the corresponding staging one
CREATE EXTERNAL TABLE dbo.fact_payment WITH (
    LOCATION = 'starSchema/fact_payment',
    DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
    FILE_FORMAT = [SynapseDelimitedTextFormat]
) AS (
    SELECT
        P.[payment_id],  -- Payment ID from staging_payment

        -- Convert the payment date to a date_id, assuming dim_date has a 'date' column
        D.date_id AS [payment_date_id],

        P.[amount],  -- Amount of the payment

        -- Rider ID from staging_payment
        P.[rider_id] 

    FROM
        dbo.staging_payment AS P
        
        -- Join with dim_date to get the date_id
        INNER JOIN dbo.dim_date AS D 
            ON CONVERT(DATE, P.[date], 120) = D.[date]

        -- Join with dim_rider to ensure the rider exists in dim_rider
        INNER JOIN dbo.dim_rider AS R 
            ON P.[rider_id] = R.[rider_id]
);

-- Query to verify the first 10 records
SELECT TOP 10 * FROM dbo.fact_payment;
