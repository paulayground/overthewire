1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. inhere 디렉토리에 의심되는 `-file0*`와 같이 여러 개가 있다는 것을 확인
3. `file -i ./-file00`을 통해 `./-file00: application/octet-stream; charset=binary` 값이 나오는것을 알 수 있으며, 일반적인 텍스트 파일의 경우 `file -i ./-file07`을 통해 `./-file07: text/plain; charset=us-ascii` 값이 나오는것을 알 수 있다.
`text/plain`파일 만을 얻기 위해 `find . -type f -exec file {} + | grep "text"`를 통해 `./-file07: ASCII text`값을 얻을 수 있으며 해당 파일을 읽으면 flag를 얻을 수 있다.

```
// -type f :일반 파일을 찾는다
// -exec (\; or +) : 찾은 파일 뒤에 명령어 실행 \;(하나 찾을 때마다 명령 실행), +(다 찾고 모아서 실행)
// | grep "text" : text 값을 뽑는다

find . -type f -exec file {} + | grep "text"
```
