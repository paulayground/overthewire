# Category

web

# Overview

input secret:

# Analysis

- `input secret`이라는 인풋박스와 `view sourcecode`를 통해 해당 페이지의 php 소스코드를 볼 수 있음

- html body 안에 실행되는 php코드가 있는 것을 알 수 있음

  ```php
  <?
  include "includes/secret.inc";
  if(array_key_exists("submit", $_POST)) {
      if($secret == $_POST['secret']) {
        print "Access granted. The password for natas7 is <censored>";
      } else {
        print "Wrong secret";
      }
  }
  ?>
  ```

  `submit`을 통해 `input secret`의 값을 찾아 `$secret`과 일치 여부를 검사하여 통과하기 때문에 `$secret`이 어떤 값인지 찾아보기 위해, `include "includes/secret.inc"`를 통해 가져오는 `includes/secret.inc`를 확인해볼 수 있다.

# Exploitation

`/includes/secret.inc`의 경로로 요청 결과 `$secret` 변수가 선언된 페이지가 나오고 해당 값을 확인할 수 있다. 이 값을 `input`에 입력하여 코드와 일치 시키면 다음 비밀번호를 알 수 있다.

```
http://natas6.natas.labs.overthewire.org/includes/secret.inc
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```

# Flag

`bm...GS`
