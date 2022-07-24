SELECT 
    name AS Customers
FROM Customers
WHERE id NOT IN
    (
    SELECT 
        O.customerId
    FROM Orders AS O
    LEFT JOIN Customers AS C
        ON O.customerId = C.id
    );