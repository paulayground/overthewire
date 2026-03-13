# Problem Overview

홈디렉토리의 `setuid`를 이용한 후, 패스워드는 `/etc/bandit_pass`에서 찾을 수 있음

# Analysis

홈디렉토리에 `setuid`가 설정된 `bandit20-do`파일을 확인함.
실행 결과 다른 유저로써 명령어를 실행하라는 힌트와 사용 예시를 확인함.
해당 파일을 실행하며 파라미터로 명령어를 전달 시 `setuid` 설정된 유저의 권한으로 명령어를 실행하는 것으로 확인함.

> `setuid` 실행파일에 대한 취약성을 확인하고 이를 통해 다음 패스워드를 확인하라는 문제

# Exploitation Strategy

`setuid`가 실행되는 `bandit20-do` 파일을 통해 다음 패스워드가 입력되어있는 경로인 `/etc/bandit_pass`를 읽어 해결할 수 있을 것으로 판단.

# Execution

```
./bandit20-do cat /etc/bandit_pass/bandit20
```

# Flag

`0qX...`
