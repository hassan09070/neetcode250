CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
IF @N < 1
    RETURN NULL;
    RETURN (
        Select 
            CASE
                WHEN (SELECT  COUNT(Distinct salary) from employee) < @N Then NULL
                ELSE(
                SELECT MIN(salary)
                    FROM (
                        SELECT DISTINCT TOP (@N) salary
                        FROM Employee
                        ORDER BY salary DESC
                    ) AS temp
                )
        END
    );
END