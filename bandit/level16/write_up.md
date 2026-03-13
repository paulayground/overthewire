# Problem Overview

현재 레벨의 암호를 localhost 31000~32000 범위의 포트로 전송해서 얻을 수 있음.
이러한 포트 중 실행 중인 포트를 찾을 것.
해당 포트 중 ssl/tls를 지원하는 서버와 지원하지 않는 서버를 확인할 것.

# Analysis

`nmap -sV --version-light -p 31000-32000 localhost` 통해 현재 열려있는 포트와 ssl/tls 정보를 31046, 31518(ssl), 31691, 31790(ssl), 31960를 확인함.

> 포트를 지정해서 스캔하고, 해당 포트에 ssl/tls가 적용되어 있는 것을 분류할 수 있는 지 여부와 ssl/tls 대화형 통신에 이미 지정된 단어들은 어떻게 피해서 원하는 정보를 얻을 수 있는지 확인하는 문제로 보임.

# Exploitation Strategy

nmap을 통해 분류한 ssl/tls를 지원하는 범위 내 열려있는 포트인 31518, 31790 포트에 현재 레벨 암호를 요청해 다음 암호를 얻을 수 있을 것이라고 예상함.

# Execution

```
nmap -sV --version-light -p 31000-32000 localhost
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
31691/tcp open  echo
31790/tcp open  ssl/unknown
31960/tcp open  echo

openssl s_client -connect localhost:31518

openssl s_client -connect localhost:31790
```

요청 후 현재 패스워드 전송 시 요청하는 현재의 패스워드가 k로 시작되기 때문에 서버에서 key update에 대한 요청으로 알고 응답으로 KEYUPDATE 응답이 돌아와 원하는 결과를 얻을 수 없음.
-quiet 옵션을 통해 대화형 명령어를 비활성화 시킨 뒤 다시 요청하면 정상적인 다음 단계에 대한 비밀키 정보를 얻을 수 있음.

```
echo <CURRENT_PASSWORD> | openssl s_client -quiet -connect localhost:31518
```

응답으로 요청한 값과 같은 값이 돌아오는 문제에 실패의 케이스로 제시된 포트라 제외함.

```
echo <CURRENT_PASSWORD> | openssl s_client -quiet -connect localhost:31790
```

응답으로 다음 레벨에 대한 비밀키값을 얻을 수 있음.

# Flag
