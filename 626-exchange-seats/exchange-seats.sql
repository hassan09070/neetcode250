# Write your MySQL query statement below
select f.id,
CASE
    WHEN f.id in (select max(id) from seat) and f.id%2 != 0 THEN student
    WHEN f.id%2 = 0  THEN (select student from seat as s where f.id -1 =s.id)
    WHEN f.id%2 != 0  THEN (select student from seat as s where f.id + 1 =s.id)
    ELSE f.student
END as student
from seat as f