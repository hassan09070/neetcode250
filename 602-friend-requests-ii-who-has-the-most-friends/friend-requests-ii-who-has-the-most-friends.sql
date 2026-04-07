SELECT user_id as id, sum(total) as num
FROM (
    SELECT COUNT(requester_id) AS total, accepter_id AS user_id
    FROM RequestAccepted
    GROUP BY accepter_id

    UNION ALL

    SELECT COUNT(accepter_id) AS total, requester_id AS user_id
    FROM RequestAccepted
    GROUP BY requester_id
) t
group by user_id
ORDER BY num DESC
limit 1