1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. rot 13으로 인코딩 되어 있어 디코딩 하는 파이썬 스크립트를 만들어 `python rot_13.py < data.txt`를 통해 flag를 획득하였다.

---

[tr 사용]
글자를 로테이트 시킬 수 있는 tr을 통해
`cat data.txt | tr 'a-mn-zA-MN-Z' 'n-za-mN-ZA-M'`와 같이 13번째까지 밀어낸
a-m -> n-z, n-z -> a-m같이 변경하여 flag를 획득 할 수도 있다.
`cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'`
앞 부분의 범위를 한 번에 지정해서 사용도 된다.

