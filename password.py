#只能輸入三次密碼

password = "a123456"

count = 0
while True:
	count = count +1
	if input("請輸入密碼:") == password :
		print("登入成功")		
		break
	else:
		if 3 - count == 0:
			print("密碼錯誤3次, 請稍後再試")
			break
		else:
			print("密碼錯誤! 還有 %d 次機會" % (3-count))

	