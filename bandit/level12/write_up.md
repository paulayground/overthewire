1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. 헥스파일인 data.txt가 존재하며, `xxd -r`을 통해 바이너리 파일로 변경하였다.
3. `file -i`를 통해 파일의 형식을 확인하여 `data: application/gzip; charset=binary`로 압축되어 있는 것을 알 수 있다.
4. 해당 파일의 형식에 맞게 gzip으로 압축을 해제하고 나온 결과는 `bzip(data: application/x-bzip2; charset=binary)`, `tar(data: application/x-tar; charset=binary)`으로 반복적으로 압축이 되어있었으며, 마지막까지 압축을 해제할 경우 flag를 획득할 수 있다.
