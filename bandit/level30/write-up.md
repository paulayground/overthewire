# Category

linux

# Overview

`ssh://bandit30-git@bandit.labs.overthewire.org/home/bandit30-git/repo`에 포트 2220을 통해 접근할 수 있는 git 저장소가 있습니다. 사용자 bandit30-git의 비밀번호는 사용자 bandit30의 비밀번호와 동일합니다.

# Analysis

git을 받은 후 로그나 브랜치를 봐도 별다른 사항을 확인할 수 없었으며, git tag에는 `secret`이라는 태그가 있는 것을 확인 할 수 있었다.

# Exploitation

`secret` tag를 확인하면 다음 비밀번호를 얻을 수 있다.

```bash
git tag
secret

git show secret
```

# Flag

`fb...Dy`
