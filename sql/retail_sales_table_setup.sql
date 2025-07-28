-- ========================================
-- Retail Sales Dataset - MySQL Table Setup
-- ========================================

-- Drop table if it already exists
DROP TABLE IF EXISTS retail_sales;

-- Create the retail_sales table
CREATE TABLE retail_sales (
    TransactionID INT PRIMARY KEY,
    SaleDate DATE,
    CustomerID VARCHAR(20),
    Gender ENUM('Male','Female'),
    Age INT,
    ProductCategory VARCHAR(50),
    Quantity INT,
    PricePerUnit DECIMAL(10,2),
    TotalAmount DECIMAL(10,2),
    Month VARCHAR(7),
    Quarter VARCHAR(7),
    `Basket Size` INT,
    Revenue DECIMAL(10,2)
);