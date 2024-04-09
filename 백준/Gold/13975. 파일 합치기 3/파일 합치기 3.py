import sys
from heapq import *

input = sys.stdin.readline

t = int(input())
chapters = []

# 두개씩 두개씩 더해서 끝까지...
# 최소 비용이 되려면? 최소, 2번째로 작은거 합친다
# 우선순위 큐, 힙

for _ in range(t):
    k = int(input())
    chapters = list(map(int, input().split()))
    heapify(chapters)
    # sort랑 같은 건가?

    novel = 0

    while len(chapters) > 1:
        temp = 0
        a = heappop(chapters)
        b = heappop(chapters)
        # 최소 뽑고 2번째 뽑기

        temp += a + b
        # 챕터 2개씩 합친 임시파일

        novel += temp
        heappush(chapters, temp)

    print(novel)
