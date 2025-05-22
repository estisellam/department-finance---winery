
-- מוסיפים שדות מיוחדים למדריכים
ALTER TABLE employee ADD COLUMN employee_role TEXT;           -- למשל 'guide', 'worker'
ALTER TABLE employee ADD COLUMN languages TEXT;      -- רק למדריכים
ALTER TABLE employee ADD COLUMN guided BOOLEAN;      -- רק למדריכים


ALTER TABLE payment ADD COLUMN payment_type TEXT;      -- מקור התשלום:



ALTER TABLE payment
ADD CONSTRAINT fk_payment_employee
FOREIGN KEY (e_id) REFERENCES employee(e_id);

ALTER TABLE tour
ADD CONSTRAINT fk_tour_guide
FOREIGN KEY (guide_id) REFERENCES employee(e_id);

ALTER TABLE payment ADD COLUMN visitorid INTEGER;

ALTER TABLE payment
ADD CONSTRAINT fk_payment_visitor
FOREIGN KEY (visitorid) REFERENCES visitor(visitorid);


