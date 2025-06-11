<<<<<<< HEAD
DO $$
BEGIN
    CALL pr_generate_payment_summary();
    PERFORM * FROM fn_guides_with_experience(10);
END;
$$;
=======
DO $$
BEGIN
    CALL pr_generate_payment_summary();
    PERFORM * FROM fn_guides_with_experience(10);
END;
$$;
>>>>>>> ce0a45f105caf80e9ae7d3947b6540b491f556a7
