CREATE OR REPLACE FUNCTION trg_update_summary()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO summary_report(emp_id, total_amount, report_date)
    VALUES (NEW.e_id, NEW.p_sum, CURRENT_DATE)
    ON CONFLICT (emp_id, report_date)
    DO UPDATE SET total_amount = summary_report.total_amount + NEW.p_sum;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_after_payment_insert
AFTER INSERT ON payment
FOR EACH ROW EXECUTE FUNCTION trg_update_summary();