CREATE TABLE SalesOrderHeader(
[SalesOrderID] [int] NOT NULL,
[RevisionNumber] [tinyint] NOT NULL,
[OrderDate] [datetime] NOT NULL,
[DueDate] [datetime] NOT NULL,
[ShipDate] [datetime] NULL,
[Status] [tinyint] NOT NULL,
[OnlineOrderFlag] [BIT] NOT NULL,
[SalesOrderNumber]  [nvarchar](23) not null,
[PurchaseOrderNumber] [nvarchar](23) NULL,
[AccountNumber] [nvarchar](23) NULL,
[CustomerID] [int] NOT NULL,
[ShipToAddressID] [int] NULL,
[BillToAddressID] [int] NULL,
[ShipMethod] [nvarchar](50) NOT NULL,
[CreditCardApprovalCode] [varchar](15) NULL,
[SubTotal] [money] NOT NULL,
[TaxAmt] [money] NOT NULL,
[Freight] [money] NOT NULL,
[TotalDue]  [money] NULL,
[Comment] [nvarchar](1000) NULL,
[rowguid] [uniqueidentifier] NOT NULL,
[ModifiedDate] [datetime] NOT NULL
)
WITH (
    LOCATION = SalesOrderHeader.csv',
  DATA_SOURCE = [mydlsfs20230413_mydls20230413_dfs_core_windows_net],
  FILE_FORMAT = [SynapseDelimitedTextFormat]
)
GO