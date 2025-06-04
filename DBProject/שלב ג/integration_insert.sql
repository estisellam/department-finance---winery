INSERT INTO payment (payment_id, amount, payment_date, e_id, visitorid, payment_type)
SELECT 
    p1.payment_id,
    p1.amount,
    p1.payment_date,
    p1.e_id,
    p1.visitorid,
    'salary' AS payment_type   -- או כל תיאור מתאים למקור הנתון
FROM payment1 p1;


UPDATE employee e
SET 
    employee_role = 'guide',
    languages = g.languages,
    guided = g.guided
FROM guide g
WHERE e.e_id = g.guide_id;
