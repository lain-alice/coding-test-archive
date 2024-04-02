import sys
input = sys.stdin.readline

n = int(input())
sum_list = [list(map(int, input().split())) for i in range(n)]

all_sum = []
for i in range(n):
    all_sum.append(sum(sum_list[i]))
    print(all_sum[i])

