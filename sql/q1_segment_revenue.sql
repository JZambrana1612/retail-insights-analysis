-- Q1: Which customer segments contribute most to revenue?

-- This query summarises revenue and basket size by gender.  It returns the total
-- revenue, average revenue per transaction, number of transactions and
-- average basket size for each gender.  Results are ordered by total
-- revenue in descending order so the highest‑contributing segment appears first.

SELECT
    Gender,
    COUNT(*) AS Transactions,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(AVG(Revenue), 2) AS Avg_Revenue,
    ROUND(AVG(`Basket Size`), 2) AS Avg_Basket_Size
FROM retail_sales
GROUP BY Gender
ORDER BY Total_Revenue DESC;