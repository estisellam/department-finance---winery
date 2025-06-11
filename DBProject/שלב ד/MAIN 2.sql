DO $$
BEGIN
    CALL pr_generate_payment_summary();
    PERFORM * FROM fn_guides_with_experience(10);
END;
$$;
