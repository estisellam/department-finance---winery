
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

ALTER TABLE payment
ADD CONSTRAINT check_positive_payment
CHECK (p_sum > 0);

ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;
