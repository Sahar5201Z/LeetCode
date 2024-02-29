# Write your MySQL query statement below

#select Employee.name as 'Employee' from Employee left join (select id, salary from Employee) as T on T.id=Employee.managerId where Employee.salary> T.salary

SELECT e2.name as Employee
FROM employee e1
inner JOIN employee e2 ON e1.id = e2.managerID
WHERE e1.salary < e2.salary