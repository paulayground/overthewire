import requests

res = requests.get(
    url="http://natas4.natas.labs.overthewire.org/",
    headers={"Referer": "http://natas5.natas.labs.overthewire.org/"},
    auth=("natas4", "Qr...LQ"),
)

print(res.text)
