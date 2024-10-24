-- Use the same file format as used for creating the External Tables during the LOAD step.
IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
FORMAT_OPTIONS (
FIELD_TERMINATOR = ',',
USE_TYPE_DEFAULT = FALSE
))
GO

-- Check if the external data source exists, and create it if it doesn't.
IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'ADLS_PayrollStorage')
BEGIN
    CREATE EXTERNAL DATA SOURCE [ADLS_PayrollStorage]
    WITH (
        LOCATION = 'abfss://adlsnycpayroll-augustine-lastintial@udacityde241024.dfs.core.windows.net'
    );
END
GO

-- Create the external table after ensuring the external data source exists.
CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_Summary]
(
	[FiscalYear] [int] NULL,
	[AgencyName] [varchar](50) NULL,
	[TotalPaid] [float] NULL
)
WITH
(
	LOCATION = '/',
	DATA_SOURCE = [ADLS_PayrollStorage],  -- Use the name of the external data source, not the URL
	FILE_FORMAT = [SynapseDelimitedTextFormat]
);
GO

