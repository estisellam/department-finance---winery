CREATE TABLE summary_report (
    emp_id INTEGER,
    total_amount NUMERIC,
    report_date DATE,
    PRIMARY KEY (emp_id, report_date)
);