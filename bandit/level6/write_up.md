1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. 문제에 제시된 user가 bandit7이고 group이 bandit6이며 사이즈가 33바이트인 파일을 찾기 위해
`find / -user bandit7 -group bandit6`을 사용할 수 있다.
권한 없는 파일들도 대상이 되기 때문에 `Permission denied`메시지를 볼 수 있으며 `2> /dev/null`를 붙여
오류 메시지는 버리는 옵션으로 깔끔하게 남아있는 파일만 볼 수 있다.
`find / -user bandit7 -group bandit6 2> /dev/null`

`/var/lib/dpkg/info/bandit7.password` 값이 출력되어 확인해서 flag를 획득할 수 있다.