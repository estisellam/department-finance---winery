ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

ALTER TABLE employee
ADD CONSTRAINT check_positive_salary
CHECK (salary > 0);

ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;
