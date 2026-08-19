SELECT	order_status        as Status, 
        count(order_id) 	as Qtde
FROM 	{{ ref('stg_orders') }}
group by order_status 