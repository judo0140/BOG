# 0. 부가 설명

* BOG/scripts/bog_master.py -> PC의 ~/catkin_ws/src/bog_table/src 폴더로
* BOG/scripts/bog_dynamixel.py -> 라즈베리파이1 의 ~/catkin_ws/src/bog_table/src 폴더로
* BOG/scripts/bog_guide1.py -> 라즈베리파이1 의 ~/catkin_ws/src/bog_table/src 폴더로
* BOG/scripts/bog_guide2.py -> 라즈베리파이2 의 ~/catkin_ws/src/bog_table/src 폴더로
* BOG/scripts/bog_guide3.py -> 라즈베리파이3 의 ~/catkin_ws/src/bog_table/src

# 1. 소프트웨어 셋업

## 1.1 Ubuntu 18.04 ROS melodic 설치
http://wiki.ros.org/melodic/Installation/Ubuntu

## 1.2 라즈베리파이 ROS melodic 설치
http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi

## 1.3 OpenCR 보드 셋업
아두이노IDE 설치 : https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-linux
OpenCR 보드에 다이나믹셀 컨트롤을 위한 펌웨어 업로드 (OpenCR을 u2d2처럼 사용)
1) 아두이노IDE 실행
2) File -> Examples -> OpenCR -> 10.Etc -> usb_to_dxl 클릭
3) 업로드

## 1.4 다이나믹셀 구동을 위한 Dynamixel SDK 패키지 설치
참고 : https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/download/#repository
```
cd ~/catkin_ws/src

git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git

cd ..

catkin_make
```


--------------

# 2. ROS 네트워크 설정

## 2.1 고정 IP 할당
동일 네트워크망 안에서 고정 IP 할당
(참고 : https://raycat.net/5314)

L8326 iptime 공유기 (ssid : bog_5g)의 경우

* PC : 192.168.0.7
* 라즈베리파이1 : 192.168.0.4
* 라즈베리파이2 : 192.168.0.5
* 라즈베리파이3 : 192.168.0.6

## 2.2 ROS ~/.bashrc 파일 수정
1) PC

터미널 실행 후
```
nano ~/.bashrc
```
네트워크 설정 변경

![Screenshot from 2022-04-08 15-49-08](https://user-images.githubusercontent.com/61779427/162380194-f8f43f7e-526e-4d51-b5f8-51d39432f2d2.png)

파일 저장 후
```
source ~/.bashrc
``` 
2) 라즈베리파이 (ROS_HOSTNAME에 각 고정 IP)

터미널 실행 후
```
nano ~/.bashrc
```
네트워크 설정 변경

![Screenshot from 2022-04-08 15-51-18](https://user-images.githubusercontent.com/61779427/162380446-398d917a-8f0c-43b9-94c3-0036861b85b7.png)

파일 저장 후
```
source ~/.bashrc
```
--------------
# 3. 하드웨어 셋업
--------------
# 4. 실행
## 4.1 ROS 및 노드 실행

리니어 가이드의 컵 구동부는 테이블 사이드로 배치

1) PC
```
roscore

rosrun bog_table bog_master.py
```
2) 라즈베리파이1

터미널 창을 2개 실행시켜 노드 2개를 실행시켜야 한다
```
rosrun bog_table bog_guide1.py
```
```
rosrun bog_table bog_dynamixel.py
# dynamixel 구동을 위한 노드
```
3) 라즈베리파이2
```
rosrun bog_table bog_guide2.py
```
4) 라즈베리파이3
```
rosrun bog_table bog_guide3.py
```

## 4.2 조작

컵, 다이나믹셀 위치 입력 후 실험 시나리오에 맞게 조작

![Screenshot from 2022-04-08 18-11-13](https://user-images.githubusercontent.com/61779427/162404612-8f359e8c-8b80-4d11-80ca-3351a890ebfb.png)

