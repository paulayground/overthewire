# Category

linux

# Overview

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

# Analysis

```bash
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

서버에 접속 후 문제에 제시된 `user`가 `bandit7`이고 `group`이 `bandit6`이며 사이즈가 `33바이트`인 파일을 찾기 위해 `find` 사용.

# Exploitation

`/` 경로 하위 검색이기 때문에 권한이 없어 발생하는 `Permission denied`를 보지 않기 위하여 발생하는 에러들을 처리함.
검색된 파일을 확인하면 다음 비밀번호를 확인할 수 있다.

```bash
find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
/var/lib/dpkg/info/bandit7.password

cat /var/lib/dpkg/info/bandit7.password
```

# Flag

`mo...aj`
