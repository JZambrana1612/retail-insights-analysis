-- create_clean_retail_sales_table.sql
--
-- This script defines the schema for a cleaned retail sales table.  It
-- matches the structure of the cleaned CSV produced by
-- ``clean_retail_data.py`` and the SELECT in ``clean_retail_sales.sql``.
-- Columns use appropriate data types for transactional data and include
-- derived fields such as Month and Quarter.

CREATE TABLE retail_sales_clean (
    TransactionID  INT            NOT NULL,
    SaleDate       DATE           NOT NULL,
    CustomerID     VARCHAR(20)    NOT NULL,
    Gender         VARCHAR(10)    NOT NULL,
    Age            INT            NOT NULL,
    ProductCategory VARCHAR(50)   NOT NULL,
    Quantity       INT            NOT NULL,
    PricePerUnit   DECIMAL(10,2)  NOT NULL,
    TotalAmount    DECIMAL(10,2)  NOT NULL,
    Month          CHAR(7)        NOT NULL, -- YYYY-MM
    Quarter        CHAR(8)        NOT NULL, -- QX-YYYY
    BasketSize     INT            NOT NULL,
    Revenue        DECIMAL(10,2)  NOT NULL,
    PRIMARY KEY (TransactionID)
);