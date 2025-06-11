CREATE OR REPLACE PROCEDURE pr_generate_payment_summary()
AS $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN SELECT e_id, SUM(p_sum) as total FROM payment GROUP BY e_id LOOP
        INSERT INTO summary_report(emp_id, total_amount, report_date)
        VALUES (r.e_id, r.total, CURRENT_DATE)
        ON CONFLICT (emp_id, report_date) DO UPDATE SET total_amount = r.total;
    END LOOP;
END;
$$ LANGUAGE plpgsql;