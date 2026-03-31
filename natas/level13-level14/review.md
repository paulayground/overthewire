# 배운 점

처음에는 아래와 같이 참이되는 조건을 만들기 위해 `" or password like "%`를 사용했는데, 리뷰하면서 `" or 1=1 #`를 사용하는게 더 깔끔하고 직관적인 방식인 것을 알게됐다.

```sql
SELECT *
from users
where username="<>"
and password="<" or password like "%>"
```

# 풀이 과정 기록

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

# 참고
