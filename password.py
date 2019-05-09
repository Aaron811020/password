#只能輸入三次密碼

password = "a123456"

count = 1
while count < 4:
	count = count +1
	if input("請輸入密碼:") == password :
		print("登入成功")		
		break
	else:
		if 4 - count == 0:
			print("密碼錯誤3次, 請稍後再試")
		else:
			print("密碼錯誤! 還有 %d 次機會" % (4-count))

	