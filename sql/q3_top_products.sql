-- q3_top_products.sql
--
-- Answer to Question 3: If we could only stock or promote a limited range of products,
-- which ones should be prioritised?
--
-- This query ranks product categories by total revenue and also reports
-- transaction count, average revenue per transaction and average unit price.

SELECT
    ProductCategory,
    COUNT(*)        AS Transactions,
    SUM(Revenue)    AS TotalRevenue,
    AVG(Revenue)    AS AvgRevenue,
    AVG(PricePerUnit) AS AvgUnitPrice
FROM retail_sales_clean
GROUP BY ProductCategory
ORDER BY TotalRevenue DESC;