USE bikeshare_project;

-- Drop table if exists
IF OBJECT_ID('dbo.dim_rider') IS NOT NULL
    DROP EXTERNAL TABLE dbo.dim_rider;

-- Create dim_rider table using the corresponding staging one
CREATE EXTERNAL TABLE dbo.dim_rider WITH (
    LOCATION = 'starSchema/dim_rider',
    DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
) AS (
    SELECT
		R.[rider_id],
        R.[first],
        R.[last],
        CONVERT(varchar(10), R.[birthday], 111) AS [birthday],
        CONVERT(varchar(10), R.[account_start_date], 111) AS [account_start_date],
        DATEDIFF(YEAR, R.[birthday], R.[account_start_date]) AS [age_at_account_start], -- Age of the rider when they created their account (int).
        CASE
            WHEN R.[is_member] = 1 THEN 'Member'
            ELSE 'Casual'
        END AS [membership_status] -- Membership status: 'Member' or 'Casual' (varchar(10)).
    FROM
        dbo.staging_rider AS R
);

-- Query to verify the first 10 records
SELECT TOP 10 * FROM dbo.dim_rider;
