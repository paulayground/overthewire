# Overview

시간 기반 작업 스케줄러인 cron에서 정기적으로 자동 실행되는 프로그램이 있습니다. `/etc/cron.d/` 디렉터리에서 구성을 확인하고 어떤 명령어가 실행되는지 살펴보세요.

# Analysis

문제에서 제시된 `/etc/cron.d`에 다음 레벨 유저인 `bandit23` 유저명으로 작성된 `cronjob_bandit23`파일을 찾았고, 확인할 결과 `cronjob_bandit23.sh`파일이 실행되는 라인이 있었다.

`cronjob_bandit23.sh`은 현재 접속한 유저이름을 기반으로 md5로 인코딩해서 유저의 비밀번호를 /tmp 경로 옮기는 코드로 구성되어있다.

```bash
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

# Exploitation

다음 비밀번호인 bandit23유저의 비밀번호를 얻기위해 md5를 직접 인코딩하여 `$mytarget`을 유추할 수 있다.

```
echo "I am user bandit23" | md5sum | cut -d ' ' -f 1
```

`tmp/<생성된 결과>`를 조회하게 되면 다음 비밀번호를 얻을 수 있다.

# Flag

`0Z...Ga`
