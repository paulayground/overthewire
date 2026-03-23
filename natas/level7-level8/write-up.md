# Category

web

# Overview

Input secret:

# Analysis

`view sourcecode`를 통해 확인하면 아래와 같은 php코드가 존재하는 것을 알 수 있으며, 입력한 `secret`이 `base64_encode()`함수로 base64 인코딩되고 `strrev()` 문자열 뒤바꿈함수로 뒤바뀌고 `bin2hex()`를 통해 바이너리에서 hex값으로 바뀐 결과를 만들어 코드상에 적혀있는 `$encodedSecret`와 비교하여 다음 비밀번호를 얻을 수 있는 코드가 존재하며, 이는 제시된 `$encodedSecret`를 역순으로 변환하고 디코딩하여 원본값을 알아낼 수 있다.

```php
<?

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

function encodeSecret($secret) {
    return bin2hex(strrev(base64_encode($secret)));
}

if(array_key_exists("submit", $_POST)) {
    if(encodeSecret($_POST['secret']) == $encodedSecret) {
      print "Access granted. The password for natas9 is <censored>";
    } else {
      print "Wrong secret";
    }
}
?>

```

# Exploitation

1. 제시된 `$encodedSecret`를 역순으로 `hex2bin()`, `strrev()`, `base64_decode()`하여 변환 되기전 원본 `secret`를 확인한다.

   ```python
   def decode_secret(secret: str):
     return base64.b64decode(bytes.fromhex(secret)[::-1])
   ```

2. 획득한 secret을 제출하게되면 다음 비밀번호를 획들할 수 있다.

# Flag

`ZE..6t`
