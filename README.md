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
7. [שלב ב – שאילתות ועדכונים](#דוח-פרויקט--שלב-ב)

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

![ERD](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/ERD.png?raw=true)

---

## תרשים DSD

![DSD](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/DSD.png?raw=true)

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

![Backup](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%90/%D7%A6%D7%99%D7%9C%D7%95%D7%9D%20%D7%9E%D7%A1%D7%9A%202025-05-02%20%D7%91-9.34.22.png?raw=true)

**קובץ הגיבוי:** `gibuy.sql`  
**קובץ השחזור:** `insertTables.sql`  
בוצע שימוש ב־pgAdmin לייצוא ושחזור הנתונים.

---

# דוח פרויקט – שלב ב
## 🔹 שאילתות select
### 1. כל העובדים שאחראים על השקעות, ממוינים לפי א׳-ב׳
```sql
SELECT DISTINCT e.e_id, e.e_name
FROM employee e
NATURAL JOIN payment p
NATURAL JOIN in_Investments i
;ORDER BY e.e_name ASC
```
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.24.02select4select1.png)
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.24.16select4select1.png)
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.24.19select4select1.png)
---

### 2. כל הרכישות שהתבצעו בתאריך 2024-06-19
```sql
SELECT p.p_id, p.p_date, i.id_Consumer
FROM payment p
NATURAL JOIN in_Purchases_from i
WHERE p.p_date = '2024-06-19';
```
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.30.40select2.png)
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.30.44select2.png)
---
### 3. כל העובדים שהתחילו לעבוד לפני 2020
```sql
SELECT e_id, e_name, job_start_date
FROM employee
WHERE job_start_date < '2020-01-01'
ORDER BY job_start_date ASC;
```
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.37.15select3.png)
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.37.18select3.png)
---

### 4. סך כל הסכום של תשלומים נכנסים בכל שנה
```sql
SELECT p_year, SUM(p_sum) AS total_income
FROM payment
WHERE in_or_out = 'in'
GROUP BY p_year
ORDER BY p_year;
```
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.38.02select4.png)
![](DBProject/שלב%20ב/צילום%20מסך%202025-05-11%20ב-11.38.06select4.png)
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

![לפני](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-before.png?raw=true)  
![הרצה](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-run.png?raw=true)  
![תוצאה](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/commit-result.png?raw=true)

---


## שאילתות DELETE
### 1. מחיקת רכישות מהיקב שבוצעו לפני שנת 2023
```sql
BEGIN;
DELETE FROM out_Purchase_for_the_winery
WHERE p_id IN (
  SELECT pfw.p_id
  FROM out_Purchase_for_the_winery pfw
  NATURAL JOIN payment p
  WHERE p.p_date < '2023-01-01'
);
ROLLBACK;
```
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/delete%201.png)


### 2. מחיקת כל הצרכנים שביצעו פחות מ־2 רכישות

```sql
BEGIN;
DELETE FROM Purchase_from_the_winery
WHERE id_Consumer IN (
  SELECT id_Consumer
  FROM in_Purchases_from
  GROUP BY id_Consumer
  HAVING COUNT(*) < 2
);
ROLLBACK;
```
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/delete%202.png)

### 3. מחיקת צרכנים שלא ביצעו אף רכישה בשנת 2024
```sql
BEGIN;
DELETE FROM Purchase_from_the_winery
WHERE id_Consumer IN (
  SELECT DISTINCT pf.id_Consumer
  FROM in_Purchases_from pf
  WHERE pf.id_Consumer NOT IN (
    SELECT pf2.id_Consumer
    FROM in_Purchases_from pf2
    NATURAL JOIN payment p
    WHERE EXTRACT(YEAR FROM p.p_date) = 2024
  )
);
ROLLBACK;
```
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/delete%203.png)
## 🔹 אילוצים
### 1. אילוץ NOT NULL על תאריך בתשלומים
```sql
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

-- ניסיון הפרה
INSERT INTO payment (p_id, p_date, p_sum, in_or_out)
VALUES (501, NULL, 5000, 'in');
```
---
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/Constraints1.png)
### 2. אילוץ על שכר- שיהיה רק חיוב
```sql
-- הוספת האילוץ
ALTER TABLE employee
ADD CONSTRAINT check_positive_salary
CHECK (salary > 0);

-- ניסיון להפרת האילוץ
INSERT INTO employee (e_id, e_name, start_date, salary)
VALUES (300, 'דוגמה', '2025-01-01', -1000);

```
---
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/Constraints%202.png)
### 3. אילוץ על מיסים- ערך ברירת המחדל של שיעור המס- 17%

```sql
-- הוספת האילוץ
ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;

-- הכנסת רשומה ללא ציון אחוז המס
INSERT INTO taxes (t_id, taxname, principal_amount)
VALUES (999, 'מס ניסיון', 10000);

-- בדיקת הערך שנקבע
SELECT * FROM taxes WHERE t_id = 999;

```

---
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%91/Constraints%203.png)
