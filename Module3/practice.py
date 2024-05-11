# 引入套件
import random 
# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# password = 25
password = random.randrange(1, 100)
print(password)

'''
程式被迴圈卡住 可以用 Ctrl+C 結束
'''

# 1.告訴使用者需要輸入的數字範圍 input()
while True:
    user_input = input('請輸入1~100的數字: ')
    user_input = int(user_input)
# 2.使用者猜對要回傳「恭喜中獎」，並結束整個迴圈的執行
    if user_input == password:
        print('恭喜中奬')
        break
# 3.超出範圍要顯示「超出範圍請重新輸入」
    elif user_input < 0 or user_input > 100:
        print('超出範圍請重新輸入')

# 4.數字太大 要提示「請輸入更小的數字」
    elif user_input > password:
        print('請輸入更小的數字')

# 5.數字太小 要提示「請輸入更大的數字」
    elif user_input < password:
        print('請輸入更大的數字')

