

# ROS Tutorial for Industrial AI & Automation



## Installation



### [Ubuntu](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ubuntu/install-ubuntu.md)



### [Utility Programs](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ubuntu/install-utility-programs.md)



### [ROS](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ubuntu/install-utility-programs.md)



### [ROS Packages for Robot](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-install-packages-for-robot.md)









## Tutorial



### 1. Ubuntu 기본

- [기본 명령어](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ubuntu/ubuntu-basic-command.md)

### 2. ROS 기본

- [talker & listener (노드와 메세지 통신 개념 이해하기)](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-talker-listener.md)

- [turtlesim 예제](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-turtlesim.md)
- [ROS build system](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-build-system.md)
- [패키지 설치와 복사](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-package.md)
- [카메라 연결 및 실행](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ros/ros-camera.md)

### 3. Simulation

- [Indy10](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/indy10/indy10-simulation.md)

- [UR5e](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ur5e/ur5e-simulation.md)

### 4. Robot Execution

- [Indy10](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/indy10/indy10-robot-execution.md)
- [UR5e](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/ur5e/ur5e-robot-execution.md)



## Source Program Description



## Trouble Shooting

- [한/영 키 설정](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/trouble%20shooting/trouble-hangeul-key.md)

- 윈도우 시간 설정



1) 환경 구축
	우분투 설치
		
	유틸 프로그램 설치 (사전 세팅)
		terminator 설치
		vs code
		github desktop
		한/영 키 설정

	ROS 설치
	conda 설치
	bashrc 세팅
	
2) 튜토리얼
	Ubuntu 기본
		OS 작동 메커니즘(하드웨어-커널-쉘-어플리케이션)
		CLI/GUI 개념
		주로 Terminal 활용/ 주요 명령어 소개(cd, ls, 파일/폴더 복사/생성, 설치/update, git 등)
		Terminal/bashrc/환경설정

	ROS 기본
		Work Space 생성
		catkin_make - 빌드개념/빌드를 해야하는 상황은?
		기본 명령어 (roscore/roslaunch/rosrun/roscd/rqt_graph 등)
		노드와 토픽 개념
		패키지 개념
		외부 패키지 설치 방법

	실습
		패키지 만들기
		노드와 토픽 만들기
			빌드 설정 파일 수정 포함
		빌드 설정하는 법
		이미지 정보 생성 및 불러오기
		launch 파일 만들기(기본/get_param/dependency??)
		pytorch 모델 활용 예제
		
3) 산업용 로봇 
	패키지 설치
		Ur5e
		Indy10
		work space로 복사하기
		catkin_make
	
	시뮬레이션
		UR5e
		Indy10
		rviz/gazebo --> plan & execute
		robot cmd: joint/absolute_pos/relative_pos/plan (move.py)
		MoveGroupInterface.py 이해하기
		(좌표계랑 함께 표기해서 해야)
		좌표계 변환??
		launch 파일??

	로봇 구동
		UR5e
		Indy10
		move.py

	데모
		pet_feeder.py
		
4) 기타
	카메라 연결/설치
	UR5e 매뉴얼 	(세팅/화면 구성/기초자료 파일)
	Indy10 매뉴얼	(세팅/화면 구성/기초자료 파일)

