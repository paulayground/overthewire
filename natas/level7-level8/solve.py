from requests import request as req
import base64

encoded_secret = "3d3d516343746d4d6d6c315669563362";

def decode_secret(secret: str):
  print(secret)

  step1 = bytes.fromhex(secret)
  print(step1)

  step2 = step1[::-1]
  print(step2)

  step3 = base64.b64decode(step2)
  print(step3)

  return step3.decode()

decoded_secret = decode_secret(encoded_secret)

res = req(
  method="POST",
  url="http://natas8.natas.labs.overthewire.org/",
  auth=("natas8", "xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q"),
  data={
    "secret": decoded_secret,
    "submit": ""
  }
)

print(res.text)