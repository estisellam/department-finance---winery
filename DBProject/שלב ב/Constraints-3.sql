
-- אילוץ 1: תאריך תשלום חייב להיות קיים
ALTER TABLE payment
ALTER COLUMN p_date SET NOT NULL;

-- אילוץ 2: סכום תשלום חייב להיות חיובי
ALTER TABLE payment
ADD CONSTRAINT check_positive_payment
CHECK (p_sum > 0);

-- אילוץ 3: שם העובד לא יכול להיות ריק
ALTER TABLE employee
ALTER COLUMN e_name SET NOT NULL;
