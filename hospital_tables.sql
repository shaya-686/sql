CREATE TABLE DEPARTMENTS (
	ID SERIAL PRIMARY KEY,
	BUILDING INT NOT NULL CHECK (BUILDING >= 1 AND BUILDING <= 5),
	FINANCING MONEY NOT NULL CHECK (FINANCING >= 0::money) DEFAULT 0.00,
	NAME VARCHAR(100) NOT NULL UNIQUE
)

INSERT INTO DEPARTMENTS (BUILDING, FINANCING, NAME) VALUES
    (1, 1000.00, 'Emergency Department'),
    (2, 1500.00, 'Surgical Department'),
    (3, 2000.00, 'Cardiology Department'),
    (4, 1200.00, 'Pediatric Department'),
    (5, 1800.00, 'Radiology Department'),
    (1, 900.00, 'Intensive Care Unit'),
    (2, 1600.00, 'Orthopedic Department'),
    (3, 2200.00, 'Neurology Department'),
    (4, 1300.00, 'Oncology Department'),
    (5, 1900.00, 'Gynecology Department'),
    (1, 1100.00, 'ENT Department'),
    (2, 1400.00, 'Urology Department'),
    (3, 2300.00, 'Endocrinology Department'),
    (4, 1000.00, 'Dermatology Department'),
    (5, 1700.00, 'Hematology Department'),
    (1, 1200.00, 'Psychiatry Department'),
    (2, 1800.00, 'Ophthalmology Department'),
    (3, 2400.00, 'Pulmonology Department'),
    (4, 1100.00, 'Allergy Department'),
    (5, 2000.00, 'Nephrology Department');
	
CREATE TABLE DESEASES (
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR(100) NOT NULL UNIQUE,
	SEVERITY INT NOT NULL CHECK (SEVERITY >= 1) DEFAULT 1
);

INSERT INTO DISEASES (NAME, SEVERITY) VALUES
    ('Influenza', 3),
    ('Pneumonia', 5),
    ('COVID-19', 7),
    ('Diabetes', 6),
    ('Hypertension', 4),
    ('Asthma', 4),
    ('Bronchitis', 3),
    ('Cancer', 8),
    ('Heart Disease', 7),
    ('Stroke', 9),
    ('Arthritis', 5),
    ('Migraine', 3),
    ('Alzheimer''s Disease', 8),
    ('Parkinson''s Disease', 7),
    ('Epilepsy', 6),
    ('Chronic Kidney Disease', 6),
    ('Liver Cirrhosis', 6),
    ('Obesity', 5),
    ('Anemia', 4),
    ('Rheumatoid Arthritis', 5);

CREATE TABLE DOCTORS (
	ID SERIAL PRIMARY KEY,
	NAME VARCHAR(255) NOT NULL,
	SURNAME VARCHAR(255) NOT NULL,
	PHONE CHAR(10),
	SALARY MONEY NOT NULL CHECK (SALARY > 0::money)
);

INSERT INTO DOCTORS (NAME, SURNAME, PHONE, SALARY) VALUES
    ('John', 'Smith', '1234567890', 80000.00),
    ('Emily', 'Johnson', '2345678901', 85000.00),
    ('Michael', 'Williams', '3456789012', 90000.00),
    ('Emma', 'Brown', '4567890123', 95000.00),
    ('Daniel', 'Jones', '5678901234', 100000.00),
    ('Olivia', 'Miller', '6789012345', 105000.00),
    ('William', 'Davis', '7890123456', 110000.00),
    ('Sophia', 'Garcia', '8901234567', 115000.00),
    ('James', 'Rodriguez', '9012345678', 120000.00),
    ('Charlotte', 'Martinez', '0123456789', 125000.00),
    ('Benjamin', 'Hernandez', '1234567890', 130000.00),
    ('Amelia', 'Lopez', '2345678901', 135000.00),
    ('Alexander', 'Gonzalez', '3456789012', 140000.00),
    ('Mia', 'Wilson', '4567890123', 145000.00),
    ('Ethan', 'Anderson', '5678901234', 150000.00),
    ('Isabella', 'Taylor', '6789012345', 155000.00),
    ('Jacob', 'Thomas', '7890123456', 160000.00),
    ('Ava', 'Moore', '8901234567', 165000.00),
    ('Noah', 'Jackson', '9012345678', 170000.00),
    ('Sophia', 'White', '0123456789', 175000.00);

CREATE TABLE EXAMINATIONS (
	ID SERIAL PRIMARY KEY,
	DAY_OF_WEEK INT NOT NULL CHECK (DAY_OF_WEEK >= 1 AND DAY_OF_WEEK <= 7),
	START_TIME TIME NOT NULL CHECK (START_TIME >= '08:00' AND START_TIME <= '18:00'),
	END_TIME TIME NOT NULL CHECK (END_TIME > START_TIME),
	NAME VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO EXAMINATIONS (DAY_OF_WEEK, START_TIME, END_TIME, NAME) VALUES
    (1, '09:00', '11:00', 'Blood Test'),
    (2, '10:30', '12:30', 'X-Ray'),
    (3, '13:00', '15:00', 'Ultrasound'),
    (4, '14:30', '16:30', 'MRI Scan'),
    (5, '09:30', '11:30', 'EKG'),
    (6, '11:00', '13:00', 'Endoscopy'),
    (7, '12:30', '14:30', 'Colonoscopy'),
    (1, '15:00', '17:00', 'CT Scan'),
    (2, '16:30', '18:30', 'Physical Examination'),
    (3, '09:00', '11:00', 'Dermatology Consultation'),
    (4, '10:30', '12:30', 'Ophthalmology Checkup'),
    (5, '13:00', '15:00', 'Neurology Assessment'),
    (6, '14:30', '16:30', 'Orthopedic Consultation'),
    (7, '09:30', '11:30', 'Psychiatry Evaluation'),
    (1, '11:00', '13:00', 'Cardiology Consultation'),
    (2, '12:30', '14:30', 'Pulmonology Appointment'),
    (3, '15:00', '17:00', 'Gastroenterology Consultation'),
    (4, '16:30', '18:30', 'Urology Appointment'),
    (5, '09:00', '11:00', 'Obstetrics Checkup'),
    (6, '10:30', '12:30', 'Pediatrics Consultation');

CREATE TABLE WARDS (
	ID SERIAL PRIMARY KEY,
	BUILDING INT NOT NULL CHECK (BUILDING >= 1 AND BUILDING <= 5),
	FLOOR INT NOT NULL CHECK (FLOOR >= 1),
	NAME VARCHAR(20) NOT NULL UNIQUE
);

INSERT INTO WARDS (BUILDING, FLOOR, NAME) VALUES
    (1, 1, 'ICU'),
    (1, 2, 'Pediatrics'),
    (1, 3, 'Neurology'),
    (2, 1, 'Oncology'),
    (2, 2, 'Orthopedics'),
    (2, 3, 'Cardiology'),
    (3, 1, 'Maternity'),
    (3, 2, 'Surgery'),
    (3, 3, 'Gynecology'),
    (4, 1, 'Psychiatry'),
    (4, 2, 'Dermatology'),
    (4, 3, 'ENT'),
    (5, 1, 'Emergency'),
    (5, 2, 'Radiology'),
    (5, 3, 'Urology'),
    (1, 4, 'Nephrology'),
    (2, 4, 'Endocrinology'),
    (3, 4, 'Pulmonology'),
    (4, 4, 'Gastroenterology'),
    (5, 4, 'Ophthalmology');
