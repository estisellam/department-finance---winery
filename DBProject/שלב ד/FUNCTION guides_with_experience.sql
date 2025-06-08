DROP FUNCTION IF EXISTS fn_guides_with_experience(integer);

CREATE OR REPLACE FUNCTION fn_guides_with_experience(min_tours INTEGER)
RETURNS TABLE(e_id NUMERIC, e_name TEXT, guided_tours INTEGER) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        employee.e_id,
        employee.e_name::TEXT,
        employee.guided_tours
    FROM employee
    WHERE employee.employee_role = 'guide' AND employee.guided_tours > min_tours;
END;
$$ LANGUAGE plpgsql;




