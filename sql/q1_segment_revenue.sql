-- q1_segment_revenue.sql
--
-- Answer to Question 1: Which customer segments contribute most to revenue?
--
-- This query summarises transaction counts, total revenue, average revenue
-- and average basket size by gender using the cleaned retail sales table.

SELECT
    Gender,
    COUNT(*)            AS Transactions,
    SUM(Revenue)        AS TotalRevenue,
    AVG(Revenue)        AS AvgRevenue,
    AVG(BasketSize)     AS AvgBasketSize
FROM retail_sales_clean
GROUP BY Gender
ORDER BY TotalRevenue DESC;