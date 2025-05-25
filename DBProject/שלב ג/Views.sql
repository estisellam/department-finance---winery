
-- יצירת מבט 1: view_tours_with_guide_info
CREATE VIEW view_tours_with_guide_info AS
SELECT 
    t.tourid,
    t.price,
    t.description,
    t.amount,
    e.e_name AS guide_name,
    e.languages,
    e.guided_tours
FROM 
    tour t
JOIN 
    employee e ON tourid = e.e_id
WHERE 
    e.employee_role = 'guide';

-- שאילתה 1 על view_tours_with_guide_info: סך ההכנסות מכל סיור לפי מדריך
SELECT 
    guide_name,
    SUM(price * amount) AS total_income
FROM 
    view_tours_with_guide_info
GROUP BY 
    guide_name;

-- שאילתה 2 על view_tours_with_guide_info: סיורים שמחירם מעל הממוצע
SELECT * 
FROM view_tours_with_guide_info
WHERE price > (
    SELECT AVG(price) 
    FROM view_tours_with_guide_info
);

-- יצירת מבט 2: view_employee_payments
CREATE VIEW view_employee_payments AS
SELECT 
    p.p_id,
    p.p_date,
    p.p_sum,
    p.payment_type,
    p.in_or_out,
    e.e_name AS employee_name,
    e.employee_role
FROM 
    payment p
JOIN 
    employee e ON p.e_id = e.e_id;

-- שאילתה 1 על view_employee_payments: כל תשלומי השכר ממוינים לפי סכום
SELECT 
    employee_name,
    employee_role,
    p_sum,
    p_date
FROM 
    view_employee_payments
WHERE 
    payment_type = 'salary'
ORDER BY 
    p_sum DESC;

-- שאילתה 2 על view_employee_payments: כל התשלומים עם סימון חיובי/שלילי לסכום
SELECT 
    p_date,
    employee_name,
    employee_role,
    payment_type,
    in_or_out,
    CASE 
        WHEN in_or_out = 'in' THEN p_sum
        ELSE -p_sum
    END AS signed_amount
FROM 
    view_employee_payments
ORDER BY 
    p_date DESC;
