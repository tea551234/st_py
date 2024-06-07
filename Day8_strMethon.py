# str 方法
## strip 可以去除開頭與結尾字元
# a='   !hi!!'
# print(a)
# print(a.strip())
# print(a.strip('!')) # 去除開頭與結尾的!
# print(a.lstrip('!')) # 去除開頭的!
# print(a.rstrip('!')) # 去除結尾的!

## count 計算字串出現次數 str.count(sub, start, end)
a='oooxxoxoo'
print(a.count('o')) #
print(a.count('o',3,len(a)-1)) #

# 使用ord & chr 可以將字元轉換成ASCII碼

print(ord('a')) # 輸出a的ASCII碼
print(chr(97)) # 輸出ASCII 97的字元 a