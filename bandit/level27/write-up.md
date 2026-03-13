# Category

linux

# Overview

ssh://bandit27-git@bandit.labs.overthewire.org/home/bandit27-git/repo에 포트 2220을 통해 접근 가능한 git 저장소가 있습니다. 사용자 bandit27-git의 비밀번호는 사용자 bandit27과 동일합니다.

# Analysis

문제에 제시된 git repo를 확인해보니 README 파일 발견.

# Exploitation

```bash
ssh://bandit27-git@bandit.labs.overthewire.org:2220/home/bandit27-git/repo
```

# Flag

`Yz...cN`
