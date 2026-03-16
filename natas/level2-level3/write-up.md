# Category

web

# Overview

There is nothing on this page

# Analysis

html 내에 단서가 될 부분이 크게 없었고, 굳이 찾자면 주석으로 아래와 같이 구글도 찾을 수 없다는 암시적인 힌트가 있었다.

```html
<!-- No more information leaks!! Not even Google will find it this time... -->
```

크롤링봇들이 사이트 수집 허용여부를 위해 확인하는 `robots.txt`를 확인한 결과 아래와 같이 `Disallow`한 부분에 수상한 경로를 확인했다.

```txt robots.txt
User-agent: *
Disallow: /s3cr3t/
```

# Exploitation

의심스러운 경로인 `/s3cr3t/` 에 접속한 결과 아래와 같이 `users.txt`파일이 존재한다는 것을 확인하였고, 해당 파일을 확인한 결과 다음 비밀번호를 얻을 수 있었다.
![alt text](../images/img2-3.png)

```
http://natas3.natas.labs.overthewire.org/robots.txt

http://natas3.natas.labs.overthewire.org/s3cr3t/

http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
```

# Flag

`Qr...LQ`
