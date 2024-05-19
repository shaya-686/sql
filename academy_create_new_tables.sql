CREATE TABLE CURATORS (
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR NOT NULL, 
	SURNAME VARCHAR NOT NULL
);

INSERT INTO CURATORS (NAME, SURNAME) VALUES
    ('John', 'Doe'),
    ('Alice', 'Smith'),
    ('Michael', 'Johnson'),
    ('Emily', 'Brown'),
    ('David', 'Wilson'),
    ('Sarah', 'Taylor'),
    ('James', 'Anderson'),
    ('Emma', 'Martinez'),
    ('Daniel', 'Miller'),
    ('Olivia', 'Davis');
	
ALTER TABLE DEPARTMENTS
ADD COLUMN FACULTY_ID INT REFERENCES FACULTIES(ID) DEFAULT FLOOR(RANDOM() * 20) + 1;

ALTER TABLE GROUPS
ADD COLUMN DEPARTMENT_ID INT REFERENCES DEPARTMENTS(ID) DEFAULT FLOOR(RANDOM() * 20) + 1;


CREATE TABLE SUBJECTS (
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO SUBJECTS (NAME) VALUES
    ('Mathematics'),
    ('Physics'),
    ('Chemistry'),
    ('Biology'),
    ('English'),
    ('History'),
    ('Computer Science'),
    ('Geography'),
    ('Literature'),
    ('Art'),
    ('Music'),
    ('Economics'),
    ('Psychology'),
    ('Sociology'),
    ('Philosophy'),
    ('Physical Education'),
    ('Foreign Language'),
    ('Statistics'),
    ('Engineering'),
    ('Environmental Science');
	
CREATE TABLE LECTURES (
	ID SERIAL PRIMARY KEY,
	LECTURE_ROOM VARCHAR NOT NULL,
	SUBJECT_ID INT REFERENCES SUBJECTS(ID),
	TEACHER_ID INT REFERENCES TEACHERS(ID)
	);

INSERT INTO LECTURES (LECTURE_ROOM, SUBJECT_ID, TEACHER_ID) VALUES
    ('Room 101', 1, 1),
    ('Room 102', 2, 2),
    ('Room 103', 3, 3),
    ('Room 104', 4, 4),
    ('Room 105', 1, 13),
    ('Room 106', 6, 6),
    ('Room 107', 7, 7),
    ('Room 108', 7, 19),
    ('Room 109', 9, 9),
    ('Room 110', 10, 10),
    ('Room 111', 11, 11),
    ('Room 112', 12, 12),
    ('Room 113', 13, 13),
    ('Room 114', 14, 14),
    ('Room 115', 15, 15),
    ('Room 116', 16, 16),
    ('Room 117', 17, 17),
    ('Room 118', 18, 18),
    ('Room 119', 19, 19),
    ('Room 120', 20, 20);

CREATE TABLE GROUPS_LECTURES (
	ID SERIAL PRIMARY KEY,
	GROUP_ID INT REFERENCES GROUPS(ID),
	LECTURE_ID INT REFERENCES LECTURES(ID)
);

INSERT INTO GROUPS_LECTURES (GROUP_ID, LECTURE_ID)
VALUES (1, 2),
	   (5, 1),
	   (7, 3),
	   (8, 4),
	   (9, 5),
	   (3, 6),
	   (12, 7),
	   (10, 8),
	   (5, 9),
	   (14, 12),
	   (15, 10), 
	   (16, 20),
	   (18, 13);
		

CREATE TABLE GROUPS_CURATORS (
	ID SERIAL PRIMARY KEY,
	GROUP_ID INT REFERENCES GROUPS(ID),
	CURATOR_ID INT REFERENCES CURATORS(ID)
);

INSERT INTO GROUPS_CURATORS (GROUP_ID, CURATOR_ID)
VALUES (1, 2),
	   (5, 1),
	   (7, 3),
	   (8, 4),
	   (9, 5),
	   (3, 6),
	   (12, 7),
	   (10, 8),
	   (5, 9),
	   (14, 7),
	   (15, 10), 
	   (16, 8),
	   (18, 6);

ALTER TABLE FACULTIES
ADD COLUMN FINANCING MONEY NOT NULL DEFAULT 30000::MONEY;
