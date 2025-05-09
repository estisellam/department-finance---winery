
-- SELECT queries
-- 1
SELECT DISTINCT e.e_id, e.e_name
FROM employee e
NATURAL JOIN payment p
NATURAL JOIN in_Investments i
ORDER BY e.e_name ASC;

-- 2
SELECT p.p_id, p.p_date, i.id_Consumer
FROM payment p
NATURAL JOIN in_Purchases_from i
WHERE p.p_date = '2023-06-15';

-- 3
SELECT e_id, e_name, job_start_date
FROM employee
WHERE job_start_date < '2020-01-01'
ORDER BY job_start_date ASC;

-- 4
SELECT p_year, SUM(p_sum) AS total_income
FROM payment
WHERE in_or_out = 'in'
GROUP BY p_year
ORDER BY p_year;

-- 5
SELECT e.e_id, e.name, e.salary
FROM employee e
NATURAL JOIN payment p
GROUP BY e.e_id, e.name, e.salary
HAVING e.salary > 10000 AND COUNT(p.p_id) > 3;

-- 6
SELECT p.*
FROM payment p 
JOIN budgets b ON p.p_year = b.b_year 
WHERE p.p_year = 2023 AND p.in_or_out = 'in';

-- 7
SELECT e.e_id, e.name, e.salary, s.neto_salary
FROM employee e
NATURAL JOIN salary s
WHERE (e.salary - s.neto_salary) <= 2000;

-- 8
SELECT i.id_Consumer, COUNT(*) AS total_purchases
FROM in_Purchases_from i
NATURAL JOIN payment p
WHERE EXTRACT(YEAR FROM p.p_date) = 2023
GROUP BY i.id_Consumer
HAVING COUNT(*) < 2;

-- DELETE queries
-- 1
DELETE FROM out_Purchase_for_the_winery
WHERE p_id IN (
  SELECT pfw.p_id
  FROM out_Purchase_for_the_winery pfw
  NATURAL JOIN payment p
  WHERE p.p_date < '2023-01-01'
);

-- 2
DELETE FROM Purchase_from_the_winery
WHERE id_Consumer IN (
  SELECT id_Consumer
  FROM in_Purchases_from
  GROUP BY id_Consumer
  HAVING COUNT(*) < 2
);

-- 3
DELETE FROM Purchase_from_the_winery
WHERE id_Consumer IN (
  SELECT id_Consumer
  FROM in_Purchases_from
  NATURAL JOIN payment
  WHERE EXTRACT(YEAR FROM p_date) IS DISTINCT FROM 2024
);

-- UPDATE queries
-- 1
UPDATE Investments
SET profit_Percentage = 15
WHERE id_Investor IN (
  SELECT ii.id_Investor
  FROM in_Investments ii
  NATURAL JOIN payment p
  WHERE p.p_sum > 10000
);

-- 2
UPDATE employee
SET salary = salary * 1.10
WHERE e_id IN (
  SELECT e_id
  FROM salary
  GROUP BY e_id
  HAVING COUNT(*) >= 3
);

-- 3
UPDATE taxes
SET percent = 8
WHERE t_id IN (
  SELECT ot.t_id
  FROM out_taxes ot
  NATURAL JOIN payment p
  WHERE p.year = 2022
);
