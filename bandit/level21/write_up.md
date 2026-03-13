# Problem Overview

프로그램이 cron을 통해서 정기적으로 실행되며, /etc/cron.d/ 설정을 확인하라

# Analysis

문제에 명시된 /etc/cron.d 에 다음 레벨의 유저이름인 bandit22의 이름이 들어간 cronjob_bandit22 파일을 발견하였고, 1초 마다 /usr/bin/cronjob_bandit22.sh를 실행하는 cronjob이 설정되어있는 것을 확인함.

> 프로그램을 정기적으로 실행 시킬 수 있는 cronjob에 대해 확인하라는 것으로 보임

# Exploitation Strategy

문제에서 제시한 /etc/cron.d에서 의심가는 부분들을 계속 따라 올라가면 다음 레벨의 비밀번호가 존재할 것으로 예상함.

# Execution

```bash
ls /etc/cron.d
cat cronjob_bandit22

cat /usr/bin/cronjob_bandit22.sh
```

# Flag

`tR...8Q`
