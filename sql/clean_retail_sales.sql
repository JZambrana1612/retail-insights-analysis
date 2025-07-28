-- clean_retail_sales.sql
--
-- This script demonstrates how to transform the raw retail sales table
-- into a cleaned dataset using SQL.  It assumes a source table named
-- ``retail_sales_full_dataset`` with the original column names used in
-- the CSV file (including spaces).  The query selects and renames
-- columns, parses the sale date, computes revenue, basket size, month
-- and quarter, and returns a result set matching the cleaned CSV.

SELECT
    `Transaction ID`      AS TransactionID,
    DATE(`Date`)          AS SaleDate,
    `Customer ID`         AS CustomerID,
    `Gender`              AS Gender,
    `Age`                 AS Age,
    `Product Category`    AS ProductCategory,
    `Quantity`            AS Quantity,
    `Price per Unit`      AS PricePerUnit,
    `Total Amount`        AS TotalAmount,
    DATE_FORMAT(`Date`, '%Y-%m')                                   AS Month,
    CONCAT('Q', QUARTER(`Date`), '-', YEAR(`Date`))                AS Quarter,
    `Quantity`                                                   AS `Basket Size`,
    (`Quantity` * `Price per Unit`)                              AS Revenue
FROM retail_sales_full_dataset;