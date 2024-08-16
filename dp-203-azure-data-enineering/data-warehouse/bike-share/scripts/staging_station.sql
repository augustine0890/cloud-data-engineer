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

CREATE EXTERNAL TABLE dbo.staging_station (
	[station_id] NVARCHAR(4000),
	[name] NVARCHAR(4000),
	[latitude] FLOAT,
	[longitude] FLOAT
	)
	WITH (
	LOCATION = 'publicstation.txt',
	DATA_SOURCE = [filesystembikesharestorage_bikesharestorage240814_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat],
	REJECT_VALUE = 1
	)
GO


SELECT TOP 100 * FROM dbo.staging_station
GO