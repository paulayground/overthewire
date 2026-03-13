1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. data.txt의 내용이 base64로 인코딩 되어있어 `base64 -d data.txt`와 같이 디코딩하여 flag를 획득할 수 있다.