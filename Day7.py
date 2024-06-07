#string
# a='abc\n123'
# b=r'abc\n123' #\r不會轉譯特殊字元

# print(a)
# print(b)

# 轉大小寫

# txt="abc"
# TXT="ABC"
# TxT="AbC"
# print(txt.title()+"字首轉大寫")
# print(txt.upper()+"全部轉大寫")
# print(TXT.lower()+"全部轉小寫")
# print(TXT.swapcase()+"大小寫對調")

#文字格式化
# a="hello {},咖挖{}"
# b=a.format("YO","幫嘎")
# print(b)
## 變更順序
# a="hello {1},咖挖{0}"
# b=a.format("YO","幫嘎")
# print(b)
## 帶入引數
a="hello {m},咖挖{n}"
b=a.format(n="YO",m="幫嘎")
print(b)