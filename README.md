# Pygame을 이용한 시뮬레이터 제작

### 1. pygame_keyEvent

![SE-00cc08ce-56c6-4283-83b2-949cc14cb873](https://user-images.githubusercontent.com/59854960/121287459-8c987100-c91c-11eb-88f9-72bd1eae43f8.png)

- 키보드 위쪽 -> 전진
- 키보드 아래쪽 -> 후진
- 키보드 오른쪽 -> 우회전
- 키보드 왼쪽 -> 좌회전

자동차의 움직임에 맞게 경로를 그려준다.

경로 궤적을 사각형과 곡선으로 표시해준다.

### 2. pygame_simul_carbody_crush

![SE-cc339abc-ad9a-458e-a480-f8291b916534](https://user-images.githubusercontent.com/59854960/122493971-8ba1c680-d023-11eb-94cc-f41761d1cf7b.png)

- 키보드 위쪽 -> 전진
- 키보드 아래쪽 -> 후진
- 키보드 오른쪽 -> 우회전
- 키보드 왼쪽 -> 좌회전

정지한 자동차와 충돌하면 pygame 종료

### 3. pygame_pathPlanning

#### 파일 실행 순서
1. roscore 돌리기
2. 파이썬 파일 실행

- 키보드 1, 2, 3, 4 누르면 각각 다른 위치에서 시작
- 키보드 q 누르면 pygame 종료
- 자동차가 AR태그로부터의 자신의 x, y, yaw 값 pub(ar_x, ar_y, ar_yaw)
- 자동차 이동 궤적 표현(사각형, 선)
- Path Planning 알고리즘 이용해 경로 계획&stanley 이용해 주차

![SE-179d5d07-f32a-478d-a29d-822a4b4acfff](https://user-images.githubusercontent.com/59854960/122492679-2b118a00-d021-11eb-92ad-513145e0afab.png)

키보드 입력 1 -> 1번 위치에서 실행

![SE-a88332b3-74e9-4f1d-a3f9-d4d859c76318](https://user-images.githubusercontent.com/59854960/122492684-2c42b700-d021-11eb-9cb5-5b52daaf5599.png)

키보드 입력 2-> 2번 위치에서 실행

![SE-96118ff5-bcfb-4000-99e2-43555e00d350](https://user-images.githubusercontent.com/59854960/122492685-2d73e400-d021-11eb-979f-24cda1f4ba83.png)

키보드 입력 3-> 3번 위치에서 실행

![SE-f53d68fb-2e9c-4d67-9151-da707007807c](https://user-images.githubusercontent.com/59854960/122492687-2ea51100-d021-11eb-9522-46eb9be510a9.png)

키보드 입력 4 -> 4번 위치에서 실행

![SE-84e682f8-3afc-4fc6-866c-864ebdb74e55](https://user-images.githubusercontent.com/59854960/122492510-d968ff80-d020-11eb-910e-faaa74f67a28.png)

아무것도 누르지 않았을 때 기본 실행되는 모습

파란색 선은 Path Planning 알고리즘을 통해 만든 AR 태그로 까지의 경로 추정이다.

stanley 

