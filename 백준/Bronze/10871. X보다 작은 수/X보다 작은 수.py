import sys
input = sys.stdin.readline

N, X = map(int, input().split())
A = list(map(int, input().split()))

answer = list(filter(lambda n: n < X, A))

for i in range(len(answer)):
    print(answer[i], end=" ")
    