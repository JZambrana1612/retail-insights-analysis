-- q2_timing_patterns.sql
--
-- Answer to Question 2: How does the timing or frequency of purchases affect revenue?
--
-- This query aggregates total revenue by month to reveal seasonal trends.

SELECT
    Month,
    SUM(Revenue) AS TotalRevenue
FROM retail_sales_clean
GROUP BY Month
ORDER BY Month;