# Category

web

# Overview

You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.
Your name:

# Analysis

- `print_credentials()`함수에서 세션에 `admin=1` 값이 존재하는 경우 다음 비밀번호를 획득할 수 있다.

  ```php
  function print_credentials() { /* {{{ */
      if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
        print "You are an admin. The credentials for the next level are:<br>";
        print "<pre>Username: natas21\n";
        print "Password: <censored></pre>";
      } else {
        print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas21.";
      }
  }
  ```

- 입력한 `name`값을 `session`의 `name`에 할당하며, `mywrite()` 함수에서 세션의 값인 `key`, `value` 형태를 `\n`를 통해 구분하여 문자열로 `$data`에 할당한다.

  `key`의 값은 `name`이며 `hello`를 입력한다면 `$data`에는 `name hello\n`와 같이 입력되는 것을 알 수 있다.

  ```php
  if(array_key_exists("name", $_REQUEST)) {
      $_SESSION["name"] = $_REQUEST["name"];
  }

  function mywrite($sid, $data) {
      // ...
      $filename = session_save_path() . "/" . "mysess_" . $sid;
      $data = "";
      ksort($_SESSION);
      foreach($_SESSION as $key => $value) {
          $data .= "$key $value\n";
      }
      file_put_contents($filename, $data);
      chmod($filename, 0600);
      return true;
  }
  ```

- `myread()` 함수에서는 `mywrite()`에서 생성한 `$data`값을 가져와 `\n`을 통해 `key`와 `value`로 나눠 세션에 할당한다.

  ```php
  function myread($sid) {
      // ...
      $data = file_get_contents($filename);
      $_SESSION = array();
      foreach(explode("\n", $data) as $line) {
          $parts = explode(" ", $line, 2);
          if($parts[0] != "") $_SESSION[$parts[0]] = $parts[1];
      }
      return session_encode() ?: "";
  }
  ```

# Exploitation

입력값에 대한 검증이 없이 `\n`을 통해 구분되며, `admin=1`이라는 값을 만들어 주기 위해 `value`를 `admin\nadmin 1`을 입력한다면, `mywrite()`에서 생성되는 `$data`는 `name admin\nadmin 1\n`이 저장된다.

이를 `myread()`에서 다시 읽어올 때 `\n`을 통해 `key`, `value`를 바꾸기 때문에 `name:admin`, `admin:1` 값으로 변환되며, 다음 비밀번호를 확인하는 `print_credentials()` 함수의 조건을 통과하게된다.

`name`에 대한 입력값을 `$_REQUEST`로 받고 있기 때문에, GET 메소드의 파리미터로 추가해서 요청이 가능하다.

`\n`의 값은 url인코딩으로 `%0A`, 공백은 `%20`를 나타내기 때문에, url을 `http://natas20.natas.labs.overthewire.org/index.php?name=admin%0Aadmin%201` 와 같이 요청하게 되면 다음 비밀번호를 알 수 있다.

# Flag

`BP...iH`
