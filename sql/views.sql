-- Monthly sales view

CREATE VIEW monthly_sales AS
SELECT
    DATE_TRUNC('month', order_purchase_timestamp) AS month,
    SUM(revenue) AS total_revenue,
    COUNT(DISTINCT order_id) AS orders_count
FROM sales
GROUP BY month;

-- Top products view
CREATE VIEW top_products AS
SELECT
    product_id,
    SUM(revenue) AS total_revenue,
    COUNT(*) AS quantity_sold
FROM sales
GROUP BY product_id;

-- Customer summary view
CREATE VIEW customer_summary AS
SELECT
    customer_unique_id,
    COUNT(DISTINCT order_id) AS orders_count,
    SUM(revenue) AS total_revenue,
    AVG(order_value) AS avg_order_value
FROM sales
GROUP BY customer_unique_id;