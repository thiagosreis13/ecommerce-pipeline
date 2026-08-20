with Dias_Entrega as (

select 
		o.order_id,
		extract(day from o.order_delivered_customer_date::timestamp - o.order_purchase_timestamp::timestamp) as Dif_dias,
		r.review_score as nota
from {{ ref('stg_orders') }} o
inner join {{ ref('stg_order_reviews') }} r on o.order_id = r.order_id 
)

select 
		CASE
			WHEN Dif_dias between 0 and 5 then '0 a 5 dias' 
			WHEN Dif_dias <= 10 then '6 a 10 dias'
			WHEN Dif_dias <= 15 then '11 a 15 dias'
			ELSE 'Mais que 15 dias'
		end as Faixa_Dias,
		avg(nota) as Vl_Media_nota
from Dias_Entrega
group by 
		case
			when Dif_dias between 0 and 5 then '0 a 5 dias' 
			when Dif_dias <= 10 then '6 a 10 dias'
			when Dif_dias <= 15 then '11 a 15 dias'
			else 'Mais que 15 dias'
		end