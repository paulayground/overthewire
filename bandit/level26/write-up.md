# Category

linux

# Overview

쉘을 얻었네! 잘했어! 이제 빨리 bandit27의 비밀번호를 가져와!

# Analysis

홈디렉토리에 소유자 bandit27의 `setuid` 설정이 되어있는 `bandit27-do`를 발견하였으며, 실행 결과 아래와 같이 출력되었다.

```bash /home/bandit26/bandit27-do
Run a command as another user.
  Example: ./bandit27-do id
```

# Exploitation

bandit27의 `setuid`가 설정되어 있고 사용법이 나와 있어 비밀번호가 있는 위치를 읽어 다음 비밀번호를 획득할 수 있다.

```bash
./bandit27-do ./bandit27-do cat /etc/bandit_pass/bandit27
```

# Flag

`up...GB`
