# 배운 점

`$0` 현재 실행중인 스크립트의 이름을 가져온다.
쉘스크립트의 경우 스크립트의 이름을 가져왔겠지만 `uppershell`의 경우 `system()`를 통해 사용자가 입력한 부분을 내부적으로 `sh`을 통해 실행하기 때문에 `$0`의 경우 `sh`로 치환되어 문제를 해결했다.

# 풀이 과정 기록

명령어를 사용해도 대문자로 바뀌고 처음에는 `sh`환경과 `bash`환경의 차이에 큰 생각을 안해 명령어를 실행했을 때, `bash`에서는 `LS: command not found`로 출력되는데 `sh`에서는 `sh: 1: LS: Permission denied` 라고 출력되어 이 프로그램이 어떻게 구성되어있을까 생각하는 과정에서 무슨 명령어를 못쓰게하는 권한 설정이 되어 있나 생각했는데 아니였다.
`$0`라는 것을 알지 못해서 풀 수가 없었는데, 아주 짤막한 힌트를 봤는데 그냥 답이 되었다. 아마도 명령어를 받아 명령어를 대문자로 바꾸고 그 결과를 실행하는 코드로 이루어진 프로그램 이였을텐데, `$0`의 경우 대문자 변경에 적용을 안받아서 이 프로그램이 실행되는 sh을 통해 나올 수 있었다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

`uppershell`을 열어보니까 예상한대로 `setuid`설정과 입력한 문구를 `toupper()` 하는 부분, `system()`으로 호출 하는 부분들을 확인했다.

```c uppershell
void main(undefined4 param_1,undefined4 param_2){
  __uid_t __euid;
  __uid_t __ruid;
  char *pcVar1;
  int iVar2;
  int in_GS_OFFSET;
  int local_418;
  char local_414 [1024];
  undefined4 local_14;
  undefined1 *puStack_10;

  puStack_10 = (undefined1 *)&param_1;
  local_14 = *(undefined4 *)(in_GS_OFFSET + 0x14);
  __euid = geteuid();
  __ruid = geteuid();
  setreuid(__ruid,__euid);
  puts("WELCOME TO THE UPPERCASE SHELL");
  while( true ) {
    printf(">> ");
    fflush((FILE *)0x0);
    pcVar1 = fgets(local_414,0x3ff,stdin);
    if (pcVar1 == (char *)0x0) break;
    for (local_418 = 0; local_414[local_418] != '\0'; local_418 = local_418 + 1) {
      iVar2 = toupper((int)local_414[local_418]);
      local_414[local_418] = (char)iVar2;
    }
    system(local_414);
  }
  exit(1);
}
```

# 한 줄 평

"어렵다... 힌트 없으면 못깼을 것 같다는 생각이 100%"

# 참고
