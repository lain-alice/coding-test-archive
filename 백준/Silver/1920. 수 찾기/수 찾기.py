import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
sources = list(map(int, input().split()))
visited = defaultdict(int) # 기본값이 정수인 딕셔너리

for source in sources:
    visited[source] = 1

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(visited[target])