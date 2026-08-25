SELECT soi.order_id
FROM {{ ref('stg_order_items') }} soi
where soi.freight_value < 0