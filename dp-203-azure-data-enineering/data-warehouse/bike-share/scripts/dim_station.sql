USE bikeshare_project;

-- Drop table if exists
IF OBJECT_ID('dbo.dim_station') IS NOT NULL
    DROP EXTERNAL TABLE dbo.dim_station;

-- Create fact_Trip table using the corresponding staging one
CREATE EXTERNAL TABLE dbo.dim_station WITH (
    LOCATION = 'starSchema',
    DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
) AS (
    SELECT 
		[station_id],
        [name],
        [latitude],
        [longitude]
    FROM
        dbo.staging_station AS S
);

-- Query to verify the first 10 records
SELECT TOP 10 * FROM dbo.dim_station;
