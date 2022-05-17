#今天讓使用者自己決定範圍

import random 
min1 = input('請自行輸入範圍最小值：')
max1 = input('請自行輸入範圍最大值:')
min1 = int(min1)
max1 = int(max1)
r = random.randint(min1, max1)
tr = r
i = 0
while True:
	i += 1 #是i = i + 1的快速寫法
	ans = input('請輸入數字：') #input. print存到左邊都是字串
	ans = int(ans)
	if ans == tr:
		print('正確解答')
		print('這是你第', i, '次猜測')
		break
	elif ans > tr:
		print('比答案大')
	elif ans < tr:
		print('比答案小')
	print('這是你第', i, '次猜測') #可以放在最底下，因為if跟兩個elif是同一個架構的
