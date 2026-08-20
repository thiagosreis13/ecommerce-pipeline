--top 10 vendedores por receita, com a nota média de avaliação dos pedidos deles.

select 	s.seller_id				as Id_Vendedor, 
		s.seller_state			as Estado, 
		s.seller_city			as Cidade,
		avg(r.review_score)		as Vl_Media_Nota,
		sum(oi.price)			as Vl_Receita
from {{ ref('stg_order_reviews') }} r--review_score
inner join {{ ref('stg_order_items') }} oi on r.order_id = oi.order_id
inner join {{ ref('stg_sellers') }} s on oi.seller_id = s.seller_id
group by
		s.seller_id, 
		s.seller_state, 
		s.seller_city
order by 5 desc 
limit 10