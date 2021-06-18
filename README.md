# Pygame을 이용한 시뮬레이터 제작

## 1. 구동 방식

![SE-00cc08ce-56c6-4283-83b2-949cc14cb873](https://user-images.githubusercontent.com/59854960/121287459-8c987100-c91c-11eb-88f9-72bd1eae43f8.png)

- 키보드 위쪽 -> 전진
- 키보드 아래쪽 -> 후진
- 키보드 오른쪽 -> 우회전
- 키보드 왼쪽 -> 좌회전

자동차의 움직임에 맞게 경로를 그려준다.

경로 궤적을 사각형과 곡선으로 표시해준다.


## 2. 실행 결과
### (1)ver_1
![SE-c14c9968-d688-4d2b-a153-9cd79691d9e4](https://user-images.githubusercontent.com/59854960/121288306-21e83500-c91e-11eb-95fd-100237e37790.png)

### (2)ver_2
![SE-58c3b793-6d61-487b-ae0b-eb2d8ed2b38c](https://user-images.githubusercontent.com/59854960/121287119-f49a8780-c91b-11eb-8730-0ed05807731f.png)

실행 결과 다음과 같은 화면을 확인할 수 있다.

### (3)crush
![SE-29003da8-30bb-4a07-ad97-055ea924ed69](https://user-images.githubusercontent.com/59854960/121472940-de182d00-c9fc-11eb-848e-0e22a27141c1.png)
움직이는 자동차와 정지해있는 자동차가 존재한다.
두 개의 자동차가 충돌하면 충돌 감지를 한다.

![SE-48107f99-68ec-4cf2-88a9-240f8baf6b12](https://user-images.githubusercontent.com/59854960/121472936-dce70000-c9fc-11eb-8300-2706f0748351.png)

충돌 감지 후 pygame을 종료한다.

### (4)path planning
![SE-bee665ce-8d12-485c-b451-57d3f45aa934](https://user-images.githubusercontent.com/59854960/121996862-565b6580-cde4-11eb-94a8-5f3264b8de54.png)
키보드 입력에 따라 시작 위치를 다르게 조정한다.
민트색 선은 path planning을 통해 유추한 위치이다.

