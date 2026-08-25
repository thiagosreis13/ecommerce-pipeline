SELECT soi.order_id
FROM {{ ref('stg_order_items') }} soi
where soi.price <= 0