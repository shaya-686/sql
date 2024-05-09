CREATE TABLE FRUITS_AND_VEGETABLES (
	ID SERIAL PRIMARY KEY,
	PRODUCT_NAME VARCHAR(30) NOT NULL UNIQUE,
	PRODUCT_TYPE INT CHECK (PRODUCT_TYPE IN (1, 2)), --1 - FRUITS, 2 - VEGETABLES
	COLOR VARCHAR(30),
	CALORIC_CONTENT INT CHECK (CALORIC_CONTENT > 0),
	DESCRIPTION VARCHAR(200)
)