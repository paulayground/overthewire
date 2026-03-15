# Category

web

# Overview

이 페이지에서 다음 단계의 비밀번호를 찾을 수 있지만, 마우스 오른쪽 버튼 클릭이 차단되었습니다!

# Analysis

우클릭 시 alert()창이 뜨게 되며, 소스 확인 결과 body의 oncontextmenu에 우클릭 방지 스크립트가 적용되어있음.

# Exploitation

우클릭 방지의 경우 아래와 같이 해결할 수 있으며, 별개로 개발자도구를 통해 비밀번호를 확인할 수 있었음

```js
document.querySelector("body").oncontextmenu = "";
```

# Flag

`Tg...lI`
