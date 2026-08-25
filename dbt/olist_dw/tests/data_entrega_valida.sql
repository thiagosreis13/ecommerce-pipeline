select so.order_id 
from {{ ref('stg_orders') }} so
where so.order_delivered_customer_date < order_purchase_timestamp