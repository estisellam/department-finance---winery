
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
ֿ
---

## 🔹 דוגמאות מתוך צילומי מסך

### 1. SELECT – עובדים שאחראים על השקעות
```sql
SELECT DISTINCT e.e_id, e.e_name
FROM employee e
NATURAL JOIN payment p
NATURAL JOIN in_Investments i
ORDER BY e.e_name ASC;
```
**הרצה:**  
![הרצה](./שלב%20ב/שאילתה%207.47.40-2%202025-05-09%20update%201.png)

**תוצאה:**  
![תוצאה](./שלב%20ב/שאילתה%207.59.05-3%202025-05-09%20update%202.png)

---

### 2. UPDATE – אחוז רווח למשקיעים עם תשלום גבוה
```sql
BEGIN;
UPDATE Investments
SET profit_Percentage = 15
WHERE id_Investor IN (
  SELECT ii.id_Investor
  FROM in_Investments ii
  NATURAL JOIN payment p
  WHERE p.p_sum > 10000
);
ROLLBACK;
```

**לפני:**  
![לפני](./שלב%20ב/שאילתה%207.49.47-3%202025-05-09%20update%201.png)

**הרצה:**  
![הרצה](./שלב%20ב/שאילתה%207.50.02-3%202025-05-09%20update%201.png)

**אחרי:**  
![אחרי](./שלב%20ב/שאילתה%208.00.03-2%202025-05-09%20update%202.png)

---

### 3. אילוץ – NOT NULL על employee.e_name
```sql
ALTER TABLE employee
ALTER COLUMN e_name SET NOT NULL;

INSERT INTO employee (e_id, e_name, job_start_date, salary)
VALUES (777, NULL, '2022-01-01', 8000);
```

**ניסיון הפרה:**  
![אילוץ 1](./שלב%20ב/אילוץ%201%208.15.58.png)

---

### 4. אילוץ – CHECK על neto_salary <= salary
```sql
ALTER TABLE salary
ADD CONSTRAINT check_net_salary
CHECK (neto_salary <= salary);

INSERT INTO salary (e_id, neto_salary)
VALUES (1, 999999);
```

**ניסיון הפרה:**  
![אילוץ 2](./שלב%20ב/אילוץ%202%208.18.14.png)

---

### 5. אילוץ – DEFAULT על taxes.percent
```sql
ALTER TABLE taxes
ALTER COLUMN percent SET DEFAULT 17;

INSERT INTO taxes (t_id, taxname, principal_amount)
VALUES (999, 'מס ניסיון', 10000);
```

**תוצאה:**  
![אילוץ 3](./שלב%20ב/אילוץ%203%208.19.22.png)

---

### 6. Rollback Example
```sql
BEGIN;
UPDATE employee SET salary = salary * 1.10 WHERE e_id = 1;
ROLLBACK;
```

**צילום תוצאה לאחר Rollback:**  
![rollback](./שלב%20ב/שאילתה%208.02.65-3%202025-05-09%20update%203.png)

---

### 7. Commit Example
```sql
BEGIN;
UPDATE employee SET salary = salary * 1.10 WHERE e_id = 1;
COMMIT;
```

**צילום תוצאה לאחר Commit:**  
![commit](./שלב%20ב/שאילתה%208.03.07-3%202025-05-09%20update%203.png)

---

📦 כל התמונות צורפו בתיקיית `שלב ב` לפי שמות קבצים ברורים לכל שאילתה.


*הפרויקט נבנה בשימוש PostgreSQL וכלי pgAdmin 4.*
