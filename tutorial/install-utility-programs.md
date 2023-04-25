# Utility Programs Installation

- Terminator

- Visual Studio Code
- Github Desktop





## Terminator

ubuntu의 terminal을 더 편리하게 사용할 수 있는 프로그램이다. 

- Install

```bash
$ sudo apt update
$ sudo apt install terminator
```



- Preferences

  - Terminator 실행 후, 우클릭하여 preferences 진입
  - 사용자에 맞게 환경설정 가능.

  
  
  





## Visual Studio Code

프로그래밍 개발도구로서, 폴더와 파일 목록을 손쉽게 볼 수 있어, ros 입문자에게 매우 편리하다.



- 설치파일 다운로드 `.deb file` -  [vs code](code.visualstudio.com)

  ![image](https://user-images.githubusercontent.com/91526930/234137097-3f1d94a7-f951-47ab-a5ae-b5ff42808324.png)



- unpack

  다운로드한 파일은 `home/Downloads` 경로에 존재한다.

```bash
$ cd ~/Downloads
$ sudo dpkg -i code_*.deb
```







## Github Desktop

github에서는 ubuntu에 Github Desktop 프로그램을 제공하지 않으나, 개인이 자체적으로 프로그램을 수정하여 배포한 프로그램이다.

```bash
$ sudo apt-get update
$ sudo apt-get install snapd
$ sudo snap install GitHubDesktop-linux-2.0.4-linux1.snap --classic --dangerous
```


