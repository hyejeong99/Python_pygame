#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame
import numpy as np
from math import sin, radians, degrees, copysign

class Car:
    #생성자 함수
    def __init__(self, x, y, yaw=0.0, max_steering=30, max_acceleration=1000.0):
        self.x = x
        self.y = y
        self.Arr_x = []
        self.Arr_y = []
        self.Arr_xl = []#수정
        self.Arr_yl = []#수정   

        #yaw 값
        self.yaw = yaw
        #최대 가속도 값
        self.max_acceleration = max_acceleration
        #최대 조향각 값
        self.max_steering = max_steering
        #브레이크로 인한 감속 가속도값 (스페이스바를 누르는 경우 사용됨)
        self.brake_deceleration = 300
        #정지마찰력으로 인한 감속 가속도값 (키 눌림이 없는 경우 (엑셀에서 발을 뗀 경우) 적용됨)
        self.free_deceleration = 50

        #선형 가속도
        self.linear_acceleration = 10.0
        #선속도
        self.linear_velocity = 0.0
        #최대 속도
        self.max_velocity = 1000
        #조향각
        self.steering_angle = 0.0
        #자동차 휠베이스 (축거 : 앞바퀴축과 뒷바퀴축 사이의 거리)        
        self.wheel_base = 84

        #자동차 이미지 좌표 (가로x세로 128x64 픽셀의 자동차 그림파일. car.png)
        self.car_img_x = 0
        self.car_img_y = 0
        self.car_x_ori = [-64,-64, 64, 64] # 왼쪽 위아래, 오른쪽 위아래 포인트 총4개
        self.car_y_ori = [-32, 32,-32, 32] # 왼쪽 위아래, 오른쪽 위아래 포인트 총4개
        
    def update(self, dt):
        #선속도를 계산한다. (선속도=선형가속도x단위시간)
        self.linear_velocity += (self.linear_acceleration * dt)
        #선속도를 (-100,100) 사이로 값을 제한한다.
        self.linear_velocity = min(max(-self.max_velocity, self.linear_velocity), self.max_velocity)

        self.angular_velocity = 0.0
        
        #조향각이 0이 아니라면
        if self.steering_angle != 0.0:
            #각속도를 계산한다. 각속도=(선속도/회전반지름)        
            self.angular_velocity = (float(self.linear_velocity) / float(self.wheel_base)) * np.tan(np.radians(self.steering_angle))
        
        #각변위를 계산해 angle 값에 더해준다. (각속도x시간=각변위)
        self.yaw += (np.degrees(self.angular_velocity) * dt)
        #이동변위를 계산해 spatium(이동거리) 값에 적용한다. (선속도x시간=이동변위)
        self.spatium = self.linear_velocity * dt
        #삼각비를 이용해 x,y 좌표를 구해준다.
        self.x += (self.spatium * np.cos(np.radians(-self.yaw)))
        self.y += (self.spatium * np.sin(np.radians(-self.yaw)))
        
        car_x = [0,0,0,0]
        car_y = [0,0,0,0]
        for i in range(4):
            car_x[i] = self.car_x_ori[i] * np.cos(-radians(self.yaw)) - self.car_y_ori[i] * np.sin(-radians(self.yaw)) + self.x
            car_y[i] = self.car_x_ori[i] * np.sin(-radians(self.yaw)) + self.car_y_ori[i] * np.cos(-radians(self.yaw)) + self.y 
        self.car_img_x = int(round(min(car_x)))
        self.car_img_y = int(round(min(car_y)))
        print('x, y' , self.x, self.y)
        print('x', self.car_img_x)
        print('y', self.car_img_y)

        print("시간:",round((pygame.time.get_ticks()/1000)%1, 1))
        py_time = round((pygame.time.get_ticks()/1000)%1, 1)
        #큐에 자동차 위치 append_plus
        self.Arr_xl.append(car_x)#수정
        self.Arr_yl.append(car_y)#수정
        if py_time==0.2 or py_time==0.4 or py_time==0.6 or py_time==0.8:#수정
            self.Arr_x.append(car_x)
            self.Arr_y.append(car_y)

#pygame을 초기화 하는 함수
pygame.init()

#windows title을 정하는 함수
pygame.display.set_caption("Pygame Car Simulator #1")

#pygame window size 설정
width, height = 1280, 720 

#설정된 windows size를 적용하는 함수
screen = pygame.display.set_mode((width, height))

#while 루프 반복주기. 화면갱신 FPS를 설정하기 위한 시간객체 생성
clock = pygame.time.Clock()

#Car 객체 생성
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "car.png")
car_image = pygame.image.load(image_path)
car = Car(100,100)

#아래 while 루프를 종료시키기 위해 선언하는 변수
exit_flags = False

while not exit_flags:

    #while 루프 반복주기. 화면갱신 FPS를 설정.
    clock.tick(60)

    #단위시간의 크기 설정 - 단위시간이란 1 frame이 지나가는데 걸리는 시간이다.
    #해당 시간이 있어야 속력=거리/시간 등의 공식을 계산할 수 있다.
    dt = float(clock.get_time()) / float(1000)
    
    #이벤트 감지. 여기선 종료이벤트만 확인하여 루프 종료변수를 True로 변경
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_flags = True
           
    #입력된 키보드값을 가져와서 pressed 변수에 입력
    pressed = pygame.key.get_pressed()

    #키보드의 위쪽 방향키가 눌러졌을 경우
    if pressed[pygame.K_UP]:
        #선속도가 음수라면 (현재 후진중이라면)
        if car.linear_velocity < 0:
            #브레이크 감속가속도가 적용된다.
            car.linear_acceleration = car.brake_deceleration
        #선속도가 양수라면 (현재 전진중이라면)
        else:
            #선가속도를 (+)방향으로 증가시킨다.(점점 빠르게 전진하도록)
            car.linear_acceleration += 10 * dt
            
    #키보드의 아래쪽 방향키가 눌러졌을 경우
    elif pressed[pygame.K_DOWN]:
        #선속도가 양수라면 (현재 전진중이라면)
        if car.linear_velocity > 0:
            #브레이크 감속가속도가 적용된다.
            car.linear_acceleration = -car.brake_deceleration
        #선속도가 음수라면 (현재 후진중이라면)
        else:        
            #선가속도를 (-)방향으로 증가시킨다. (점점 빠르게 후진하도록)            
            car.linear_acceleration -= 10 * dt
            
    #키보드의 스페이스키가 눌러졌을 경우
    elif pressed[pygame.K_SPACE]:
        #선속도가 (브레이크 감속가속도 x 단위시간)보다 크다면
        if abs(car.linear_velocity) > dt * car.brake_deceleration:
            #copysign(double x, double y); y의 부호를 x의 부호로 사용
            #브레이크 감속가속도만큼 빼서 선가속도를 줄인다. 빠르게 멈춘다.
            car.linear_acceleration = -copysign(car.brake_deceleration, car.linear_velocity)
        #선속도가 (브레이크 감속가속도 x 단위시간)보다 작다면
        else:
            #선속도/단위시간=선가속도 만큼 뺀다. 즉, 가속도값이 0이 되어 멈춘다.
            car.linear_acceleration = -float(car.linear_velocity) / float(dt)
    
    #그 외의 키보드키가 눌러졌을 경우    
    else:
        #선속도가 (정지마찰력 감속가속도 x 단위시간)보다 크다면
        if abs(car.linear_velocity) > dt * car.free_deceleration:
            #copysign(double x, double y); y의 부호를 x의 부호로 사용
            #정지마찰력이 적용돼 서서히 멈춘다.
            car.linear_acceleration = -copysign(car.free_deceleration, car.linear_velocity)
        #선속도가 (정지마찰력 감속가속도 x 단위시간)보다 작다면
        else:
            #단위시간이 0이 아니라면
            if dt != 0:
                #선속도/단위시간=선가속도 만큼 뺀다. 즉, 가속도값이 0이 되어 멈춘다.
                car.linear_acceleration = -float(car.linear_velocity) / float(dt)
    
    #선가속도의 범위를 (-1000.0~1000.0)사이의 값으로 제한한다.    
    car.linear_acceleration = max(-car.max_acceleration, min(car.linear_acceleration, car.max_acceleration))

    #키보드의 오른쪽 방향키가 눌러졌을 경우 
    if pressed[pygame.K_RIGHT]:
        #우회전한다. 30x단위시간으로 계산된 각도만큼 뺀다.
        car.steering_angle -= 30 * dt
        
    #키보드의 왼쪽 방향키가 눌러졌을 경우     
    elif pressed[pygame.K_LEFT]:
        #좌회전한다. 30x단위시간으로 계산된 각도만큼 더한다.
        car.steering_angle += 30 * dt
        
    #조향관련 키가 아무것도 눌러지지 않았을 경우    
    else:
        #조향각을 '0'으로 설정한다.
        car.steering_angle = 0
        
    #steering의 범위를 (-30~30)사이의 값으로 제한한다.   
    car.steering_angle = max(-car.max_steering, min(car.steering_angle, car.max_steering))

    #자동차의 상태를 단위시간마다 업데이트 해준다.
    car.update(dt)

    #스크린 배경을 검은색으로 지정한다.->흰색_plus
    screen.fill((255, 255, 255))

    #자동차 이미지 (car.png)를 회전시킨다.
    rotated = pygame.transform.rotate(car_image, car.yaw)

    #자동차 이동 궤적 그리기_plus  
    for i in range(len(car.Arr_x)):
        #car_xc = (car.Arr_x[i][0]+car.Arr_x[i][1])/2
        #car_yc = (car.Arr_y[i][0]+car.Arr_y[i][1])/2


        #pygame.draw.circle(screen, (255, 0, 0), [int(car_xc), int(car_yc)], 5)
        pygame.draw.line(screen, (0, 0, 255), [car.Arr_x[i][0], car.Arr_y[i][0]], [car.Arr_x[i][1],car.Arr_y[i][1]], 5)
        pygame.draw.line(screen, (0, 0, 255), [car.Arr_x[i][0], car.Arr_y[i][0]], [car.Arr_x[i][2],car.Arr_y[i][2]], 5)
        pygame.draw.line(screen, (0, 0, 255), [car.Arr_x[i][1], car.Arr_y[i][1]], [car.Arr_x[i][3],car.Arr_y[i][3]], 5)
        pygame.draw.line(screen, (0, 0, 255), [car.Arr_x[i][3], car.Arr_y[i][3]], [car.Arr_x[i][2],car.Arr_y[i][2]], 5)#수정 2->5

    #자동차 이동 선 그리기_plus #수정
    for i in range(len(car.Arr_xl)):
        car_xc = (car.Arr_xl[i][0]+car.Arr_xl[i][1])/2#수정
        car_yc = (car.Arr_yl[i][0]+car.Arr_yl[i][1])/2#수정
        pygame.draw.circle(screen, (255, 0, 0), [int(car_xc), int(car_yc)], 5)


    #회전된 자동차 이미지를 계산된 위치에 그린다.
    screen.blit(rotated, [car.car_img_x, car.car_img_y])


    #화면을 갱신한다.
    pygame.display.flip()

#while 루프를 빠져나왔으므로 프로그램을 종료한다
pygame.quit()
