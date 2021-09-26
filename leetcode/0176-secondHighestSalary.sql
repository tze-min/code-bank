# Write your MySQL query statement below

SELECT max(Salary) AS SecondHighestSalary FROM Employee
WHERE Salary not IN (SELECT max(Salary) FROM Employee)