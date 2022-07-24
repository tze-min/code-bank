-- report the second highest salary, but if there's no second highest salary, return null

SELECT 
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

SELECT 
	MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary NOT IN (SELECT max(Salary) FROM Employee);

-- the below method doesn't return NULL when there's no second highest salary; only returns ""

SELECT 
    salary AS SecondHighestSalary
FROM Employee
ORDER BY salary DESC
LIMIT 1, 1;
