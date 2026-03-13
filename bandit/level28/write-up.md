# Category

linux

# Overview

ssh://bandit28-git@bandit.labs.overthewire.org/home/bandit28-git/repo에 포트 2220을 통해 접근 가능한 git 저장소가 있습니다. 사용자 bandit28-git의 비밀번호는 사용자 bandit28과 동일합니다.

# Analysis

클론을 받아 파일을 확인해보니 아래와 같이 bandit29 유저정보가 적인 md파일을 발견했으며 .git파일이 있어 이전 수정 기록이 있는지 확인할 수 있다.

```md
# Bandit Notes

Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
```

# Exploitation

git 변경기록을 보면 이전 수정사항을 확인해 다음 비밀번호를 알 수 있다.

```bash
git log -p

commit b5ed4b5a3499533c2611217c8780e8ead48609f6 (HEAD -> master, origin/master, origin/HEAD)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 14 09:26:24 2025 +0000

    fix info leak

diff --git a/README.md b/README.md
index d4e3b74..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: 4p...J7
+- password: xxxxxxxxxx
```

# Flag

`4p...J7`
