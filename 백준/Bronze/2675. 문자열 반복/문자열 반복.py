import sys
T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()

    for i in S:
        print(i * int(R), end='')
    print()
