
# מחלקת כספים - פרויקט בסיסי נתונים

**שמות המגישות:**  
- וקנין הדס אסתר – 324966993  
- ישראלי תהילה – 325119493  

**שם המערכת:**  
ניהול כספים ביקב  
**היחידה הנבחרת:**  
מחלקת כספים

---

## תוכן עניינים

1. [מבוא](#מבוא)
2. [תרשים ERD](#תרשים-erd)
3. [תרשים DSD](#תרשים-dsd)
4. [החלטות עיצוב](#החלטות-עיצוב)
5. [שיטות הכנסת נתונים](#שיטות-הכנסת-נתונים)
6. [גיבוי ושחזור נתונים](#גיבוי-ושחזור-נתונים)
7. [שלב ב – שאילתות ועדכונים](#שלב-ב--שאילתות-ועדכונים)

---

## מבוא

### תיאור הנתונים הנשמרים במערכת:

1. **טבלת תשלומים (payment)** – מזהה, סכום, תאריך, סוג (הכנסה/הוצאה)
2. **טבלת עובדים (employee)** – מזהה, שם, תאריך התחלה, שכר
3. **טבלת תקציבים (budgets)** – שנה, סכום
4. **טבלת השקעות (investments)** – מזהה השקעה, משקיע, סכום, תשואה
5. **טבלת רכישות (purchases)** – מידע על מה נרכש, כמה, ומי רכש
6. **טבלת מיסים (taxes)** – סכום, אחוז, כללים משתנים
7. **טבלת משכורות (salary)** – ברוטו, נטו, הפרשים מול מס

### הפונקציונליות העיקרית במערכת:

- קישור תשלום להשקעות / רכישות / משכורות
- חישוב שכר נטו לאחר ניכוי מס
- ניהול תקציב מול הכנסות והוצאות בפועל
- מעקב אחר רכישות לפי צרכן, כמות ומחיר
- חישוב מסים לפי חוקים מותאמים

---

## תרשים ERD



---

## תרשים DSD



---

## החלטות עיצוב

1. ריכוז כל סוגי התשלומים בטבלה אחת (`payment`) לניהול אחיד וקל.
2. קישור ישיר בין `payment` לבין השקעות, רכישות ומשכורות – לשם מעקב ברור אחרי מקור ההוצאה/הכנסה.
3. פיצול רכישות לרכישות כלליות ורכיבי רכישה – לפירוט מלא של מה נקנה.
4. הפרדת משכורות – מאפשרת לחשב שכר נטו לפי חוקי מס משתנים.
5. שימוש בטבלת תקציבים – למעקב שנתי ולהשוואה מול הוצאות.
6. שמירת אחוזי מס בטבלה נפרדת – כך ניתן לעדכן חוקים בלי לשנות את מבנה הטבלאות.

---

## שיטות הכנסת נתונים

### 1. שימוש ב־Mockaroo

[mockarooFiles](https://github.com/estisellam/department-finance---winery/tree/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/mockarooFiles)

### 2. שימוש ב־GENERATEDATA

[generatedataFiles](https://github.com/estisellam/department-finance---winery/tree/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/generatedataFiles)

### 3. סקריפט ב־Python

[scripts folder](https://github.com/estisellam/department-finance---winery/tree/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/python_script)

---

## גיבוי ושחזור נתונים



**קובץ הגיבוי:** `gibuy.sql`  
**קובץ השחזור:** `insertTables.sql`  
בוצע שימוש ב־pgAdmin לייצוא ושחזור הנתונים.

---

## שלב ב – שאילתות ועדכונים


## 🔹 שאילתות UPDATE

### 1. עדכון אחוז רווח למשקיעים עם תשלום מעל 10,000
```sql
UPDATE Investments
SET profit_Percentage = 15
WHERE id_Investor IN (
  SELECT ii.id_Investor
  FROM in_Investments ii
  NATURAL JOIN payment p
  WHERE p.p_sum > 10000
);
```




---

### 2. העלאת שכר ב־10% לעובדים עם 3+ תלושי שכר
```sql
UPDATE employee
SET salary = salary * 1.10
WHERE e_id IN (
  SELECT e_id
  FROM salary
  GROUP BY e_id
  HAVING COUNT(*) >= 3
);
```




---

### 3. הורדת אחוז מס ל־8% עבור תשלומים מ־2022
```sql
UPDATE taxes
SET percent = 8
WHERE t_id IN (
  SELECT ot.t_id
  FROM out_taxes ot
  NATURAL JOIN payment p
  WHERE p.p_year = 2022
);
```




---

## 🔹 שימוש ב־ROLLBACK
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
ROLLBACK;
```




---

## 🔹 שימוש ב־COMMIT
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
COMMIT;
```




---

## 🔹 אילוצים

### 1. NOT NULL על תאריך בתשלומים (payment.p_date)
```sql
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (501, NULL, 5000, 'in');
```


---

### 2. CHECK – סכום תשלום גדול מאפס (payment.p_sum > 0)
```sql
ALTER TABLE payment
ADD CONSTRAINT check_positive_payment
CHECK (p_sum > 0);

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (502, '2023-01-01', 0, 'in');
```


---

### 3. DEFAULT על taxes.percent
```sql
ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;

-- בדיקה
INSERT INTO taxes (t_id, taxname, principal_amount)
VALUES (999, 'מס ניסיון', 10000);
```


---


## 🔹 שאילתות SELECT (1–4)

### 1. עובדים שאחראים על השקעות
```sql
SELECT DISTINCT e.e_id, e.e_name
FROM employee e
NATURAL JOIN payment p
NATURAL JOIN in_Investments i
ORDER BY e.e_name ASC;
```

### 2. רכישות בתאריך 15.6.2023
```sql
SELECT p.p_id, p.p_date, i.id_Consumer
FROM payment p
NATURAL JOIN in_Purchases_from i
WHERE p.p_date = '2023-06-15';
```

### 3. עובדים שהחלו לעבוד לפני 2020
```sql
SELECT e_id, e_name, job_start_date
FROM employee
WHERE job_start_date < '2020-01-01'
ORDER BY job_start_date ASC;
```

### 4. סכום תשלומים נכנסים לפי שנה
```sql
SELECT p_year, SUM(p_sum) AS total_income
FROM payment
WHERE in_or_out = 'in'
GROUP BY p_year
ORDER BY p_year;
```


## 🔹 שאילתות UPDATE

### 1. עדכון אחוז רווח למשקיעים עם תשלום מעל 10,000
```sql
UPDATE Investments
SET profit_Percentage = 15
WHERE id_Investor IN (
  SELECT ii.id_Investor
  FROM in_Investments ii
  NATURAL JOIN payment p
  WHERE p.p_sum > 10000
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-after.png)

---

### 2. העלאת שכר ב־10% לעובדים עם 3+ תלושי שכר
```sql
UPDATE employee
SET salary = salary * 1.10
WHERE e_id IN (
  SELECT e_id
  FROM salary
  GROUP BY e_id
  HAVING COUNT(*) >= 3
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-after.png)

---

### 3. הורדת אחוז מס ל־8% עבור תשלומים מ־2022
```sql
UPDATE taxes
SET percent = 8
WHERE t_id IN (
  SELECT ot.t_id
  FROM out_taxes ot
  NATURAL JOIN payment p
  WHERE p.p_year = 2022
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-after.png)

---


## 🔹 שימוש ב־ROLLBACK
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
ROLLBACK;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-result.png)

---


## 🔹 שימוש ב־COMMIT
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
COMMIT;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-result.png)

---


## 🔹 אילוצים

### 1. NOT NULL על תאריך בתשלומים (payment.p_date)
```sql
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (501, NULL, 5000, 'in');
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint1-error.png)

---

### 2. CHECK – סכום תשלום גדול מאפס (payment.p_sum > 0)
```sql
ALTER TABLE payment
ADD CONSTRAINT check_positive_payment
CHECK (p_sum > 0);

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (502, '2023-01-01', 0, 'in');
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint2-error.png)

---

### 3. DEFAULT על taxes.percent
```sql
ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;

-- בדיקה
INSERT INTO taxes (t_id, taxname, principal_amount)
VALUES (999, 'מס ניסיון', 10000);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint3-default.png)

---


## 🔹 שאילתות SELECT (5–8)

### 5. עובדים עם שכר גבוה ואחריות ל־3+ תשלומים
```sql
SELECT e.e_id, e.e_name, e.salary
FROM employee e
NATURAL JOIN payment p
GROUP BY e.e_id, e.e_name, e.salary
HAVING e.salary > 10000 AND COUNT(p.p_id) > 3;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select05-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select05-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select05-result.png)

---

### 6. כל ההכנסות לשנת 2023
```sql
SELECT p.*
FROM payment p 
JOIN budgets b ON p.p_year = b.b_year 
WHERE p.p_year = 2023 AND p.in_or_out = 'in';
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select06-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select06-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select06-result.png)

---

### 7. עובדים עם הפרש שכר נטו ≤ 2000
```sql
SELECT e.e_id, e.e_name, e.salary, s.neto_salary
FROM employee e
NATURAL JOIN salary s
WHERE (e.salary - s.neto_salary) <= 2000;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select07-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select07-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select07-result.png)

---

### 8. צרכנים עם פחות מ־2 רכישות ב־2023
```sql
SELECT i.id_Consumer, COUNT(*) AS total_purchases
FROM in_Purchases_from i
NATURAL JOIN payment p
WHERE EXTRACT(YEAR FROM p.p_date) = 2023
GROUP BY i.id_Consumer
HAVING COUNT(*) < 2;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select08-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select08-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/select08-result.png)

---


## 🔹 שאילתות UPDATE

### 1. עדכון אחוז רווח למשקיעים עם תשלום מעל 10,000
```sql
UPDATE Investments
SET profit_Percentage = 15
WHERE id_Investor IN (
  SELECT ii.id_Investor
  FROM in_Investments ii
  NATURAL JOIN payment p
  WHERE p.p_sum > 10000
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update01-after.png)

---

### 2. העלאת שכר ב־10% לעובדים עם 3+ תלושי שכר
```sql
UPDATE employee
SET salary = salary * 1.10
WHERE e_id IN (
  SELECT e_id
  FROM salary
  GROUP BY e_id
  HAVING COUNT(*) >= 3
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update02-after.png)

---

### 3. הורדת אחוז מס ל־8% עבור תשלומים מ־2022
```sql
UPDATE taxes
SET percent = 8
WHERE t_id IN (
  SELECT ot.t_id
  FROM out_taxes ot
  NATURAL JOIN payment p
  WHERE p.p_year = 2022
);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/update03-after.png)

---


## 🔹 שימוש ב־ROLLBACK
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
ROLLBACK;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/rollback-result.png)

---


## 🔹 שימוש ב־COMMIT
```sql
BEGIN;
UPDATE employee
SET salary = salary + 123
WHERE e_id = 200;
COMMIT;
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-before.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-run.png)
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-result.png)

---


## 🔹 אילוצים

### 1. NOT NULL על תאריך בתשלומים (payment.p_date)
```sql
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (501, NULL, 5000, 'in');
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint1-error.png)

---

### 2. CHECK – סכום תשלום גדול מאפס (payment.p_sum > 0)
```sql
ALTER TABLE payment
ADD CONSTRAINT check_positive_payment
CHECK (p_sum > 0);

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (502, '2023-01-01', 0, 'in');
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint2-error.png)

---

### 3. DEFAULT על taxes.percent
```sql
ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;

-- בדיקה
INSERT INTO taxes (t_id, taxname, principal_amount)
VALUES (999, 'מס ניסיון', 10000);
```
![](DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/constraint3-default.png)
