# a=['r','g','b']
# print(type(a))
# aa=('r','g','b')
# print(type(aa))
# b=list(aa) # 當 list -> 放入tuple 轉換成串列
# print(b)
# a='r...g...b'
# b=a.split('.')
# print(b)

# 使用+號 & extend() 合併
## 可以使用+號賦予新的變數
a=['a1','a2','a3']
b=['b1','b2','b3']
c=a+b
print(c)
## 使用extend()方法,為改變串列本身,故不會回傳直
a.extend(b)
print(a)
