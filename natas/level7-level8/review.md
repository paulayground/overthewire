# 배운 점

# 풀이 과정 기록

# 익스플로잇 코드 정리

```python
import base64

encoded_secret = "3d3d516343746d4d6d6c315669563362";

def decode_secret(secret: str):
  # hex encoded_secret을 바이트로 변환하여 가져옴
  step1 = bytes.fromhex(secret)

  # 변환된 바이트를 뒤집기
  step2 = step1[::-1]

  # 뒤집힌 바이트를 base64 decoding
  step3 = base64.b64decode(step2)

  return step3.decode()
```

# 심화 학습 (Deep Dive)

# 한 줄 평

"natas는 예전에 만들어진 서비스라 그런가 php만 계속 나오려나..."

# 참고
