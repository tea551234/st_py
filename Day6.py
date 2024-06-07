#operator number

a=7 
b=5
# #a,b轉成二進位
# print( "這是A的二進制                  :"+ bin(a))
# print( "這是B的二進制                  :"+ bin(b))

# print( "這是A向左位移2位元             : " + bin(a<<2))
# print( "這是A向右位移2位元             : " + bin(a>>2))
# print( "二進位數字「完全相同」的部分   : " + str(a&b)) 
# print( "二進位數字「只要有一個為 1 」  : " + str(a|b)) 

# 內建計算
# a=-3
print(abs(a)) #絕對值
print(pow(a,2)) #次方
print(divmod(a,b)) #商數餘數 回傳tuple
print(max("12132132139z ")) # 讀承ASCII 並回傳最大值
c = complex(1,2) #複數
print(c.real) #實部
print(c.imag) #虛部