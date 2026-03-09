-- Monthly revenue

SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    SUM(price + freight_value) AS revenue
FROM sales
GROUP BY month
ORDER BY month;



-- Number of orders per month

SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    COUNT(DISTINCT order_id) AS orders
FROM sales
GROUP BY month
ORDER BY month;



-- Top 10 products by revenue

SELECT
    product_id,
    SUM(price + freight_value) AS revenue,
    COUNT(*) AS quantity
FROM sales
GROUP BY product_id
ORDER BY revenue DESC
LIMIT 10;



-- Top customers by revenue

SELECT
    customer_unique_id,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(price + freight_value) AS total_revenue
FROM sales
GROUP BY customer_unique_id
ORDER BY total_revenue DESC
LIMIT 10;



-- Average order value

SELECT
    AVG(order_value) AS avg_order_value
FROM (
    SELECT
        order_id,
        SUM(price + freight_value) AS order_value
    FROM sales
    GROUP BY order_id
) t;