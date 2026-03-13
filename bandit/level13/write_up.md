# Problem Overview

- bandit14의 패스워드는 /etc/bandit_pass/bandit14에 있으며 bandit14만 읽을 수 있다.
- 이번 레벨에서는 패스워드 대신 private SSH key가 제공된다.

> 비밀번호가 아닌 private key 기반 SSH 인증을 이해하고 활용하는 문제

# Analysis

bandit13 계정에 비밀키가 존재하며, 비밀키를 통해 bandit14 계정으로 SSH 접속을 해야 한다.

# Exploitation Strategy

1. bandit13 user의 홈에 sshkey.private를 확인해 받은 키를 로컬에 저장하고, bandit14 유저로 `ssh -i`로 비밀키를 이용해 접속한다.
2. private key는 권한이 너무 넓으면 SSH에서 거부되므로 권한을 제한해야 한다.
3. 문제에 제시된 패스워드 파일인 /etc/bandit_pass/bandit14를 확인한다.

# Execution

```
# USER bandit13
cat sshkey.private

# LOCAL
scp -P 2220 bandit13@bandit.labs.overthewire.org:/home/bandit13/sshkey.private ~
chmod 400 ~/sshkey.private
ssh -i ~/sshkey.private bandit14@bandit.labs.overthewire.org -p 2220

# USER bandit14
cat /etc/bandit_pass/bandit14
```

# Flag

-
