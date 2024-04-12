import sys
input = sys.stdin.readline

N, K = map(int,input().split())
h = list(map(int,input().split()))

array = []

for i in range(1,N):
    array.append(h[i] - h[i - 1])

array.sort(reverse=True)
print(sum(array[K-1:]))

# 각 애들 사이사이 차이…
# 제일큰애 작은애 차이랑 똑같다
# 3 4 5 사이사이 1씩 차이 = 5 - 3