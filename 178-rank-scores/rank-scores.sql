/* Write your T-SQL query statement below */
Select score , DENSE_RANK()over ( order by score DESC) as 'rank'
from scores;
