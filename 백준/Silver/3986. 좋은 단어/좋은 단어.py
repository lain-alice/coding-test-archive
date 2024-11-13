import sys
input = sys.stdin.readline

# 선끼리 교차하지 않으면서? A와 B 짝지을 수 있으면
# 괄호랑 반대...?

N = int(input())
answer = 0


for _ in range(N):
    word = list(input().strip())
    stack = []

    # ABBA

    for i in word:
        if not len(stack):
            stack.append(i) # 비어있으면 일단 넣기

        elif stack[-1] == i:
            stack.pop() # 이번 글자랑 마지막으로 들어온 글자 같으면 없앰

        else:
            stack.append(i) # 다르면 계속 넣음

    # ABBA일 때 : A넣기, B넣기, B 넣었는데 두번째 B랑 같아서 없어짐, A 넣었는데 맨처음 A랑 같아서 없어짐

    if not stack:
        answer += 1 # 다 없어지면 좋은 단어, 개수 1 추가

print(answer)





