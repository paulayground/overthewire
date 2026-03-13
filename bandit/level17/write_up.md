# Problem Overview

password.old, password.new 2개의 패스워드 파일이 존재함.
다음 패스워드는 password.new에 존재하며, password.old, password.new 사이의 변경된 줄임.

# Analysis

password.old, password.new 2개의 text/plain 파일 확인함.

> diff를 통한 내용에 대한 차이를 비교하여 해결할 수 있는지 확인하는 문제

# Exploitation Strategy

diff를 통해서 둘 텍스트파일의 차이점을 찾으면 될 것으로 보임

# Execution

```
diff password.new password.old
```

# Flag
