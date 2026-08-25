select sor.order_id
from {{ ref('stg_order_reviews') }} sor
where (sor.review_score < 1 or sor.review_score > 5)