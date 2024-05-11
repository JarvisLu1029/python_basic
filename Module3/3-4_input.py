# input() 函數 讓使用者在終端機輸入資料

# 取得使用者輸入的資料
num = input("輸入數字後，按下Enter: ")
num = int(num)

print(type(num))
# print(f'使用者輸入的是: {num}')

# 將使用者輸入強制轉型成 int

if num > 10:
    print(f'數字 {num} 大於 10') 
