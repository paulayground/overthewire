# 배운 점

`Referer` 요청이 어떤 페이지에서 왔는 지 적힌 헤더. 전체 url(path, query string)이 찍히며, 이로인해 민감정보 노출 위험이 있어서 `Referrer-Policy`로 제한할 수 있다. 마케팅, seo 분석할 때 많이 쓴다

`Origin` 요청이 어떤 사이트에서 왔는 지 적힌 헤더. `referer`와 달리 사이트의 호스트만 보여주며, cors요청, 상태 변경 메소드같은 곳에 사용된다.

# 풀이 과정 기록

처음에는 어디서 왔는지 기록을 남기는 곳이라고 생각은 했지만 `referer`가 생각이 안나고 `origin` 문제인가? 생각했는데, 서로간의 차이와 개념에 대해서 잘 몰라서 혼동한 것 같다. 문제 푸는 것에는 지장은 없었지만 다시 한 번 정리하는 기회가 됐다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

버프스위트 말고도 그냥 `curl` 요청을 통해서 `referer`값을 지정해 응답을 받을 수도 있다.

```
curl -u natas4:Qr...LQ -H "Referer: http://natas5.natas.labs.overthewire.org/" http://natas4.natas.labs.overthewire.org/
```

# 한 줄 평

"슬슬 공부할게 나오는구만"

# 참고
