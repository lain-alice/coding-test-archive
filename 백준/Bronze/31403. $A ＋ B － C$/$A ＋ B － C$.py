import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ab = int(f'{A}{B}')

print(A+B-C)
print(ab-C)