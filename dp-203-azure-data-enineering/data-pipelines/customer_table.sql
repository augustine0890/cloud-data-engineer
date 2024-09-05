CREATE EXTERNAL TABLE Customer(
    [CustomerID] [int] NOT NULL,
    [NameStyle]  [bit] NOT NULL,
    [Title] [nvarchar](8) NULL,
    [FirstName] [nvarchar](128) NOT NULL,
    [MiddleName] [nvarchar](20) NULL,
    [LastName] [nvarchar](128) NOT NULL,
    [Suffix] [nvarchar](10) NULL,
    [CompanyName] [nvarchar](128) NULL,
    [SalesPerson] [nvarchar](256) NULL,
    [EmailAddress] [nvarchar](50) NULL,
    [Phone] [nvarchar](20) NULL,
    [PasswordHash] [varchar](128) NOT NULL,
    [PasswordSalt] [varchar](10) NOT NULL,
    [rowguid] [uniqueidentifier] NOT NULL,
    [ModifiedDate] [datetime] NOT NULL
)
WITH (
    LOCATION = Customer.csv',
  DATA_SOURCE = [mydlsfs20230413_mydls20230413_dfs_core_windows_net],
  FILE_FORMAT = [SynapseDelimitedTextFormat]
)
GO