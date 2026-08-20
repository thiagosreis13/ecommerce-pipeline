select avg(extract(day from o.order_delivered_customer_date::timestamp - o.order_purchase_timestamp::timestamp)) as Nr_Dias_Entrega
from {{ ref('stg_orders') }} o
where o.order_status = 'delivered'