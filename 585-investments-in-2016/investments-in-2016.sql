# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016
from Insurance 
WHERE pid IN
(select  distinct f.pid
from insurance f
join insurance s
on s.pid != f.pid 
where f.tiv_2015 = s.tiv_2015 )
and  pid not IN
(select  distinct f.pid
from insurance f
join insurance s
on s.pid != f.pid 
where f.lon = s.lon and f.lat = s.lat)