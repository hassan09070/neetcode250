# Write your MySQL query statement below

select f.customer_id 
from Customer as f
group by f.customer_id 
having (select count(product_key) from ( select distinct s.product_key from Customer as s where f.customer_id= s.customer_id )as t) = (select count(product_key) from Product)

