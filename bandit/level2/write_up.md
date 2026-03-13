1. 이전 레벨에서 획득한 pw로 ssh를 통한 host의 2220으로 접속
2. 의심되는 파일이 `--spaces in this filename--` 와 같이 되어있어, 일반적으로 `cat --spaces in this filename--`으로 열게 될 경우 옵션을 나타내는 `--`와 겹치게되어 파일을 제대로 읽을 수 가 없다.
이전 단계와 마찬가지로 `cat ./--spaces in this filename--`를 통해 flag를 획득할 수 있다.