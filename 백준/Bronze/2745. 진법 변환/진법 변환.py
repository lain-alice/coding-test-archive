import sys
input = sys.stdin.readline().strip()

N, B = input.split(' ')
B = int(B)

decimal = int(N, B)

print(decimal)