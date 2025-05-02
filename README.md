ב״ה
מחלקת כספים ביקב -הסבר על ישויות וכספים:
אסתר הדס וקנין 324966993
תהילה ישראלי 325119493

תיאור הנתונים הנשמרים במערכת:
טבלת תשלומים (payment) – כוללת מזהה תשלום, סכום, תאריך, וסיווג האם מדובר בהוצאה או הכנסה.
עובדים (employee) – לכל עובד יש מזהה, שם, תאריך התחלת עבודה ושכר.
תקציבים (budgets-תקציבים) – כוללים שנת תקציב וסכום מוקצה.
השקעות (השקעות) – מקשרות בין גורם משקיע (משקיע) לסוגי השקעות, עם סכומי השקעה ותשואה.
רכישות ורכיבי קנייה – מעקב אחר רכישות, כולל מידע על הצורך ברכישה, מי רכש, וכמות.
מיסים (מיסים) – כללים על מיסים שונים, סכום מס, ואחוזים.
משכורות (משכורות) – כוללות משכורת נטו, מס הכנסה וכו'.


הפונקציונליות העיקרית במערכת:
מעקב אחר כל תשלום כולל קישור להשקעות, משכורות ורכישות.
חישוב משכורות נטו לעובדים לאחר ניכוי מסים.
ניהול תקציבים ובדיקת הוצאות מול הכנסות.
מעקב אחר רכישות – מי רכש, מה נקנה, וכמות.
חישוב מסים לפי חוקים והגדרות מותאמות.







החלטות עיצוב ונימוקים:
ריכוז התשלומים בישות אחת (payment) – כל התשלומים במערכת (משכורות, רכישות, השקעות) מנוהלים דרך ישות מרכזית אחת. זה מאפשר גישה אחידה לכל סוגי ההוצאות וההכנסות.
קישור ישיר בין תשלומים לרכישות, משכורות והשקעות – לכל תשלום ניתן לשייך את מקורו (לדוגמה: רכישה, משכורת, השקעה), מה שמאפשר מעקב ברור אחר סוגי התנועות הכספיות.
פיצול ישות הרכישה – הרכישות מחולקות לרכישה כללית ורכישת רכיב ספציפי, כך שניתן לפרט כל רכישה לרמת הפריטים שנקנו, הכמות והמחיר ליחידה.
ניהול משכורות בנפרד עם חישובי מס – הפרדת המשכורות מאפשרת לחשב משכורת נטו על בסיס מס הכנסה וחוקים שונים.
שימוש בישות תקציב (budgets-תקציבים) – מאפשר מעקב אחר הגבלת הוצאות והשוואה מול הסכומים המתוקצבים לכל שנה.
ניהול מסים בנפרד – במקום לשמור אחוזי מס בתוך תשלומים, ישות נפרדת למסים מאפשרת לעדכן חוקים משתנים ללא שינוי מבנה בסיס הנתונים.





תרשים ERD מחלקת כספים ביקב
קישור- https://erdplus.com/edit-diagram/790391ba-6f06-41c1-a01f-5b97b7cf2e96







תרשים DSD מחלקת כספים ביקב
https://erdplus.com/edit-diagram/62f31d65-48f3-42a1-8cb3-2746b7fb069aקישור  





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
  FOREIGN KEY (t_id) REFERENCES tasxes(t_id)
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





הדרכים בהן השתמשנו ליצירת טבלאות:
כתיבת סקריפט בפייתון
script in python
mockaroo
generatdata









