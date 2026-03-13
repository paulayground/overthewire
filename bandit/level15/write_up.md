# Problem Overview

현재 레벨의 비밀번호를 ssl/tls를 통해 30001포트로 전송하면 다음 비밀번호를 얻을 수 있음.

> ssl/tls를 통해 연결 후 데이터 전송을 할 수 있는지 확인하는 문제로 보임.

# Analysis

ssl/tls 접속을 위해 openssl s_client를 사용하여 30001포트의 연결을 하여, 서버의 ssl/tls 정보, 데이터 전송 가능 여부를 확인함.

# Exploitation Strategy

서버와 ssl/tls 연결 후 현재의 비밀번호를 보내 다음 비밀번호의 응답을 받을 수 있을 것이라 판단함.

# Execution

```
openssl s_client -connect localhost:30001
<CURRENT_PASSWORD>
Correct!
<NEXT_PASSWORD>
```

# Flag
