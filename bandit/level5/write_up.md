1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. inhere 수 많은 디렉토리에서 문제에 일치하는 flag를 얻기위해 `find . -type f -size 1033c ! -executable -type f -exec file -i {} + | grep "text"`를 통해 사이트가 1033바이트에 맞고(`-size 1033c`) 실행가능한 파일이 아니면서(`! -executable`) 인간이 읽은 수 있는 파일인(`file -i | grep "text"`) 통해 flag 확득
