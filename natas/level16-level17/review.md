# 배운 점

SQL Where 조건에 `SLEEP()` 사용

# 풀이 과정 기록

`$query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";` 을 통해 sql injection을 파악했다.

하지만 응답을 보니 응답이 주석으로 되어있어 맞는값인지 틀린값인지 알 수가 없었다.

네트워크 응답을 비교해보며 살펴봐도 응답의 값은 같았기 때문에, 별 다른 소득은 없었다.

찾아본 결과 응답이 없을 경우 지연을 통해서 유추할 수 있다는 것을 확인했고 `SLEEP()`의 사용이 가능한 것을 알게되었다.

# 익스플로잇 코드 정리

solve.py

# 심화 학습 (Deep Dive)

# 참고
