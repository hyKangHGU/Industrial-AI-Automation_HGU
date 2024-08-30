# Ubuntu 설치하기 (듀얼부팅)

- 참고자료
  - [ROS 개발환경 구축 - YouTube](https://youtu.be/x7tpah6Tiqw)

- PC 마다 설치 환경이 다르므로, 본 자료와 상이한 부분에 대해서는 충분히 검색 후, 안전하게 진행하는 것을 추천함.



## OS 설치용 USB 만들기



### Ubuntu 디스크 이미지 파일 

- [ubuntu 20.04.6 LTS](https://releases.ubuntu.com/focal/)

![ubuntu-20.04.6 disk image](https://user-images.githubusercontent.com/91526930/233799641-5a7e2ec0-93f8-427f-a42c-3a3e7925e8f4.png)



### USB에 디스크 이미지 굽기

- [Rufus 다운로드](https://rufus.ie/ko/)
  - 포터블 다운로드 시 설치 과정 없이 바로 실행 가능

![image](https://user-images.githubusercontent.com/91526930/233799896-4a051f93-a35a-496c-aa30-3db0d592216a.png)



- USB 연결
  - 디스크 이미지 파일 설치 시 USB 내의 파일들은 모두 사라지므로, 다른 저장소에 옮겨둘 것.



- rufus 실행

  - 업데이트 정책 - [아니오]
  - [장치] - USB 선택
  - [부트 유형 ] - [선택] - `ubuntu-(version)-desktop-amd64.iso` 열기![rufus_실행_디스크선택](https://user-images.githubusercontent.com/91526930/233800162-3994bbf3-f50c-4e09-97ef-5d1331e54ae1.png)

  

  - 파티션 구성 GPT/MBR 구분해서 선택.

    - 내 PC  GPT/MBR 확인 방법 (문서 하단 참고)

    ![rufus_파티션구성](https://user-images.githubusercontent.com/91526930/233800311-774ef86e-bcda-44cd-a72a-290af0ed118e.png)

    - 파일 시스템
      - GPT : FAT32(기본) 선택
      - MBR: FAT32 / NTFS 둘다 가능  // 특별한 경우가 아니라면, FAT32 추천

  

  - 디스크 이미지 굽기

    ![rufus_이미지 굽기](https://user-images.githubusercontent.com/91526930/233800405-18681b12-3a1b-44dd-b877-a045d1bf5682.png)

    

    - [ISO 이미지 모드로 쓰기(권장)] - OK

    - [데이터 모두 삭제] - OK

    - 완료되면, USB 내 파일 구성이 다음의 결과로 나타남.

      ![rufus_이미지굽기_완료](https://user-images.githubusercontent.com/91526930/233800461-98f5c213-e9b1-4238-8b03-9ae6da951b34.png)





## Ubuntu 설치하기

### 설치공간 확보 

- ubuntu20.04인 경우, 설치 중에 디스크 할당할 수 있음 (영상 확인할 것)

- [시작] - [컴퓨터 관리] -  [디스크 관리] - [주사용 디스크] - [우클릭] - [볼륨 축소]

  ![디스크_볼륨축소](https://user-images.githubusercontent.com/91526930/233800558-1c9838d6-6577-4872-a0b2-c3425e04ce84.png)

  <img src="https://user-images.githubusercontent.com/91526930/233800566-ac8a69e9-357c-4c01-a646-dd435e072f6c.png" alt="디스크_볼륨축소_할당" style="zoom:67%;" />



- 할당되지 않은 디스크 볼륨

![02_디스크_볼륨축소_결과](https://user-images.githubusercontent.com/91526930/233800577-49f4cb20-9fda-4434-ba43-8ef54f9cc441.png)



### 부팅 옵션 설정

**<주의사항>**  본격적인 우분투 설치 전, BitLocker 키를 백업할 것 !!! (문서 하단 참고)

- 설치용 USB 연결하고, Booting 후, BIOS 진입하기 (제조사별 BIOS 진입 key는 문서 하단 참고)
- 옵션 설정
  - 부팅순서는 USB를 1번으로 함.
  - Secure Boot : Disable
  - Fast Boot : Disable
  - UEFI mode 선택 (Legacy mode 선택 x)
  - AHCI mode 선택



### Ubuntu 설치

- 부팅 옵션 설정이 올바르게 되면, 설치용 USB에 의해 ubuntu 설치를 진행할 수 있음.

  ![image](https://user-images.githubusercontent.com/91526930/233800893-64b75d34-b087-4763-9bf1-b4b16455b678.png)



- Keyboard Layout -  [Continue]

- Updates and other software

  - Normal과 Minimal (상관없음)

  - Install third-party ~~ (선택)

    ![image](https://user-images.githubusercontent.com/91526930/233801007-d312d181-4284-457a-8b35-d2728353bc1f.png)

    

- Installation type

  - Something else 선택

    ![image](https://user-images.githubusercontent.com/91526930/233801028-3089aac4-310d-4416-ac42-340573d5d267.png)

  

  - Device 선택 및 설치

    - PC에 내장된 device 목록이 출력됨.

      ![image](https://user-images.githubusercontent.com/91526930/233801135-b4f1a4de-ea0d-4492-a38c-77195029c728.png)

    - 캡쳐본

      - /dev/sda 내에 sda1, sda2, sda3개의 드라이브가 역할에 따라 구분되어 있음.
      - /dev/sdb 내에 sdb1개만 있음. 용량을 비교했을 때, ubuntu 설치용으로 만들어 놓은 드라이브임.
      - 원래는 free space로 떠야 정상이나, 이번 케이스에 경우 PC가 임의로 만들어버린 공간이 존재함. 
      - 주황색으로 선택하고, 아래에 `-`  클릭해서 free space로 만들어줌.

      ![image](https://user-images.githubusercontent.com/91526930/233801431-6a0b2f75-c197-4006-9e1e-9eb346dbe51a.png)

    

    - `+` 클릭 후, 다음과 같이 설정하고, mount point는 `/` 를 입력한다.

      (windows에서 할당하지 않은 드라이브를 만들었던 것을 찾아서 진행하면 됨.)

      ![image](https://user-images.githubusercontent.com/91526930/233801511-ebf5c21f-c7c3-49f5-bcc6-77c24dd916ab.png)

      

    - Boot loader 선택

      - 캡처본에서는 물리적인 디스크가 2개이기 때문에, Ubuntu 설치하는 디스크에 boot loader를 설치했음.

      ![image](https://user-images.githubusercontent.com/91526930/233801651-2ff7a1cd-072b-4d99-9806-e84906008c5e.png)

      

    - Install Now 클릭 - [continue]

      - 만약, efi 관련하여 경고가 뜬다면, 문서 하단 참고할 것.

      ![image](https://user-images.githubusercontent.com/91526930/233801734-1cc16c7a-5714-4a97-9df6-1921901a262a.png)

    



### 설치 완료

- [재부팅] - [USB 제거] - [Set PC name & password]
  - 비밀번호는 짧게 하는게 편함.

![image](https://user-images.githubusercontent.com/91526930/233801833-1f2f3665-e533-4796-91ed-23a307837df5.png)





## 문제 해결

### BitLocker 키 백업 (필수)

**Ubuntu 듀얼 부팅 설치 전에** BitLocker 키를 백업해야 함.

- MS 계정으로 로그인하여 [내 계정]-[디바이스] 탭으로 접속

- 등록되어 있는 디바이스의 [Bitlocker 키 보기]를 통해 드라이브에 해당하는 키 ID를 확인 가능.

![Untitled](https://user-images.githubusercontent.com/91526930/233802004-2fe80c3f-2539-46d0-9705-1bf4201c3427.png)

- [운영 체제 드라이브]의 recovery key를 확인하고, 따로 적어둘 것. 같은 PC에 적어두면, 문제 생겼을 시 확인을 할 수 없으므로, **꼭 다른 곳에 적어두어야!**



- BitLocker 끄기

![Untitled2](https://user-images.githubusercontent.com/91526930/233802011-bb7591b6-ab2d-4557-a45b-48e1d0b4762c.png)



[Reference]

https://sol2gram.tistory.com/68

https://www.samsungsvc.co.kr/solution/25356





### 내 PC의 GPT/MBR 확인 방법

- [시작] - [컴퓨터 관리] - [디스크 관리] - [디스크 우클릭] - [속성] - [볼륨 탭]

![컴퓨터관리_디스크속성](https://user-images.githubusercontent.com/91526930/233802295-ff2a8325-bb08-4683-b830-c57ca0245a18.png)

![디스크속성_파티션형식](https://user-images.githubusercontent.com/91526930/233802314-119508c8-ec6a-4d98-91f7-7b5ff453d33e.png)



[Reference]

https://reason1241.tistory.com/15



### ubuntu 설치: 디스크 선택하여 진행 중에 EFI 관련 에러

캡처본의 경우,

- 각각 512GB 용량의 드라이브가 2개인 상황. 
  - dev/sda : windows가 설치되어 있음. (windows 부팅 관련한 것들이 포함됨)
  - dev/sdb : 아무것도 없음. (포맷된 상태)
- 보통은 free space 선택해서 ext4 ~ 선택하고, mount point `/` 만 입력해주면 잘 진행됨.
- 그러나, 이번 경우에는 efi 관련하여 에러메시지가 뜨면서, 설치해봤자 제대로 동작안할 것이라는 경고 문구를 띄워줌.
- 추측하면, efi라는 것은 부팅과 관련한 거 같음. 없으면 안될 거 같음.
- [free space 선택] - `+` 클릭 
  - 용량은 100MB ~ 150MB 할당
  - efi 선택하고, 생성.
  - 나머지 용량에 대해서는 ext4 journaling sytstem으로 선택하고 생성
  - 그 결과,![image](https://user-images.githubusercontent.com/91526930/233802422-f5c6e0a7-8beb-42ce-b0bd-9ee95a5e3b12.png)





### Ubuntu 설치 후, 듀얼부팅이 안되는 문제

부팅할 때, 윈도우/우분투 선택 창이 출력되지 않고, 바로 윈도우로 진입하는 경우

- 수동으로 부팅 메뉴 진입하여, 부팅 선택하기

  |  제조사  |               BIOS               |            Boot Menu            |
  | :------: | :------------------------------: | :-----------------------------: |
  | 삼성전자 |                F2                |        F10 / 일부는 ESC         |
  |  LG전자  |                F2                |     F10 (노트북) / F12(PC)      |
  |   한성   |                F2                |               F7                |
  |  TG삼보  |            F2 or Del             |               F12               |
  | 주연테크 |            F2 or Del             |               F7                |
  |    HP    | F10 or ESC(startup menu) and F10 | F9 or ESC(startup menu) and F10 |
  |  레노버  |          F2 / 일부는 F1          |               F12               |
  |   DELL   |                F2                |               F12               |
  |   ASUS   |            F2 or Del             |          ESC or F8(PC)          |
  |   MSI    |               Del                |               F11               |
  |   ACER   |                F2                |               F12               |
  | GIGABYTE |            F2 or Del             |               F12               |
  | TOSHIBA  |      F2 / 일부는 ESC and F1      |               F12               |
  |  INTEL   |                F2                |               F10               |

