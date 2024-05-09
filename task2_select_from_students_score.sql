--Показати мінімальну середню оцінку по всіх студентах
SELECT MIN(AVERAGE_SCORE) AS MIN_SCORE
FROM STUDENTS_SCORE

--Показати максимальну середню оцінку по всіх студентах
SELECT MAX(AVERAGE_SCORE) AS MAX_SCORE
FROM STUDENTS_SCORE

--Показати статистику міст. Має відображатися назва міста та кількість студентів з цього міста.
SELECT CITY, COUNT(*) AS STUDENTS_COUNT
FROM STUDENTS_SCORE
GROUP BY CITY; 

--Показати статистику студентів. Має відображатися назва країни та кількість студентів з цієї країни.
SELECT COUNTRY, COUNT(*) AS STUDENTS_COUNT
FROM STUDENTS_SCORE
GROUP BY COUNTRY; 


--Показати кількість студентів з мінімальною середньою оцінкою з математики.
SELECT COUNT(*) AS STUDENTS_COUNT
FROM STUDENTS_SCORE
WHERE SUBJECT_NAME_MIN_ASCORE = 'Math' AND SUBJECT_MIN_ASCORE = (
    SELECT MIN(SUBJECT_MIN_ASCORE)
    FROM STUDENTS_SCORE
    WHERE SUBJECT_NAME_MIN_ASCORE = 'Math'
);

--Показати кількість студентів з максимальною середньою оцінкою з математики
SELECT COUNT(*) AS STUDENTS_COUNT
FROM STUDENTS_SCORE
WHERE SUBJECT_NAME_MAX_ASCORE = 'Math' AND SUBJECT_MAX_ASCORE = (
    SELECT MAX (SUBJECT_MAX_ASCORE)
    FROM STUDENTS_SCORE
    WHERE SUBJECT_NAME_MAX_ASCORE = 'Math'
);

--Показати кількість студентів у кожній групі
SELECT COUNT(*) AS STUDENTS_COUNT, GROUP_NAME 
FROM STUDENTS_SCORE
GROUP BY GROUP_NAME;

--Показати середню оцінку групи
SELECT ROUND(AVG(AVERAGE_SCORE), 2) AVG_SCORE, GROUP_NAME 
FROM STUDENTS_SCORE
GROUP BY GROUP_NAME;

--вивести середню оцінку по групах, лише для груп де кількість студентів більша 3
SELECT ROUND(AVG(AVERAGE_SCORE), 2) AVG_SCORE, GROUP_NAME 
FROM STUDENTS_SCORE
GROUP BY GROUP_NAME
HAVING COUNT(*) > 3;

--вивести ті групи середня оцінка яких лежить в межах 70-80, не враховувати студентів  яким менше 25 років
SELECT ROUND(AVG(AVERAGE_SCORE), 2) AS AVG_SCORE, GROUP_NAME 
FROM STUDENTS_SCORE
WHERE EXTRACT(YEAR FROM AGE(BIRTHDAY)) > 22
GROUP BY GROUP_NAME
HAVING ROUND(AVG(AVERAGE_SCORE), 2) BETWEEN 80 AND 82;
