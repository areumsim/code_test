# TESTDOME  문제
https://www.testdome.com/library?page=1&skillArea=36&questionSets=public

- Social Network  품
- Session 품
- Students 품
- Regional Sales Comparison  - 못 품! *** 
- Enrollment - 틀림 (update 사용)
- Users And Roles - (create)- 못 품! *** 
- Pets - 품
- Workers - 품
- Web Shop - 품
---

**Enrollment**

*update*

```sql
UPDATE enrollments SET year = 2015 WHERE ID BETWEEN 20 AND 100
```

*** 동일한 결과여도, update 아니면 틀림

```sql
SELECT id, 
  CASE
  WHEN id >= 20 and id <= 100 then 2015
  ELSE year
  END as year, studentID
FROM enrollments
```

---

**Users And Roles**

```sql
CREATE TABLE TestTable AS
SELECT customername, contactname
	FROM customers;
```

https://moonlight-spot.tistory.com/entry/SQL-TestDome-Solution-Users-And-Roles

ref. https://growthhacker-hyounsub.tistory.com/17

```sql
create table usersRoles (
  userId integer NOT NULL,
  roleId integer NOT NULL,
  FOREIGN KEY (userId) REFERENCES users (id),
  FOREIGN KEY (roleId) REFERENCES roles (id),
  UNIQUE(userId,roleId)
  );
```

```txt
내가 만들 테이블은 usersRoles 테이블이야
       거기에 userid 와 roleid 칼럼을 만들거야
       그 userid 칼럼은 지명당할 건데, 그 시작 테이블은 users이고, 그 시작 칼럼은 id 야
       그 roleid 칼럼은 지명당할 건데, 그 시작 테이블은 roles이고, 그 시작 칼럼은 id 야
       두 개 모두 unique한 값만 지정할거야
```
---

### Pets

*Union*

```sql
SELECT name
FROM dogs

UNION

SELECT name
FROM cats
```

---

### Workers

```sql
SELECT e.name
FROM employees e
where e.name not in (
  SELECT e.name
  FROM employees e
  join employees m on e.id = m.managerId
)
```
