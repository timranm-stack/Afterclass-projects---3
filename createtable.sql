-- Part 1: Create the Table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    status VARCHAR(20)
);

-- Part 2: Insert Sample Data
INSERT INTO employees (employee_id, first_name, last_name, department, salary, status)
VALUES 
(101, 'John', 'Doe', 'Finance', 65000.00, 'Active'),
(102, 'Jane', 'Smith', 'HR', 55000.00, 'Active'),
(103, 'Tarun', 'Sharma', 'IT', 75000.00, 'Active'),
(104, 'Robert', 'Johnson', 'Finance', 90000.00, 'Under Investigation'),
(105, 'Emily', 'Davis', 'Operations', 48000.00, 'Under Investigation');

-- Part 3: Fetch Specific Records
SELECT employee_id, first_name, last_name, department, status 
FROM employees 
WHERE status = 'Under Investigation';