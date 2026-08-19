WITH soma_pedidos AS (
    select 	sop.order_id		as id_pedidos, 
		sum(sop.payment_value)	as vl_pedido
	from {{ ref('stg_order_payments') }} sop
	group by sop.order_id
)

SELECT
    avg(vl_pedido) as Vl_Ticket_Medio
FROM soma_pedidos