-- get duplicate emails; each row in Person has unique id
-- HAVING is a group filter

SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(id) > 1;

-- self join, which is faster than the above method using HAVING

SELECT DISTINCT
    A.email AS Email
FROM Person A
JOIN Person B
ON A.email = B.email
WHERE 
    A.email = B.email
    AND A.id > B.id