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
8. [שלב ג- אינטגרציה ומבטים](#דוח-פרויקט--שלב-ג)
9. [שלב ד- תכנות](#דוח-פרויקט--שלב-ד)
10. [שלב ה- ממשק גרפי](#שלב-ה-–-מערכת-לניהול-עובדים-סיורים-ותשלומים)


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

# דוח פרויקט – שלב ג
## אגף מרכז מבקרים- ERD
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%92/ERD_MERCAZ_MEVAKRIM.png?raw=true)

## אגף מרכז מבקרים- DSD
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%92/DSD%20mercaz%20mevacrim.jpeg?raw=true)

## אינטגרציה -ERD
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%92/ERD%20Integration.png?raw=true)

## אינטגרציה- DSD
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%92/DSD%20INTEGRETION.png?raw=true)


## החלטות שנעשו בשלב האינטגרציה

### עקרונות שהנחו אותנו:
- לאחד טבלאות בעלות תפקיד דומה (כגון payment).
- לשמור עקביות בשמות עמודות ומפתחות.
- לייעל את הסכימה כדי למנוע כפילויות ולהקל על שליפות.

### טבלאות שאוחדו:

#### 1. payment + payment:
שתי הטבלאות ייצגו תשלומים מסוגים שונים – שכר עובדים, רכישות, הכנסות מתיירים ועוד.
הן אוחדו לטבלה אחת בשם payment.
נוספה עמודה חדשה: payment_type אשר מתארת את מקור או סוג התשלום (לדוגמה: salary, tour_income, purchase, investment וכו').

#### 2. employee + guide:
מדריכים הם תת-קבוצה של עובדים ולכן איחדנו את שתי הטבלאות לטבלה אחת בשם employee.
בטבלה החדשה נוספה עמודה role, עם ערכים כגון guide, admin, worker וכו'.
שדות ייחודיים למדריכים כמו:
- languages – שפות שהמדריך דובר.
- guided – מספר סיורים שהדריך.

הוכנסו לטבלה עם ערכים רלוונטיים למדריכים, וערכי ברירת מחדל (עברית) לשאר העובדים.


## הסבר מילולי של התהליך והפקודות

### שינויים בטבלת employee
```sql
ALTER TABLE employee ADD COLUMN employee_role TEXT;           -- למשל 'guide', 'worker'
ALTER TABLE employee ADD COLUMN languages TEXT;      -- רק למדריכים
ALTER TABLE employee ADD COLUMN guided INTEGER;      -- רק למדריכים
```
#### הוספת שדות:
- `employee_role` (`TEXT`)  
  משמש לציון תפקיד העובד (למשל: `"guide"`, `"worker"`).

- `languages` (`TEXT`)  
  מציין אילו שפות מדריך מדבר. רלוונטי רק לעובדים בתפקיד מדריך.

- `guided` (`INTEGER`)  
  שדה מספרי לציון כמה הדרכות העובד ביצע.

---

### שינויים בטבלת התשלומים (`payment`)

```sql
ALTER TABLE payment ADD COLUMN payment_type TEXT;      -- מקור התשלום:
```
#### הוספת שדות:
- `payment_type` (`TEXT`)  
  מציין את מקור התשלום, לדוגמה: Credit, Bank Transfer, Bit .


#### הוספת קשרים (Foreign Keys):
```sql
ALTER TABLE payment
ADD CONSTRAINT fk_payment_employee
FOREIGN KEY (e_id) REFERENCES employee(e_id);
```

- `e_id` → `employee(e_id)`  
  קישור של תשלום לעובד (למשל כאשר עובד שילם על שירות מסוים).

- `visitorid` → `visitor(visitorid)`  
  קישור של תשלום למבקר.

---

### שינויים בטבלת הסיורים (`tour`)
```sql
ALTER TABLE tour
ADD CONSTRAINT fk_tour_guide
FOREIGN KEY (guide_id) REFERENCES employee(e_id);
```
#### הוספת קשר:
- `guide_id` → `employee(e_id)`  
  כל מדריך סיור חייב להיות עובד קיים בטבלת `employee`.


#### הכנסת נתונים לטבלאות:
```sql
UPDATE employee e
SET 
    employee_role = 'guide',
    languages = g.languages,
    guided = g.guided
FROM guide g
WHERE e.e_id = g.guide_id;
```
##### הסבר:
אחרי שיצרנו את העמודות החדשות, משכנו ערכים מטבלת guide לפי ההתאמה של הid של העובדים
```sql
INSERT INTO payments_table (p_id, p_date, in_or_out, p_sum, p_year, e_id, payment_type)
SELECT
    p1.paymentid,
    p1.paymentdate,
    'in',
    p1.amount,
    EXTRACT(YEAR FROM p1.paymentdate),
    NULL,
    payment method 
FROM payment1 p1;
```
##### הסבר:
המרנו נתונים מהטבלה payment למבנה הטבלה החדשה תוך חישוב והתאמת שדות כמו תאריך, שנה וסוג תשלום. קראנו לטבלה payment של הבסיס נתונים של המרכז מבקרים payment1 כדי שלא יהיו לנו כפילויות של טבלאות בבסיס נתונים המשותף לפני השינויים.

#### הכנסת ערכי ברירת מחדל:
```sql
ALTER TABLE employee
ALTER COLUMN guide SET DEFAULT 'worker';
```
כל עובד שהוא לא מדריך- הוא עובד פשוט
```sql
ALTER TABLE employee
ALTER COLUMN languege SET DEFAULT 'עברית';
```
כל עובד שלא מדריך- דובר רק שפה עברית אלא אם הוגדר אחרת
```sql
ALTER TABLE employee
ALTER COLUMN guided SET DEFAULT 0;
```
כל עובד שלא מדריך- לא הדריף אף פעם ולכן הדריך 0 סיורים
```sql
ALTER TABLE payment
ALTER COLUMN payment_type SET DEFAULT 'credit';
```
שיטת התשלום הרגילה היום היא דרך כרטיס אשראי ולכן זה הברירת מחדל

---
---

### סיכום

שינויים אלו מאפשרים:
- הבדלה בין סוגי עובדים.
- מעקב אחר שפות הדרכה וניסיון הדרכתי.
- שיוך תשלומים לסוג.
- הגדרת קשרים בין סיורים, מדריכים, תשלומים ומבקרים.


## ֿ מבט 1 – `view_tours_with_guide_info`

###  תיאור מילולי:
מבט זה מאחד מידע מטבלת הסיורים (tour) עם מידע על מדריכים מטבלת העובדים (employee), וכולל רק עובדים בעלי תפקיד `guide`.
המבט מציג: מזהה סיור, מחיר, תיאור, כמות משתתפים, שם המדריך, שפות שהוא דובר, וכמות סיורים שהעביר.

```sql
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
    employee e ON t.guideid = e.e_id
WHERE 
    e.employee_role = 'guide';

```


---

###  שאילתה 1:
#### תיאור:
מציגה את סך ההכנסות מכל סיור (מחיר * כמות משתתפים) עבור כל מדריך.
```sql
SELECT 
    guide_name,
    SUM(price * amount) AS total_income
FROM 
    view_tours_with_guide_info
GROUP BY 
    guide_name;
```

![](DBProject/שלב%20ג/m1.1.png)
---

###  שאילתה 2:
#### תיאור:
מציגה את כל הסיורים שמחירם גבוה מהממוצע בכלל הסיורים.
```sql
SELECT * 
FROM view_tours_with_guide_info
WHERE price > (
    SELECT AVG(price) 
    FROM view_tours_with_guide_info
);
```

![](DBProject/שלב%20ג/m1.2.png)

---

##  מבט 2 – `view_employee_payments`

###  תיאור מילולי:
מבט זה מאחד בין טבלת התשלומים (payment) וטבלת העובדים (employee), ומציג מידע מלא על כל תשלום שבוצע לעובד:
מזהה תשלום, תאריך, סכום, סוג תשלום, האם מדובר בהכנסה או הוצאה, שם העובד ותפקידו.

```sql
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

```


---

###  שאילתה 1:
#### תיאור:
למצוא את סכום התשלומים הכולל שביצע כל עובד בתפקיד מסוים, לפי סוג תשלום (הכנסה/הוצאה), ולמיין לפי הסכום הגבוה ביותר..
```sql
SELECT 
    employee_name,
    employee_role,
    in_or_out,
    SUM(p_sum) AS total_payment
FROM 
    view_employee_payments
GROUP BY 
    employee_name, employee_role, in_or_out
HAVING 
    SUM(p_sum) > 10000
ORDER BY 
    total_payment DESC;

```

![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%92/m2.1.png)

---

###  שאילתה 2:
#### תיאור:
מציגה את כל התשלומים (הכנסות והוצאות) כאשר סכומי ההוצאות מוצגים כסכום שלילי – לצורך ניתוח תקציבי.
```sql
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
```
![](DBProject/שלב%20ג/m2.2.png)

# דוח פרויקט – שלב ד

---
### כדי שהתוכנית תהיה משמעותית, הוספנו את הטבלה 'summary_report'
הטבלה נועדה לרכז את סך כל התשלומים שקיבל כל עובד בכל יום לצורך מעקב ובקרה.
היא מתעדכנת אוטומטית דרך טריגר ופרוצדורה בכל הוספת תשלום חדש.
```sql
CREATE TABLE summary_report (
    emp_id INTEGER,
    total_amount NUMERIC,
    report_date DATE,
    PRIMARY KEY (emp_id, report_date)
);
```
## פונקציה 1: חישוב סה"כ תשלום למדריך לפי מזהה

### תיאור:
פונקציה שמחזירה REF CURSOR של כל התשלומים למדריך מסוים ומחשבת את סכום התשלומים הכולל.

### קוד:
```sql
CREATE OR REPLACE FUNCTION fn_total_payment_for_guide(guide_id_input INTEGER)
RETURNS REFCURSOR AS $$
DECLARE
    total_sum NUMERIC := 0;
    rec RECORD;
    ref REFCURSOR;
BEGIN
    
    OPEN ref FOR 
        SELECT * FROM payment WHERE e_id = guide_id_input;


    FOR rec IN SELECT p_sum FROM payment WHERE e_id = guide_id_input LOOP
        total_sum := total_sum + rec.p_sum;
    END LOOP;

  
    RAISE NOTICE 'Total payment for guide ID %: %', guide_id_input, total_sum;

    RETURN ref;
END;
$$ LANGUAGE plpgsql;

```

### הוכחת ריצה:
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%94%D7%95%D7%9B%D7%97%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%A4%D7%95%D7%A0%D7%A7%D7%A6%D7%99%D7%94%201.png)

---

## פונקציה 2: מדריכים עם ניסיון מעל N סיורים

### תיאור:
מחזירה טבלה של מדריכים שביצעו יותר מ־N סיורים.

### קוד:
```sql
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

```

### הוכחת ריצה:
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%94%D7%95%D7%9B%D7%97%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%A4%D7%95%D7%A0%D7%A7%D7%A6%D7%99%D7%94%202%20.png)

---

## פרוצדורה 1: עדכון תפקיד עובד

### תיאור:
פרוצדורה שבודקת אם העובד קיים ואם כן מעדכנת את תפקידו, אחרת זורקת חריגה.

### קוד:
```sql
CREATE OR REPLACE PROCEDURE pr_update_employee_role(emp_id INTEGER, new_role TEXT)
AS $$
BEGIN
 
    IF NOT EXISTS (SELECT 1 FROM employee WHERE e_id = emp_id) THEN
        RAISE EXCEPTION 'No such employee with ID: %', emp_id;
    END IF;

    UPDATE employee SET role = new_role WHERE e_id = emp_id;
    RAISE NOTICE 'Role updated successfully for employee %', emp_id;
END;
$$ LANGUAGE plpgsql;

```

### הוכחת ריצה:
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%94%D7%95%D7%9B%D7%97%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%A4%D7%A8%D7%95%D7%A6%D7%93%D7%95%D7%A8%D7%94%201.png)

---

## פרוצדורה 2: דו"ח תשלומים לכל עובד

### תיאור:
יוצרת או מעדכנת סיכום תשלומים לפי עובד בתאריך של היום, כולל שימוש בלולאה ו־DML.

### קוד:
```sql
CREATE OR REPLACE PROCEDURE pr_generate_payment_summary()
AS $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN SELECT e_id, SUM(p_sum) as total FROM payment GROUP BY e_id LOOP
        INSERT INTO summary_report(emp_id, total_amount, report_date)
        VALUES (r.e_id, r.total, CURRENT_DATE)
        ON CONFLICT (emp_id, report_date) DO UPDATE SET total_amount = r.total;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
```

### הוכחת ריצה:
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%94%D7%95%D7%9B%D7%97%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%A4%D7%A8%D7%95%D7%A6%D7%93%D7%95%D7%A8%D7%94%202.png)
---

## טריגר 1: בדיקת קיום עובד לפני הכנסת תשלום

### קוד:
```sql
CREATE OR REPLACE FUNCTION trg_check_employee_exists()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM employee WHERE e_id = NEW.e_id) THEN
        RAISE EXCEPTION 'Employee ID % does not exist', NEW.e_id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_before_payment_insert
BEFORE INSERT ON payment
FOR EACH ROW EXECUTE FUNCTION trg_check_employee_exists();
```

---

## טריגר 2: עדכון summary_report אחרי הכנסת תשלום

### קוד:
```sql
CREATE OR REPLACE FUNCTION trg_update_summary()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO summary_report(emp_id, total_amount, report_date)
    VALUES (NEW.e_id, NEW.p_sum, CURRENT_DATE)
    ON CONFLICT (emp_id, report_date)
    DO UPDATE SET total_amount = summary_report.total_amount + NEW.p_sum;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_after_payment_insert
AFTER INSERT ON payment
FOR EACH ROW EXECUTE FUNCTION trg_update_summary();
```

---

## תוכנית ראשית 1: הפעלת פונקציה ופרוצדורה

```sql
DO $$
DECLARE
    c REFCURSOR;
BEGIN
    c := fn_total_payment_for_guide(2);      
    CALL pr_update_employee_role(2, 'admin'); 
END;
$$;

```
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%AA%D7%95%D7%A6%D7%90%D7%95%D7%AA%20%D7%94%D7%A8%D7%A6%D7%94%20%D7%AA%D7%95%D7%9B%D7%A0%D7%99%D7%AA%201.png)
---

## תוכנית ראשית 2: הפעלת פונקציה 2 ופרוצדורה 2

```sql
DO $$
BEGIN
    CALL pr_generate_payment_summary();
    PERFORM * FROM fn_guides_with_experience(10);
END;
$$;
```
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%94%D7%95%D7%9B%D7%97%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%AA%D7%95%D7%9B%D7%A0%D7%99%D7%AA%202.png)
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%93/%D7%AA%D7%95%D7%A6%D7%90%D7%95%D7%AA%20%D7%A8%D7%99%D7%A6%D7%94%20%D7%AA%D7%95%D7%9B%D7%A0%D7%99%D7%AA%202.png)

# שלב ה' – מערכת לניהול עובדים, סיורים ותשלומים

מערכת זו נבנתה בשפת Python עם חיבור למסד PostgreSQL. המערכת מאפשרת ניהול עובדים, סיורים, תלושי שכר ודוחות סיכום באופן גרפי ואינטראקטיבי.

---

## הוראות הפעלה של האפליקציה

1. ודא שהמערכת עומדת בדרישות הבאות:
   - מותקן Python 3.10+
   - מסד PostgreSQL פעיל עם:
     - host: localhost
     - port: 5433
     - dbname: stage5
     - user: postgres
     - password: 16040010

2. הפעל את הקובץ:
   ```
   python opening_screen.py
   ```

3. יוצג סרטון פתיחה. ניתן ללחוץ "דלג" או להמתין לסיומו. לאחר מכן יוצג המסך הראשי של המערכת.

---

## מבנה המסכים והמעברים

### 1. opening_screen.py – מסך פתיחה
- מציג סרטון וידאו במסך מלא.
- כפתור “דלג” מאפשר מעבר מהיר.
- בסיום הסרטון מוצג המסך הראשי של המערכת (Landing Page).

### המסך הראשי של המערכת (נמצא בתוך opening_screen.py)

מרכז הניווט של המערכת – מכיל 4 כפתורים עיקריים:

#### ניהול עובדים (employee.py)
- טבלת עובדים: ת”ז, שם, תפקיד.
- פעולות: הוספה, עדכון, מחיקה.
- לכל עובד כפתורים:
  - ניהול תלושים (SalaryManager.py)
  - ניהול סיורים (TourManagerApp.py)

#### סיכום תשלומים (summary_screen.py)
- מפעיל את הפרוצדורה `pr_generate_payment_summary`
- מציג את תוכן הטבלה `summary_report`

#### מדריכים עם ניסיון (guides_experience_screen.py)
- מקבל מהמשתמש מספר סיורים מינימלי
- מציג מדריכים עם ניסיון מעל ערך זה
- משתמש בפונקציה `fn_guides_with_experience`

#### גרף השוואתי בין מדריכים (compare_visitors_guides.py)
- מבצע חישוב כמות משתתפים לפי מדריך
- מציג גרף באמצעות matplotlib
- נגיש מהתפריט הראשי

---

## מסכים פנימיים שנפתחים מתוך employee.py

### SalaryManager.py – ניהול תלושי שכר
- מציג תלושים לעובד נבחר
- פעולות: הוספה, עדכון, מחיקה
- כולל יצוא לקובץ Excel

### TourManagerApp.py – ניהול סיורים
- מציג את הסיורים של המדריך
- פעולות: הוספה, עדכון, מחיקה
- מחשב סך הכנסות לכל סיור

---

## תמונות מסך

### מסך פתיחה  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/opening_screen.png)

### תפריט ראשי  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/selection_screen.png)

### ניהול עובדים  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/employee_management.png)

### ניהול תלושי שכר  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/salary_reports.png)

### דוח סיכום תשלומים  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/summary_reports.png)

### מדריכים עם ניסיון  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/experienced_guides.png)

### גרף השוואת מדריכים  
![](https://github.com/estisellam/department-finance---winery/blob/main/DBProject/%D7%A9%D7%9C%D7%91%20%D7%94/guide_comparison.png)

## שאילתות, פרוצדורות ופונקציות בשימוש בפועל

### employee.py
- SELECT * FROM employee;
- INSERT INTO employee (...);
- UPDATE employee SET ...;
- DELETE FROM employee WHERE ...;

### SalaryManager.py
- SELECT payslip_number, neto_salary, payslip_date FROM salary WHERE e_id = %s;
- DELETE FROM salary WHERE payslip_number = %s;

### TourManagerApp.py
- SELECT tourid, price * amount AS total FROM tour WHERE guideid = %s;
- DELETE FROM tour WHERE tourid = %s;

### summary_screen.py
- CALL pr_generate_payment_summary();
- SELECT * FROM summary_report;

### guides_experience_screen.py
- SELECT * FROM fn_guides_with_experience(min_tours);

---

## סיכום

לאחר הצגת הסרטון, מוצג תפריט ראשי שמרכז את כל הרכיבים: ניהול עובדים, תלושים, סיורים ודוחות. כל כפתור פותח ממשק עצמאי, המחובר למסד הנתונים ומאפשר עבודה מלאה עם הנתונים בהתאם לצורך.
