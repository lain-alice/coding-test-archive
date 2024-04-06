import sys
input = sys.stdin.readline

word = input().rstrip()
index = int(input())

print(word[index - 1])