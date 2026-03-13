# Problem Overview

현재 레벨의 비밀번호를 로컬호스트 30000 포트로 전송하면 비밀번호를 얻을 수 있음.

> 지정한 포트로 데이터를 포함한 요청할 수 있는지 확인하는 문제

# Analysis

nmap을 통한 30000포트에 ndmps라는 서비스가 동작하고 있는 것을 확인하였고, nc를 통해 30000포트의 tcp 연결이 성공적으로 이루어진다는 것을 확인함.

# Exploitation Strategy

nc를 통해 현재 비밀번호를 전송하면, 다음 레벨의 비밀번호인 응답을 얻을 수 있을 것이라고 판단함.

# Execution

```
echo <CURRENT PASSWORD> | nc localhost 30000
Correct!
<NEXT PASSWORD>
```

# Flag

-
