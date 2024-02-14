# sql

### 포함

```sql
WHERE CITY LIKE “%서울%” OR CITY LIKE “%수원%”

WHERE LEFT(CITY, 1) IN ('A', 'C', 'I')
AND RIGHT(CITY, 1) IN ('A', 'C', 'I')

## 글자수 지정
WHERE CITY LIKE “__시” OR CITY LIKE “__광역_” OR CITY LIKE “_____시”
```

### DATA FORMAT

`DATE_FORMAT(REPLY.CREATED_DATE, '%Y-%m-%d')`

`**MONTH(DATE_OF_BIRTH) = 3**`

**`START_DATE >= '2022-08-01' AND START_DATE <= '2022-10-31’`**

### ROUND

`ROUND(AVG(RR.REVIEW_SCORE),2) AS SCORE`

### TRUNCATE

`**TRUNCATE(3456.1234567 ,2)**` 

// 3456.12

`**TRUNCATE(3456.1234567 ,-2)**` 

// 3400

### IS NULL  = NVL / IS NOT NULL

`ISNULL(표현식1, 표현식2)`  `NVL(표현식1, 표현식2)` 

`IFNULL(FREEZER_YN, 'N')`

### UNION DISTINCT / UNION ALL

```sql
SELECT  ...
FROM ..

UNION

SELECT  ...
FROM ..

ORDER BY SALES_DATE, PRODUCT_ID , USER_ID
```

### 빈 열 추가

```sql
SELECT PRODUCT_ID, **NULL USER_ID,** SALES_AMOUNT
FROM OFFLINE_SALE
```

### 조건으로 열 추가

```sql
SELECT hook_type,
   CASE hook_type
      WHEN 0 THEN 'OFFER'
      WHEN 1 THEN 'ACCEPT'
      WHEN 2 THEN 'EXPIRED'
   END AS hook_name,
   COUNT(*) AS number_of_exchange_activities
FROM `exchange`
GROUP BY hook_type

SELECT *,
    CASE
        WHEN START_DATE <= "2022-10-16%" AND END_DATE >= "2022-10-16%" THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY        
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
```

### 중복

**`HAVING COUNT(colname) > 1`** 

```sql
SELECT  COLUMN_NAME ,  -- 중복되는 데이터
         COUNT(COLUMN_NAME) -- 중복 갯수
FROM TABLE_NAME              -- 중복조사를 할 테이블 이름
GROUP BY COLUMN_NAME      -- 중복되는 항목 조사를 할 컬럼
**HAVING COUNT(COLUMN_NAME) > 1 ;  -- 1개 이상 (갯수)**
```

### 항목 당 최대 값만 출력

```sql
**WHERE (FOOD_TYPE, FAVORITES) IN ( 
    SELECT FOOD_TYPE, max(FAVORITES)
    FROM REST_INFO
    GROUP BY FOOD_TYPE** )
```

개수가 최대!

```sql
**( SELECT MEMBER_ID 
	FROM REST_REVIEW
	GROUP BY MEMBER_ID
	ORDER BY COUNT(*) DESC
	LIMIT 1 )**
```

### 상위 N개 출력

```sql
...
ORDER BY ... 
**LIMIT N** 
```

### **STRING / DATE**

### DATE (DATEDIFF)

**`DATEDIFF(날짜1, 날짜2);`**

DATEDIFF(날짜1, 날짜2) + 1  : 날짜 차이 셀 

`**TIMESTAMPDIFF(단위, 날짜1, 날짜2);**`

- 단위 : SECOND : 초   /  MINUTE : 분  /  HOUR : 시  /  DAY : 일  /  WEEK : 주  /  MONTH : 월  /  QUARTER : 분기  /  YEAR : 연

### STRING ( CONCAT )

`CONCAT( , , ... )`

### **WHERE vs HAVING**

**Where**

`select * from 테이블명 where 조건절`

- 항상 from뒤에 위치
- 우선적으로 모든 필드를 조건 적

**having**

`select * from 테이블명 group by 필드명 having 조건절`

- 항상 group by뒤에 위치하고
- group by 된 이후 특정한 필드로 그룹화 되어진 새로운 테이블에 조건 적

### 사용자 정의 변수 선언

```sql
SET @start = 1, @finish = 10;
set @rownum = 0; -- set으로 rownum을 정의하고 초기값 0 할당

SELECT @start := 1, @finish := 10;

select (@rownum:= @rownum +1) as rownum, emp_no, first_name from employees e  limit 5;
--매 레코드마다 rownum +1을 해준다.
```

- `SET @변수명` 을 사용시 `=` 대입연산자를 사용한다
- `SELECT @변수명` 을 사용시 `:=` 과 같은 대입연산자를 사용한다.

### 임시/가상 테이블 (WITH)

```sql
WITH 가상테이블명 AS
(
    SELECT 쿼리
    UNION ALL -- 뭐 붙이거나 할 경우 추가
    SELECT 쿼리
)

WITH TBL AS
(
	SELECT '철수' AS NAME, 20 AS AGE
	UNION ALL
	SELECT NAME, AGE
	  FROM TB1
)

SELECT NAME, AGE FROM TBL;
```

### 서브쿼리

```sql
select avg(Population)
from (
	select Continent, Population 
	from country 
	group by Continent) as T ;

## SELECT 안 
SELECT first_name, last_name,
       (SELECT COUNT(*) FROM orders WHERE orders.customer_id = customers.customer_id)
       AS order_count
FROM customers;

## FROM 안 
SELECT emp.first_name, emp.last_name, emp.salary
FROM (SELECT * FROM employees WHERE salary > 50000) AS emp
ORDER BY emp.salary DESC;

## WHERE 안
...
WHERE department_id IN (SELECT department_id FROM departments WHERE location = 'New York');

## HAVING 안
GROUP BY department_id
HAVING COUNT(*) > (SELECT AVG(employee_count) FROM
                  (SELECT department_id, COUNT(*) AS employee_count
                   FROM employees
                   GROUP BY department_id) AS dept_counts);
```

