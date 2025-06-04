
-- מוסיפים שדות מיוחדים למדריכים
ALTER TABLE employee ADD COLUMN employee_role TEXT;           -- למשל 'guide', 'worker'
ALTER TABLE employee ADD COLUMN languages TEXT;      -- רק למדריכים
ALTER TABLE employee ADD COLUMN guided INTEGER;      -- רק למדריכים


ALTER TABLE payment ADD COLUMN payment_type TEXT;      -- מקור התשלום:



ALTER TABLE payment
ADD CONSTRAINT fk_payment_employee
FOREIGN KEY (e_id) REFERENCES employee(e_id);

ALTER TABLE tour
ADD CONSTRAINT fk_tour_guide
FOREIGN KEY (guide_id) REFERENCES employee(e_id);

UPDATE employee e
SET 
    employee_role = 'guide',
    languages = g.languages,
    guided = g.guided
FROM guide g
WHERE e.e_id = g.guide_id;

INSERT INTO payments_table (p_id, p_date, in_or_out, p_sum, p_year, e_id, payment_type)
SELECT
    p1.paymentid,
    p1.paymentdate,
    'in',
    p1.amount,
    EXTRACT(YEAR FROM p1.paymentdate),
    NULL,
    payment method 
FROM payment1 p1;

ALTER TABLE employee
ALTER COLUMN guide SET DEFAULT 'worker';

ALTER TABLE employee
ALTER COLUMN languege SET DEFAULT 'עברית';

ALTER TABLE employee
ALTER COLUMN guided SET DEFAULT 0;

ALTER TABLE payment
ALTER COLUMN payment_type SET DEFAULT 'credit';


