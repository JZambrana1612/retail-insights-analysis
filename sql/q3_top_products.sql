-- Q3: Which products should be prioritised?

-- This query ranks product categories by total revenue and reports the
-- average unit price and average revenue per transaction for each category.
-- Ordering by Total_Revenue highlights the most valuable categories.

SELECT
    ProductCategory,
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    ROUND(AVG(PricePerUnit), 2) AS Avg_Unit_Price,
    ROUND(AVG(Revenue), 2) AS Avg_Revenue_Per_Transaction
FROM retail_sales
GROUP BY ProductCategory
ORDER BY Total_Revenue DESC;