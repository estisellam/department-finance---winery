CREATE OR REPLACE PROCEDURE pr_update_employee_role(emp_id INTEGER, new_role TEXT)
AS $$
BEGIN
    -- בדיקה אם העובד קיים
    IF NOT EXISTS (SELECT 1 FROM employee WHERE e_id = emp_id) THEN
        RAISE EXCEPTION 'No such employee with ID: %', emp_id;
    END IF;

    -- עדכון תפקיד העובד
    UPDATE employee SET role = new_role WHERE e_id = emp_id;
    RAISE NOTICE 'Role updated successfully for employee %', emp_id;
END;
$$ LANGUAGE plpgsql;
