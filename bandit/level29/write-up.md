# Category

linux

# Overview

`ssh://bandit29-git@bandit.labs.overthewire.org/home/bandit29-git/repo`에 포트 `2220`을 통해 접근 가능한 git 저장소가 있습니다. 사용자 `bandit29-git`의 비밀번호는 사용자 bandit29의 비밀번호와 동일합니다.

# Analysis

git을 받아 내용을 확인한 결과 README.md 파일은 아래와 같았으며 패스워드가 production에서는 안보이게 바꾼것으로 보여 다른 브랜치에 존재할 가능성이 있다는 것을 확인함.

```md README.md
# Bandit Notes

Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
```

# Exploitation

브랜치의 종류를 확인하여 dev, master, spoloits-dev 원격브랜치를 확인함.

```bash
git branch -r
origin/HEAD -> origin/master
origin/dev
origin/master
origin/sploits-dev
```

각각의 브랜치에 들어가 파일을 확인하고 git 변경사항을 확인한 결과 dev 브랜치의 git log 변경사항에 다음 비밀번호에 대한 내용이 있는 것을 확인함.

```bash
git checkout dev

git log -p
commit e50e6cc6be6bc718f834b1584971b1039e4e87db (HEAD -> dev, origin/dev)
Author: Morla Porla <morla@overthewire.org>
Date:   Tue Oct 14 09:26:26 2025 +0000

    add data needed for development

diff --git a/README.md b/README.md
index 1af21d3..bc6ad3d 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for bandit30 of bandit.
 ## credentials

 - username: bandit30
-- password: <no passwords in production!>
+- password: qp...ZL
```

# Flag

`qp...ZL`
