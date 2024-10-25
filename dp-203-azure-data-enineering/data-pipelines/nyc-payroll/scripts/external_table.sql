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

IF NOT EXISTS (SELECT * FROM sys.external_file_formats WHERE name = 'SynapseDelimitedTextFormat') 
	CREATE EXTERNAL FILE FORMAT [SynapseDelimitedTextFormat] 
	WITH ( FORMAT_TYPE = DELIMITEDTEXT ,
	       FORMAT_OPTIONS (
			 FIELD_TERMINATOR = ',',
			 USE_TYPE_DEFAULT = FALSE
			))
GO

IF NOT EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net') 
	CREATE EXTERNAL DATA SOURCE [adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net] 
	WITH (
		LOCATION = 'abfss://adlsnycpayroll-augustine-lastintial@udacityde241024.dfs.core.windows.net' 
	)
GO

CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_AGENCY_MD] (
	[AgencyID] [varchar](10) NULL,
    [AgencyName] [varchar](50) NULL
	)
	WITH (
	LOCATION = '/',
	DATA_SOURCE = [adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO


CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_EMP_MD] (
	[EmployeeID] [varchar](10) NULL,
    [LastName] [varchar](20) NULL,
    [FirstName] [varchar](20) NULL
	)
	WITH (
	LOCATION = '/',
	DATA_SOURCE = [adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_TITLE_MD]  (
	[TitleCode] [varchar](10) NULL,
    [TitleDescription] [varchar](100) NULL
	)
	WITH (
	LOCATION = '/',
	DATA_SOURCE = [adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

CREATE EXTERNAL TABLE [dbo].[NYC_Payroll_Data] (
	[FiscalYear] [int] NULL,
    [PayrollNumber] [int] NULL,
    [AgencyID] [varchar](10) NULL,
    [AgencyName] [varchar](50) NULL,
    [EmployeeID] [varchar](10) NULL,
    [LastName] [varchar](20) NULL,
    [FirstName] [varchar](20) NULL,
    [AgencyStartDate] [date] NULL,
    [WorkLocationBorough] [varchar](50) NULL,
    [TitleCode] [varchar](10) NULL,
    [TitleDescription] [varchar](100) NULL,
    [LeaveStatusasofJune30] [varchar](50) NULL,
    [BaseSalary] [float] NULL,
    [PayBasis] [varchar](50) NULL,
    [RegularHours] [float] NULL,
    [RegularGrossPaid] [float] NULL,
    [OTHours] [float] NULL,
    [TotalOTPaid] [float] NULL,
    [TotalOtherPay] [float] NULL
	)
	WITH (
	LOCATION = '/',
	DATA_SOURCE = [adlsnycpayroll-augustine-lastintial_udacityde241024_dfs_core_windows_net],
	FILE_FORMAT = [SynapseDelimitedTextFormat]
	)
GO

