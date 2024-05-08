--Відображення всієї інформації з таблиці овочів та фруктів;
SELECT * FROM FRUITS_AND_VEGETABLES;

--Відображення усіх овочів;
SELECT * FROM FRUITS_AND_VEGETABLES WHERE PRODUCT_TYPE = 2;

--Відображення усіх фруктів
SELECT * FROM FRUITS_AND_VEGETABLES WHERE PRODUCT_TYPE = 1;

--Відображення усіх назв овочів та фруктів;
SELECT PRODUCT_NAME FROM FRUITS_AND_VEGETABLES;

-- Відображення усіх кольорів. Кольори мають бути унікальними;
SELECT DISTINCT COLOR FROM FRUITS_AND_VEGETABLES;

--Відображення фруктів певного кольору
SELECT * FROM FRUITS_AND_VEGETABLES WHERE PRODUCT_TYPE=1 AND COLOR = 'Red';

--Відображення овочів певного кольору
SELECT * FROM FRUITS_AND_VEGETABLES WHERE PRODUCT_TYPE=2 AND COLOR = 'Green';