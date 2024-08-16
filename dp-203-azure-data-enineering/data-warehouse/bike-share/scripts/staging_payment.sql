IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://filesystembikesharestorage@bikesharestorage240814.dfs.core.windows.net' 
	)
GO

CREATE EXTERNAL TABLE dbo.staging_payment (
	[payment_id] BIGINT,
	[date] VARCHAR(50),
	[amount] FLOAT,
	[rider_id] BIGINT
	)
	WITH (
	LOCATION = 'publicpayment.txt',
	DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat],
	REJECT_VALUE = 1  -- Reject after 1 error
	)
GO


SELECT TOP 100 * FROM dbo.staging_payment
GO