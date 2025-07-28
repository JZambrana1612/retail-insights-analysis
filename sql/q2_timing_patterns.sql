-- Q2: How does the timing or frequency of purchases affect revenue generation?

-- This script provides two summaries: revenue by month and revenue by quarter.
-- The Month and Quarter fields are precomputed in the dataset (e.g., '2023-05'
-- and 'Q2-2023').  If your dataset lacks these fields, you can derive them
-- using DATE_FORMAT(SaleDate, '%Y-%m') and CONCAT('Q', QUARTER(SaleDate), '-', YEAR(SaleDate)).

-- Revenue by Month
SELECT
    Month,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_sales
GROUP BY Month
ORDER BY Month;

-- Revenue by Quarter
SELECT
    Quarter,
    ROUND(SUM(Revenue), 2) AS Total_Revenue
FROM retail_sales
GROUP BY Quarter
ORDER BY Quarter;