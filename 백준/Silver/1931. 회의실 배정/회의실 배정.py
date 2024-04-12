import sys
input = sys.stdin.readline

n = int(input())
room = []

for _ in range(n):
    meeting = tuple(map(int, input().split()))
    room.append(meeting)

room.sort(key=lambda x: (x[1], x[0]))
# 일찍 끝나는 순서대로 정렬하고
# 첫 회의 끝 시간이 둘째 회의 시작 시간 되도록


time = 0
cnt = 0
for meeting in room:
    if time <= meeting[0]:
        time = meeting[1]
        cnt += 1
        
print(cnt)

# 그리디 알고리즘... 문제를 잘게 쪼개고 그 안에서 최선의 선택?
