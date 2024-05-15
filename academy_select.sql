--Вивести таблицю кафедр, але розташувати її поля у зворотному порядку
SELECT *
FROM DEPARTMENTS
ORDER BY ID DESC;

--Вивести назви груп та їх рейтинги з уточненнями до назв полів відповідно до назви таблиці.
SELECT NAME AS "GROUP NAME", RATING AS "GROUP RATING"
FROM GROUPS;

--Вивести для викладачів їх прізвища, відсоток ставки по відношенню до надбавки та відсоток ставки по відношенню до зарплати (сума ставки та надбавки).
SELECT SURNAME, ROUND((SALARY/PREMIUM)*100) AS "SALARY TO PREMIUM", ROUND((SALARY/(SALARY + PREMIUM)) * 100) AS "SALARY TO TOTAL"
FROM TEACHERS;

--Вивести таблицю факультетів одним полем у такому форматі: «The dean of faculty [faculty] is [dean].».
SELECT CONCAT('The dean of faculty ', NAME, ' is ', DEAN)
FROM FACULTIES;

--Вивести прізвища професорів, ставка яких перевищує 1050.
SELECT SURNAME
FROM TEACHERS
WHERE IS_PROFESSOR = TRUE AND SALARY > 5000::MONEY; 

--Вивести назви кафедр, фонд фінансування яких менший, ніж 11000 або більший за 25000.
SELECT NAME
FROM DEPARTMENTS
WHERE FINANCING < 50000::MONEY OR FINANCING > 60000::MONEY;

--Вивести назви факультетів, окрім факультету «Computer Science».
SELECT NAME
FROM FACULTIES
WHERE LOWER(NAME) NOT LIKE 'faculty of nursing';

--Вивести прізвища та посади викладачів, які не є професорами.
SELECT SURNAME, POSITION
FROM TEACHERS
WHERE IS_PROFESSOR = FALSE;

--Вивести прізвища, посади, ставки та надбавки асистентів, надбавка яких у діапазоні від 160 до 550
SELECT SURNAME, POSITION, SALARY, PREMIUM
FROM TEACHERS
WHERE IS_ASSISTANT = TRUE AND PREMIUM BETWEEN 160::MONEY AND 550::MONEY;

--Вивести прізвища та ставки асистентів.
SELECT SURNAME, SALARY
FROM TEACHERS
WHERE IS_ASSISTANT = TRUE;

--Вивести прізвища та посади викладачів, які були прийняті на роботу до 01.01.2000.
SELECT SURNAME, POSITION
FROM TEACHERS
WHERE EMPLOYMENT_DATE < '2000-01-01';

--Вивести назви кафедр, які в алфавітному порядку розміщені до кафедри «Software Development». Виведене поле
--назвіть «Name of Department».
SELECT NAME AS "NAME OF DEPARTMENT"
FROM DEPARTMENTS
WHERE NAME < 'Law'
ORDER BY NAME;

--Вивести прізвища асистентів із зарплатою (сума ставки та надбавки) не більше 1200.
SELECT SURNAME
FROM TEACHERS
WHERE IS_ASSISTANT = TRUE AND SALARY + PREMIUM <= 4000::MONEY;

--Вивести назви груп 5-го курсу з рейтингом у діапазоні від 2 до 4.
SELECT NAME
FROM GROUPS
WHERE YEAR = 2 AND RATING BETWEEN 2 AND 4;

--Вивести прізвища асистентів зі ставкою менше, ніж 550 або надбавкою менше, ніж 200.
SELECT SURNAME
FROM TEACHERS
WHERE IS_ASSISTANT = TRUE AND SALARY < 3200::MONEY OR PREMIUM < 560::MONEY;