# a= 1
# print(a)

# ================

# a,b,c = 1,2,3
# print(a,b,c)

# ================

# a=1111
# b=2222
# a,b=b,a
# print(a,b)

# ================
# append為修改 固賦予的b也會受到影響,而c為直接指定值,不會影響到d

# a = []
# b=a
# c=[]
# d=c

# a.append(1)
# print(f"A:{a} & B:{b} 使用append修改會影響到b")
# c=[1]
# print(f"C:{c} & D:{d} 直接指定值不會影響到d")

# ================
# 而透過function也是直接修改值,固後續全域變數也會受到影響
# 而C是透過宣告賦值,所以變成區域變數

# a = []
# b=a
# c=[]
# d=c

# def f1():
#     global c
#     a.append(1)
#     c=[1]
#     print(f"def1 A:{a}")
#     print(f"def1 B:{b}")
#     print(f"def1 C:{c}")
#     print(f"def1 D:{d}")

# def f2():
#     print(f"def2 A:{a}")
#     print(f"def2 B:{b}")
#     print(f"def2 C:{c}")
#     print(f"def2 D:{d}")

# f1()
# f2()

# ================
a=1
def hello():
    a=2
    print(locals())
    print(globals()) 
hello()
print(a)

# ================