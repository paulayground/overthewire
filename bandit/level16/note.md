# 출제의도

포트 스캔을 통해 열려있는 포트 확인과 ssl/tls 를 사용하는 포트의 분류 여부, 또 s_client의 대화형 명령어를 우회할 수 있는지를 물어보는 문제로 보임.

# 배운 점

nmap -p 1-65535 와 같이 포트의 범위를 지정해서 스캔할 수 있음.
nmap -sV --version-light -p 31000-32000 localhost 통해서 확인이 가능하지만 응답에 시간이 걸렸음.
nmap --script ssl-enum-ciphers를 통해 ssl연결을 빠르게 지원하는 포트들을 찾을 수 있다.

openssl s_client를 통해 현재 비밀번호 시 비밀번호가 k로 시작하고 대화형 메시지에서 k(키 업데이트(tls1.3 only)), Q(커넥션 종료), R(ssl 재협상)등이 key update 등 지정된 값이라 계속 KEYUPDATE로 반응 했었다. -quiet 옵션을 통해 대화형 명령어를 끄고 나서 해결했다.

# 실수한 점

# 적용할 수 있는 곳

# 자동화 아이디어

# 사고 흐름 복기

서버의 tls버전이나 cipher가 달라 KEYUPDATE 응답이 계속되나 의심했었음.

처음부터 nmap script ssl-enum-ciphers 를 통해 쉽게 ssl/tls의 사용 포트를 찾았는데, 후에 nmap -sV를 쓰니 속도가 차이가 난다는 것을 느꼈다.

# 참고

- https://docs.openssl.org/3.0/man1/openssl-s_client/#notes
