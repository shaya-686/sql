-- Відображення усіх овочів з калорійністю, менше вказаної.
SELECT * 
FROM FRUITS_AND_VEGETABLES 
WHERE PRODUCT_TYPE = 'vegetable' AND CALORIC_CONTENT < 50;

-- Відображення усіх фруктів з калорійністю у вказаному діапазоні.
SELECT * 
FROM FRUITS_AND_VEGETABLES 
WHERE PRODUCT_TYPE = 'fruit' AND CALORIC_CONTENT BETWEEN 40 AND 60;

--Відображення усіх овочів, у назві яких є вказане слово. Наприклад, слово: капуста
SELECT * 
FROM FRUITS_AND_VEGETABLES 
WHERE PRODUCT_TYPE = 'vegetable' AND LOWER(PRODUCT_NAME) LIKE '%carrot%';

-- Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово. Наприклад, слово: гемоглобін
SELECT * 
FROM FRUITS_AND_VEGETABLES 
WHERE LOWER(DESCRIPTION) LIKE '%crunchy%';

-- Показати усі овочі та фрукти жовтого або червоного кольору
SELECT * 
FROM FRUITS_AND_VEGETABLES 
WHERE LOWER(COLOR) IN ('red', 'yellow');