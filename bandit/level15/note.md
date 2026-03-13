# 출제의도

ssl/tls를 통해 서버와 연결하는 법, 또 데이터를 전송하고 서버의 ssl/tls 정보를 조회할 수 있는 것을 확인하는 문제로 보임.

# 배운 점

openssl s_client를 통해 해당 포트에 ssl/tls 연결 을 통해 해당 포트에서 어떤 인증서정보(인증서 공개키, CA, issuer, cipher, tls 버전 등)를 가져올 수 있는 것을 확인했다.

TLS 연결 흐름 요약

1. TCP 3-way handshake
2. TLS handshake
   • Client Hello
   • Server Hello
   • Certificate
   • Key exchange
3. 암호화 채널 확립
4. Application Data 전송

# 실수한 점

# 적용할 수 있는 곳

# 자동화 아이디어

# 사고 흐름 복기

처음에는 현재의 비밀번호를 암호화해야하는 건가? 싶어서 어떤 식으로 암호화를 해야하는 지 찾았다.
또 서버와 통신을 하면서 서버에서 규정한 ssl/tls 정보 (cipher 등)을 맞춰서 요청을 보내야 연결이 되는 것이 아닌가 생각했는데, 문제에서 제시된 명령어 모음 중에 openssl s_client를 보고 찾아 ssl/tls 연결 테스트 하는 방법을 보고 시도한 결과 답을 찾았다.

# 참고

- https://siyul-park.github.io/network/understanding-tls/
