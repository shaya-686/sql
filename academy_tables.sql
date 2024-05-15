CREATE TABLE DEPARTMENTS (
	ID SERIAL PRIMARY KEY,
	FINANCING MONEY NOT NULL CHECK (FINANCING >= 0::MONEY) DEFAULT 0.00,
	NAME VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO DEPARTMENTS (FINANCING, NAME) VALUES
(50000.00, 'Computer Science'),
(55000.00, 'Physics'),
(60000.00, 'Chemistry'),
(45000.00, 'Biology'),
(48000.00, 'Mathematics'),
(52000.00, 'Engineering'),
(53000.00, 'Literature'),
(58000.00, 'History'),
(56000.00, 'Psychology'),
(51000.00, 'Economics'),
(54000.00, 'Sociology'),
(57000.00, 'Political Science'),
(59000.00, 'Philosophy'),
(62000.00, 'Fine Arts'),
(63000.00, 'Music'),
(61000.00, 'Languages'),
(64000.00, 'Education'),
(57000.00, 'Business Administration'),
(60000.00, 'Health Sciences'),
(55000.00, 'Law');

CREATE TABLE FACULTIES (
	ID SERIAL PRIMARY KEY,
	DEAN VARCHAR(255) NOT NULL,
	NAME VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO FACULTIES (DEAN, NAME) VALUES
('John Doe', 'Faculty of Engineering'),
('Jane Smith', 'Faculty of Medicine'),
('Michael Johnson', 'Faculty of Business Administration'),
('Emily Brown', 'Faculty of Arts'),
('David Wilson', 'Faculty of Law'),
('Sarah Thompson', 'Faculty of Science'),
('Robert Davis', 'Faculty of Education'),
('Laura Martinez', 'Faculty of Social Sciences'),
('Daniel Taylor', 'Faculty of Information Technology'),
('Rachel Lee', 'Faculty of Fine Arts'),
('Christopher Clark', 'Faculty of Psychology'),
('Jennifer White', 'Faculty of Nursing'),
('Matthew Harris', 'Faculty of Economics'),
('Jessica Carter', 'Faculty of Communication'),
('Andrew Anderson', 'Faculty of Mathematics'),
('Olivia Garcia', 'Faculty of Languages'),
('William Thomas', 'Faculty of Agriculture'),
('Stephanie Moore', 'Faculty of Environmental Studies'),
('Kevin Evans', 'Faculty of Architecture'),
('Amanda Rodriguez', 'Faculty of Pharmacy');

CREATE TABLE GROUPS (
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR(10) NOT NULL UNIQUE,
	RATING INT NOT NULL CHECK (RATING >= 0 AND RATING <= 5),
	YEAR INT NOT NULL CHECK (YEAR >= 1 AND YEAR <= 5)
);

INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
('Group 1', 4, 3),
('Group 2', 3, 2),
('Group 3', 5, 4),
('Group 4', 2, 1),
('Group 5', 4, 3),
('Group 6', 1, 1),
('Group 7', 5, 5),
('Group 8', 3, 2),
('Group 9', 4, 4),
('Group 10', 2, 1),
('Group 11', 3, 3),
('Group 12', 4, 2),
('Group 13', 5, 5),
('Group 14', 2, 1),
('Group 15', 4, 4),
('Group 16', 3, 3),
('Group 17', 1, 1),
('Group 18', 5, 5),
('Group 19', 3, 2),
('Group 20', 4, 4);

CREATE TABLE TEACHERS (
	ID SERIAL PRIMARY KEY,
	EMPLOYMENT_DATE DATE NOT NULL CHECK (EMPLOYMENT_DATE >= '1990-01-01'),
	IS_ASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
	IS_PROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
	NAME VARCHAR NOT NULL,
	POSITION VARCHAR NOT NULL,
	PREMIUM MONEY NOT NULL CHECK (PREMIUM >= 0::MONEY) DEFAULT 0.00,
	SALARY MONEY NOT NULL CHECK (SALARY > 0::MONEY),
	SURNAME VARCHAR NOT NULL
);

INSERT INTO TEACHERS (EMPLOYMENT_DATE, IS_ASSISTANT, IS_PROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME) VALUES
('1995-03-15', TRUE, FALSE, 'John', 'Lecturer', 500.00, 3000.00, 'Doe'),
('2000-07-20', FALSE, TRUE, 'Alice', 'Professor', 1000.00, 5000.00, 'Smith'),
('1998-11-10', TRUE, FALSE, 'Michael', 'Assistant Professor', 700.00, 3500.00, 'Johnson'),
('2005-02-28', TRUE, FALSE, 'Emily', 'Lecturer', 600.00, 3200.00, 'Brown'),
('2002-09-03', TRUE, FALSE, 'David', 'Lecturer', 550.00, 3100.00, 'Wilson'),
('1997-06-12', FALSE, TRUE, 'Sarah', 'Professor', 1200.00, 6000.00, 'Thompson'),
('2008-04-17', TRUE, FALSE, 'Robert', 'Assistant Professor', 800.00, 3700.00, 'Davis'),
('2003-10-25', FALSE, TRUE, 'Laura', 'Professor', 1100.00, 5500.00, 'Martinez'),
('1999-08-05', TRUE, FALSE, 'Daniel', 'Lecturer', 650.00, 3300.00, 'Taylor'),
('2006-12-30', TRUE, FALSE, 'Rachel', 'Lecturer', 700.00, 3400.00, 'Lee'),
('2001-05-08', FALSE, TRUE, 'Christopher', 'Professor', 1050.00, 5200.00, 'Clark'),
('2004-01-19', FALSE, TRUE, 'Jennifer', 'Professor', 1250.00, 6200.00, 'White'),
('1996-09-23', TRUE, FALSE, 'Matthew', 'Assistant Professor', 750.00, 3600.00, 'Harris'),
('2007-08-11', TRUE, FALSE, 'Jessica', 'Lecturer', 680.00, 3350.00, 'Carter'),
('2009-11-02', FALSE, TRUE, 'Andrew', 'Professor', 1150.00, 5800.00, 'Anderson'),
('2000-03-14', TRUE, FALSE, 'Olivia', 'Assistant Professor', 720.00, 3650.00, 'Garcia'),
('1998-02-09', TRUE, FALSE, 'William', 'Lecturer', 620.00, 3150.00, 'Thomas'),
('2005-07-21', FALSE, TRUE, 'Stephanie', 'Professor', 1300.00, 6500.00, 'Moore'),
('2002-04-05', TRUE, FALSE, 'Kevin', 'Lecturer', 670.00, 3250.00, 'Evans'),
('2003-12-18', FALSE, TRUE, 'Amanda', 'Professor', 1350.00, 6700.00, 'Rodriguez');
