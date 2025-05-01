-- הכנסת נתונים לטבלת budgets
INSERT INTO budgets (b_year, b_sum) VALUES (2023, 500000);
INSERT INTO budgets (b_year, b_sum) VALUES (2024, 600000);
INSERT INTO budgets (b_year, b_sum) VALUES (2025, 700000);

-- הכנסת נתונים לטבלת employee
INSERT INTO employee (e_id, e_name, job_start_date, salary) VALUES (101, 'Alice', '2020-06-15', 55000);
INSERT INTO employee (e_id, e_name, job_start_date, salary) VALUES (102, 'Bob', '2019-08-21', 60000);
INSERT INTO employee (e_id, e_name, job_start_date, salary) VALUES (103, 'Charlie', '2021-02-10', 48000);

-- הכנסת נתונים לטבלת salary
INSERT INTO salary (neto_salary, payslip_number, down, e_id) VALUES (45000, 201, 10000, 101);
INSERT INTO salary (neto_salary, payslip_number, down, e_id) VALUES (50000, 202, 10000, 102);
INSERT INTO salary (neto_salary, payslip_number, down, e_id) VALUES (38000, 203, 10000, 103);

-- הכנסת נתונים לטבלת tasxes
INSERT INTO tasxes (t_id, t_percent, TaxName, principal_amount) VALUES (1, 15, 1000, 15000);
INSERT INTO tasxes (t_id, t_percent, TaxName, principal_amount) VALUES (2, 20, 1200, 20000);
INSERT INTO tasxes (t_id, t_percent, TaxName, principal_amount) VALUES (3, 25, 1300, 25000);

-- הכנסת נתונים לטבלת Investments
INSERT INTO Investments (id_Investor, name_Investor, profit_Percentage) VALUES (301, 'David', 5);
INSERT INTO Investments (id_Investor, name_Investor, profit_Percentage) VALUES (302, 'Eve', 7);
INSERT INTO Investments (id_Investor, name_Investor, profit_Percentage) VALUES (303, 'Frank', 6);

-- הכנסת נתונים לטבלת Winery_purchases
INSERT INTO Winery_purchases (id_Purchase, purchase_need, who_purchased) VALUES (401, 'Grapes', 'Alice');
INSERT INTO Winery_purchases (id_Purchase, purchase_need, who_purchased) VALUES (402, 'Barrels', 'Bob');
INSERT INTO Winery_purchases (id_Purchase, purchase_need, who_purchased) VALUES (403, 'Bottles', 'Charlie');

-- הכנסת נתונים לטבלת Purchase_from_the_winery
INSERT INTO Purchase_from_the_winery (id_Consumer, Quantity_of_wine, PricePerUnit) VALUES (501, 100, 15);
INSERT INTO Purchase_from_the_winery (id_Consumer, Quantity_of_wine, PricePerUnit) VALUES (502, 200, 14);
INSERT INTO Purchase_from_the_winery (id_Consumer, Quantity_of_wine, PricePerUnit) VALUES (503, 150, 16);

-- הכנסת נתונים לטבלת payment
INSERT INTO payment (p_id, p_date, in_or_out, p_sum, p_year, e_id) VALUES (601, '2023-03-10', 'IN', 20000, 2023, 101);
INSERT INTO payment (p_id, p_date, in_or_out, p_sum, p_year, e_id) VALUES (602, '2024-06-15', 'OUT', 15000, 2024, 102);
INSERT INTO payment (p_id, p_date, in_or_out, p_sum, p_year, e_id) VALUES (603, '2025-09-21', 'IN', 25000, 2025, 103);

-- הכנסת נתונים לטבלת out_tasxes
INSERT INTO out_tasxes (p_id, t_id) VALUES (601, 1);
INSERT INTO out_tasxes (p_id, t_id) VALUES (602, 2);
INSERT INTO out_tasxes (p_id, t_id) VALUES (603, 3);

-- הכנסת נתונים לטבלת in_Purchases_from
INSERT INTO in_Purchases_from (p_id, id_Consumer) VALUES (601, 501);
INSERT INTO in_Purchases_from (p_id, id_Consumer) VALUES (602, 502);
INSERT INTO in_Purchases_from (p_id, id_Consumer) VALUES (603, 503);

-- הכנסת נתונים לטבלת out_Purchase_for_the_winery
INSERT INTO out_Purchase_for_the_winery (p_id, id_Purchase) VALUES (601, 401);
INSERT INTO out_Purchase_for_the_winery (p_id, id_Purchase) VALUES (602, 402);
INSERT INTO out_Purchase_for_the_winery (p_id, id_Purchase) VALUES (603, 403);

-- הכנסת נתונים לטבלת in_Investments
INSERT INTO in_Investments (p_id, id_Investor) VALUES (601, 301);
INSERT INTO in_Investments (p_id, id_Investor) VALUES (602, 302);
INSERT INTO in_Investments (p_id, id_Investor) VALUES (603, 303);

-- הכנסת נתונים לטבלת out_salary
INSERT INTO out_salary (p_id, payslip_number) VALUES (601, 201);
INSERT INTO out_salary (p_id, payslip_number) VALUES (602, 202);
INSERT INTO out_salary (p_id, payslip_number) VALUES (603, 203);

