<<<<<<< HEAD
DO $$
DECLARE
    c REFCURSOR;
BEGIN
    c := fn_total_payment_for_guide(2);        -- הפעלת הפונקציה עם מזהה מדריך 2
    CALL pr_update_employee_role(2, 'admin');  -- שינוי תפקידו ל-admin
END;
$$;
=======
DO $$
DECLARE
    c REFCURSOR;
BEGIN
    c := fn_total_payment_for_guide(2);        -- הפעלת הפונקציה עם מזהה מדריך 2
    CALL pr_update_employee_role(2, 'admin');  -- שינוי תפקידו ל-admin
END;
$$;
>>>>>>> ce0a45f105caf80e9ae7d3947b6540b491f556a7
