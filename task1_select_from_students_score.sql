--Показати ПІБ усіх студентів з мінімальною оцінкою у вказаному діапазоні.
SELECT *
FROM STUDENTS_SCORE
WHERE SUBJECT_MIN_ASCORE BETWEEN 20 AND 40;

--Показати інформацію про студентів, яким виповнилося 20 років.
SELECT *
FROM STUDENTS_SCORE
WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) >= 20;

--Показати інформацію про студентів з віком, у вказаному діапазоні.
SELECT *
FROM STUDENTS_SCORE
WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) BETWEEN 18 AND 23;

--Показати інформацію про студентів із конкретним ім’ям. Наприклад, показати студентів з ім’ям Борис.
SELECT *
FROM STUDENTS_SCORE
WHERE FIRST_NAME = 'Ethan';

--Показати інформацію про студентів, в номері яких є три сімки.
SELECT *
FROM STUDENTS_SCORE
WHERE CONTACT_PHONE LIKE '%7%7%7%';

--Показати електронні адреси студентів, що починаються з конкретної літери.
SELECT *
FROM STUDENTS_SCORE
WHERE EMAIL LIKE 'w%';
