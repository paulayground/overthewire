# Category

linux

# Overview

bandit25에서 bandit26으로 로그인하는 건 꽤 쉬울 거야… 사용자 bandit26의 셸은 `/bin/bash`가 아니라 다른 거야. 그게 뭔지, 어떻게 작동하는지, 그리고 어떻게 빠져나올 수 있는지 알아내 봐.

# Analysis

홈디렉토리에 `bandit26.sshkey` 확인 후 bandit26으로 접속하였지만 ssh 접속 연결 후 bandit26이란 텍스트로 이루어진 그림이 출력 후 바로 종료되는 현상이 나타나 정상적인 접속이 불가했다.
bandit25로 돌아가 `/etc/passwd`의 bandit26의 로그인 쉘을 확인한 결과 `/usr/bin/showtext`가 실행되는 것을 확인하였으며 내용은 아래와 같다.

```bash /usr/bin/showtext
#!/bin/sh

export TERM=linux

exec more ~/text.txt
exit 0
```

bandit26 접속 시 홈디렉토리의 `text.txt`의 파일을 `more`를 이용해서 출력하기 때문에 bandit26 글자가 적혀있는 `text.txt`보다 화면이 큰 터미널에서 접속 시 `more`가 전부 다 읽히고 화면이 종료되는 문제를 확인했다.

# Exploitation

`text.txt`의 출력 크기보다 터미널 크기를 작게 조정해 접속하면 `text.txt`가 `more`로 다 출력되지 않아 `more`가 진행중인 상태가 되며 터미널이 종료되지 않는다.

`more` 상태에서 vi편집기로 넘어 간 후 명령모드에서 shell 환경변수를 수정하여 쉘로 접근할 수 있다.
쉘로 접근한 후 `/etc/bandit_pass/bandit26`에 적힌 다음 비밀번호를 확인할 수 있다.

```
# in more
# to vi editor
v

# in vi editor
:set shell=/bin/bash
:sh

# in shell
cat /etc/bandit_pass/bandit26
```

# Flag

`s0...CZ`
