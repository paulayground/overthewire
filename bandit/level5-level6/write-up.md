# Category

linux

# Overview

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:

human-readable
1033 bytes in size
not executable

# Analysis

```bash
ssh bandit5@bandit.labs.overthewire.org -p 2220
```

서버에 접속 후 홈디렉토리 `inhere` 하위에 `maybehere00...` 등 많은 디렉토리파일로 구성되어 있음.
문제에 제시된 `human-readable`, `not executable`, 사이즈가 `1033바이트`인 파일을 찾기 위해 `find` 사용.

# Exploitation

문제에 제시된 요건에 맞춰 파일을 검색하면 파일이 검색되며, 해당 파일을 읽으면 다음 패스워드를 알 수 있다.

```bash
find inhere/ ! -executable -size 1033c -exec file {} \+ | grep ASCII
inhere/maybehere07/.file2: ASCII text, with very long lines (1000)

cat inhere/maybehere07/.file2
```

# Flag

`HW...EG`
