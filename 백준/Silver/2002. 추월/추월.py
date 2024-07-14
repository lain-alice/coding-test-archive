import sys
input = sys.stdin.readline

n = int(input())
in_cars = {} # 입구 들어온 차 딕셔너리
out_cars = {} # 출구 나간 차

# 들어온차 나온차 상대적인 위치 차이 따지기 위해 각 위치에 번호 부여

for i in range(n):
    car = input()
    in_cars[car] = i

for i in range(n):
    car = input()
    out_cars[car] = i

count = 0
# 추월한 자동차 수
out_keys = list(out_cars.keys()) # 나온 차 순서

for i in range(0, len(out_keys)-1):
    now_in = in_cars[out_keys[i]] 
    for j in range(i+1, len(out_keys)):
        next_in = in_cars[out_keys[j]]
        if next_in < now_in:
            count += 1
            break
            
# 들어온 차 순서가 나온 차 순서보다 빠르면 추월한 것

print(count)

