-- Table schema for sales analysis dataset

CREATE TABLE sales (
    order_id TEXT,
    product_id TEXT,
    seller_id TEXT,
    customer_id TEXT,
    customer_unique_id TEXT,

    order_status TEXT,

    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP,

    product_category_name TEXT,

    price NUMERIC,
    freight_value NUMERIC,
    revenue NUMERIC,
    order_value NUMERIC
);
