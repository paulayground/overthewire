# Category

linux

# Overview

`ssh://bandit31-git@bandit.labs.overthewire.org/home/bandit31-git/repo`에 포트 2220을 통해 접근할 수 있는 git 저장소가 있습니다. 사용자 bandit31-git의 비밀번호는 사용자 bandit31의 비밀번호와 동일합니다.

# Analysis

git을 받고 내용을 확인하니 원격 저장소로 `key.txt` 파일을 만들고 `master` 브랜치에 푸시하라는 내용이였다.

```md README.md
This time your task is to push a file to the remote repository.

Details:
File name: key.txt
Content: 'May I come in?'
Branch: master
```

# Exploitation

`.gitignore`에 `*.txt`가 설정되어 있어 로컬에서 `!key.txt` 와 같이 `.gitignore`의 범위에서 뺀 뒤 `key.txt`파일을 만들어 해당 변경사항만 커밋 후 푸시하게되면 다음 비밀번호를 얻을 수 있다.

# Flag

`3O...5K`
