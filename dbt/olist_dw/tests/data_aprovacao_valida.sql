SELECT so.order_id
FROM {{ ref('stg_orders') }} so
where so.order_approved_at < so.order_purchase_timestamp