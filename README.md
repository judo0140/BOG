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

