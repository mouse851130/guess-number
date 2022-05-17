import random 
r = random.randint(1, 100)

tr = r
while True:
	ans = input('請輸入數字：')
	ans = int(ans)
	if ans == tr:
		print('正確解答')
		break
	elif ans > tr:
		print('比答案大')
	elif ans < tr:
		print('比答案小')
