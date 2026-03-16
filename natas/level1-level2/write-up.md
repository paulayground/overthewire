# Category

web

# Overview

There is nothing on this page

# Analysis

문제에 이 페이지에는 아무것도 없다는 내용의 힌트와 페이지내 의미없는 1px의 이미지가 `files/pixel.png` 경로로 존재하는 것을 보아 다른 페이지에 정보가 있을 것으로 확인됨.

# Exploitation

`/files` 경로에 이미지 말고 다른 파일이 존재하는 지 접속한 결과, `pixel.png` 이외에 `users.txt` 파일이 존재한다는 것을 확인했으며 `users.txt` 파일 내부에 다음 레벨에 대한 비밀번호를 확인할 수 있음.
![alt text](../images/img1-2.png)

# Flag

`3g...YH`
