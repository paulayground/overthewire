# 배운 점

mysql에서 like는 대소문자를 구별하지 않아 `BINARY()`로 바꿔서 검사하면 된다

# 풀이 과정 기록

유저가 존재하는지 확인하는 서비스로 소스코드 보니 유저 테이블 정보 `username`, `password`가 있고 유저 가져오는 쿼리문을 보고 sql 인젝션 문제이라고 생각했다.

처음에는 반환값을 안보고 무작정 어떻게 공격할 지 생각했고 `" OR 1=1 #` 만들어서 공격하면 되겠다고 생각했다.

```sql
SELECT *
from users
where username=" $_REQUEST["username"] ";
```

다시 코드를 보고 유저 존재여부만 알려준다는 것을 확인하고 `users` 테이블의 `username`과 `password`가 어떤 것일지 유추가 됐다.
그리고 반환값을 이용한 blind sql injection 공격을 하기로 생각했다.

```sql
SELECT *
from users
where username="" OR 1=1 AND password like "[a-z0-9]%";
```

처음에는 `username`이 1개일 거라는 생각에 비워두고 공격을 했지만 이상한 패스워드가 나오는 것을 보고 다른 유저의 가능성을 깨달아 natas16으로 타겟을 지정한 쿼리문으로 고쳤다.

```sql
SELECT *
from users
where username="natas16" AND password like "[a-z0-9]%";
```

소문자로 이루어진 `hp...go` 비밀번호을 얻게 되었는데, 일치하지 않았고 찾아보다가 MySQL에서는 `LIKE`로 검사시 대소문자 구분을 하지 않는다는 사실을 알았다.

소문자로 받아온 비밀번호에 `BINARY()`를 적용하는 방식으로 다시 시도하여 다음 비밀번호를 획득했다.

```sql
SELECT *
from users
where username="<natas16" AND BINARY(password) like "[a-z0-9]%>";
```

# 익스플로잇 코드 정리

solve.py 참고

# 심화 학습 (Deep Dive)

# 참고
