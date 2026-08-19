select  sct.product_category_name_english 	as Nm_Categoria_Ingles,
		sum(soi.price) 						as Vl_Produto
from {{ ref('stg_order_items') }} soi
inner join {{ ref('stg_products') }} sp on soi.product_id = sp.product_id
inner join {{ ref('stg_category_translation') }} sct on sp.product_category_name = sct.product_category_name
group by sct.product_category_name_english