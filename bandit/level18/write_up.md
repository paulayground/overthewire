# Problem Overview

다음 비밀번호는 홈디렉토리의 readme 파일에 존재함.
.bashrc의 설정으로 ssh 접근이 차단되어 있음

# Analysis

ssh 접근 시 Byebye !와 함께 커넥션이 종료되는 것을 확인함.

> ssh를 통한 쉘 접근만 가능한 것 아닌, ssh를 통해 명령어를 전달하고 응답을 받는 것을 확인하는 문제로 보임

# Exploitation Strategy

ssh를 통해 홈디렉토리의 readme를 읽어오는 명령어를 보내서 다음 비밀번호를 획득할 수 있을 것으로 보임.

# Execution

```
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

# Flag
