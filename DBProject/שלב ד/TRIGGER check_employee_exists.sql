CREATE OR REPLACE FUNCTION trg_check_employee_exists()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM employee WHERE e_id = NEW.e_id) THEN
        RAISE EXCEPTION 'Employee ID % does not exist', NEW.e_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_before_payment_insert
BEFORE INSERT ON payment
FOR EACH ROW EXECUTE FUNCTION trg_check_employee_exists();
