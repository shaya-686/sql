--Виведіть усі можливі пари рядків викладачів і груп
SELECT LECTURES.ID, LECTURES.LECTURE_ROOM, SUBJECTS.NAME, TEACHERS.SURNAME, TEACHERS.NAME, GROUPS.NAME
FROM GROUPS_LECTURES
	JOIN GROUPS ON GROUPS.ID = GROUPS_LECTURES.GROUP_ID
	JOIN LECTURES ON LECTURES.ID = GROUPS_LECTURES.LECTURE_ID
	JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHER_ID
	JOIN SUBJECTS ON LECTURES.SUBJECT_ID = SUBJECTS.ID;
	
--. Виведіть назви факультетів, фонд фінансування кафедр
--яких перевищує фонд фінансування факультету

SELECT FACULTIES.NAME
FROM FACULTIES
WHERE FACULTIES.FINANCING < (SELECT SUM(FINANCING)
	FROM DEPARTMENTS
	WHERE DEPARTMENTS.FACULTY_ID = FACULTIES.ID
	GROUP BY FACULTY_ID);
	
--Виведіть прізвища кураторів груп і назви груп, які вони курирують.
SELECT CURATORS.SURNAME, GROUPS.NAME
FROM GROUPS_CURATORS
	JOIN GROUPS ON GROUPS.ID = GROUPS_CURATORS.GROUP_ID
	JOIN CURATORS ON CURATORS.ID = GROUPS_CURATORS.CURATOR_ID;
	
--Виведіть імена та прізвища викладачів, які читають лекції у групі «P107» (-> "Group 5")
SELECT DISTINCT TEACHERS.SURNAME, TEACHERS.NAME
FROM GROUPS_LECTURES
	JOIN GROUPS ON GROUPS.ID = GROUPS_LECTURES.GROUP_ID
	JOIN LECTURES ON LECTURES.ID = GROUPS_LECTURES.LECTURE_ID
	JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHER_ID
WHERE GROUPS.NAME = 'Group 5';

--Виведіть прізвища викладачів і назви факультетів, на яких вони читають лекції.
SELECT DISTINCT TEACHERS.SURNAME, FACULTIES.NAME
FROM GROUPS_LECTURES
	JOIN GROUPS ON GROUPS.ID = GROUPS_LECTURES.GROUP_ID
	JOIN LECTURES ON LECTURES.ID = GROUPS_LECTURES.LECTURE_ID
	JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHER_ID
	JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENT_ID
	JOIN FACULTIES ON FACULTIES.ID = DEPARTMENTS.FACULTY_ID;

--Виведіть назви кафедр і назви груп, які до них належать.
SELECT DEPARTMENTS.NAME, GROUPS.NAME
FROM GROUPS
	JOIN DEPARTMENTS ON GROUPS.DEPARTMENT_ID = DEPARTMENTS.ID; 
	
--Виведіть назви предметів, які викладає викладач «Samantha Adams» (->Thomas Amelia)
SELECT DISTINCT SUBJECTS.NAME
FROM LECTURES
	JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHER_ID
	JOIN SUBJECTS ON LECTURES.SUBJECT_ID = SUBJECTS.ID
WHERE TEACHERS.SURNAME = 'Thomas' AND TEACHERS.NAME = 'Amelia';

--Виведіть назви кафедр, на яких викладається дисципліна «Database Theory».(->Mathematics)
SELECT DISTINCT DEPARTMENTS.NAME
FROM GROUPS_LECTURES
	JOIN GROUPS ON GROUPS.ID = GROUPS_LECTURES.GROUP_ID
	JOIN LECTURES ON LECTURES.ID = GROUPS_LECTURES.LECTURE_ID
	JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENT_ID
	JOIN SUBJECTS ON LECTURES.SUBJECT_ID = SUBJECTS.ID
WHERE SUBJECTS.NAME = 'Mathematics';

--Виведіть назви груп, що належать до факультету «Computer Science».
SELECT GROUPS.NAME
FROM GROUPS
	JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENT_ID
	JOIN FACULTIES ON FACULTIES.ID = DEPARTMENTS.FACULTY_ID
WHERE FACULTIES.NAME = 'Faculty of Fine Arts';

--Виведіть назви груп 5-го курсу, а також назви факультетів, до яких вони належать.
SELECT GROUPS.NAME, FACULTIES.NAME
FROM GROUPS
	JOIN DEPARTMENTS ON DEPARTMENTS.ID = GROUPS.DEPARTMENT_ID
	JOIN FACULTIES ON FACULTIES.ID = DEPARTMENTS.FACULTY_ID
WHERE GROUPS.YEAR = 5;

--Виведіть повні імена викладачів і лекції, які вони читають
--(назви предметів та груп). Зробіть відбір по тим лекціям,
--які проходять в аудиторії «B103».
SELECT TEACHERS.SURNAME, TEACHERS.NAME, SUBJECTS.NAME, GROUPS.NAME
FROM GROUPS_LECTURES
	JOIN GROUPS ON GROUPS.ID = GROUPS_LECTURES.GROUP_ID
	JOIN LECTURES ON LECTURES.ID = GROUPS_LECTURES.LECTURE_ID
	JOIN TEACHERS ON TEACHERS.ID = LECTURES.TEACHER_ID
	JOIN SUBJECTS ON LECTURES.SUBJECT_ID = SUBJECTS.ID
WHERE LECTURES.LECTURE_ROOM = 'Room 120'

