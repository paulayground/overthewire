# 배운 점

`find`에서 `size`의 옵션들을 확인했다.

```bash
find . -size +N # N 크기 이상 검색
find . -size -N # N 크기 이하 검색
find . -size N # N 크기 검색

# c: byte
# k: KB
```

# 풀이 과정 기록

# 익스플로잇 코드 정리

```bash
# / 에서(/)
# 소유자가 bandit7(-user bandit7)
# 그룹이 bandit6(-group bandit6)
# 사이즈 33byte(-size 33c)
# stderr 버리기(2> /dev/null)
find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
```

# 심화 학습 (Deep Dive)

# 한 줄 평

"맨날 까먹는 find"

# 참고
