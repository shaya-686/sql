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
	IS_ASSISTANT BIT(1) NOT NULL DEFAULT B'0',
	IS_PROFESSOR BIT(1) NOT NULL DEFAULT B'0',
	NAME VARCHAR NOT NULL,
	POSITION VARCHAR NOT NULL,
	PREMIUM MONEY NOT NULL CHECK (PREMIUM >= 0::MONEY) DEFAULT 0.00,
	SALARY MONEY NOT NULL CHECK (SALARY > 0::MONEY),
	SURNAME VARCHAR NOT NULL
);

INSERT INTO TEACHERS (EMPLOYMENT_DATE, IS_ASSISTANT, IS_PROFESSOR, NAME, POSITION, PREMIUM, SALARY, SURNAME)
VALUES
('2005-01-01', B'0', B'1', 'John', 'Professor', 1500.00, 6000.00, 'Doe'),
('2010-03-15', B'1', B'0', 'Alice', 'Assistant Professor', 1000.00, 4500.00, 'Smith'),
('2008-07-20', B'0', B'0', 'Emma', 'Lecturer', 800.00, 4000.00, 'Johnson'),
('2012-11-10', B'1', B'1', 'Michael', 'Associate Professor', 1200.00, 5500.00, 'Williams'),
('2007-05-05', B'1', B'0', 'Sophia', 'Teaching Assistant', 600.00, 3500.00, 'Brown'),
('2004-09-30', B'0', B'0', 'Matthew', 'Lecturer', 850.00, 4200.00, 'Jones'),
('2015-02-18', B'1', B'1', 'Olivia', 'Full Professor', 2000.00, 7000.00, 'Davis'),
('2018-06-22', B'0', B'1', 'Daniel', 'Professor', 1800.00, 6500.00, 'Miller'),
('2006-12-03', B'1', B'0', 'Isabella', 'Assistant Professor', 1100.00, 4800.00, 'Wilson'),
('2009-08-14', B'0', B'0', 'William', 'Lecturer', 750.00, 3900.00, 'Martinez'),
('2013-04-27', B'1', B'1', 'Oliver', 'Associate Professor', 1300.00, 5700.00, 'Taylor'),
('2016-10-09', B'0', B'0', 'Sophie', 'Lecturer', 900.00, 4300.00, 'Anderson'),
('2003-11-21', B'1', B'0', 'Amelia', 'Teaching Assistant', 700.00, 3700.00, 'Thomas'),
('2017-08-05', B'1', B'1', 'Benjamin', 'Full Professor', 2200.00, 7500.00, 'White'),
('2002-07-15', B'0', B'1', 'Charlotte', 'Professor', 1600.00, 6200.00, 'Garcia'),
('2019-01-25', B'1', B'0', 'Ethan', 'Assistant Professor', 1300.00, 5200.00, 'Lee'),
('2001-05-12', B'0', B'0', 'Ava', 'Lecturer', 800.00, 4000.00, 'Hernandez'),
('2014-09-08', B'1', B'1', 'Mia', 'Full Professor', 1900.00, 6800.00, 'Clark'),
('2008-03-01', B'0', B'1', 'James', 'Professor', 1700.00, 6300.00, 'Lewis'),
('2005-11-14', B'1', B'0', 'Harper', 'Assistant Professor', 1200.00, 4900.00, 'Young');