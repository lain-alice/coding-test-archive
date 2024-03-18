import sys

k = int(sys.stdin.readline())
money_list = list()

for i in range(k):
	money = int(sys.stdin.readline().strip())
	
	if (money == 0):
		money_list.pop()
	else:
		money_list.append(money)
		
print(sum(money_list))
