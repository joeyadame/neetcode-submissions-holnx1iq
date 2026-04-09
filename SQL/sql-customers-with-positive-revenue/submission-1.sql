-- Write your query below
SELECT 
    customer_id
FROM 
    customers
WHERE year = 2020
GROUP BY 1
HAVING SUM(revenue) > 0;