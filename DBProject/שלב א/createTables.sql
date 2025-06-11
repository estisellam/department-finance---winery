CREATE TABLE budgets
(
  b_year INT NOT NULL,
  b_sum INT NOT NULL,
  PRIMARY KEY (b_year)
);

CREATE TABLE employee
(
  e_id NUMERIC(3) NOT NULL,
  e_name VARCHAR(15) NOT NULL,
  job_start_date DATE NOT NULL,
  salary INT NOT NULL,
  PRIMARY KEY (e_id)
);

CREATE TABLE salary
(
  neto_salary INT NOT NULL,
  payslip_number NUMERIC(3) NOT NULL,
  down INT NOT NULL,
  e_id NUMERIC(3) NOT NULL,
  PRIMARY KEY (payslip_number),
  FOREIGN KEY (e_id) REFERENCES employee(e_id)
);

CREATE TABLE taxes
(
  t_id NUMERIC(3) NOT NULL,
  t_percent INT NOT NULL,
  TaxName INT NOT NULL,
  principal_amount INT NOT NULL,
  PRIMARY KEY (t_id)
);

CREATE TABLE Investments
(
  id_Investor NUMERIC(3) NOT NULL,
  name_Investor VARCHAR(15) NOT NULL,
  profit_Percentage INT NOT NULL,
  PRIMARY KEY ( id_Investor)
);

CREATE TABLE Winery_purchases
(
  id_Purchase NUMERIC(3) NOT NULL,
  purchase_need VARCHAR(15) NOT NULL,
  who_purchased VARCHAR(15) NOT NULL,
  PRIMARY KEY (  id_Purchase)
);

CREATE TABLE Purchase_from_the_winery
(
  id_Consumer NUMERIC(3) NOT NULL,
 Quantity_of_wine INT NOT NULL,
  PricePerUnit INT NOT NULL,
  PRIMARY KEY ( id_Consumer )
);

CREATE TABLE payment
(
  p_id NUMERIC(3) NOT NULL,
  p_date DATE NOT NULL,
  in_or_out VARCHAR(3) NOT NULL,
  p_sum INT NOT NULL,
  p_year INT NOT NULL,
  e_id NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id),
  FOREIGN KEY (p_year) REFERENCES budgets(b_year),
  FOREIGN KEY (e_id) REFERENCES employee(e_id)
);

CREATE TABLE out_taxes
(
  p_id NUMERIC(3) NOT NULL,
  t_id NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id, t_id),
  FOREIGN KEY (p_id) REFERENCES payment(p_id),
  FOREIGN KEY (t_id) REFERENCES taxes(t_id)
);

CREATE TABLE in_Purchases_from
(
  p_id NUMERIC(3) NOT NULL,
  id_Consumer NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id, id_Consumer),
  FOREIGN KEY (p_id) REFERENCES payment(p_id),
  FOREIGN KEY (id_Consumer) REFERENCES  Purchase_from_the_winery(id_Consumer)
);

CREATE TABLE out_Purchase_for_the_winery
(
  p_id NUMERIC(3) NOT NULL,
  id_Purchase  NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id, id_Purchase ),
  FOREIGN KEY (p_id) REFERENCES payment(p_id),
  FOREIGN KEY (id_Purchase) REFERENCES Winery_purchases(id_Purchase)
);

CREATE TABLE in_Investments
(
  p_id NUMERIC(3) NOT NULL,
  id_Investor NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id, id_Investor),
  FOREIGN KEY (p_id) REFERENCES payment(p_id),
  FOREIGN KEY (id_Investor) REFERENCES Investments(id_Investor)
);

CREATE TABLE out_salary
(
  p_id NUMERIC(3) NOT NULL,
  payslip_number NUMERIC(3) NOT NULL,
  PRIMARY KEY (p_id,   payslip_number),
  FOREIGN KEY (p_id) REFERENCES payment(p_id),
  FOREIGN KEY (payslip_number) REFERENCES salary(payslip_number)
);
