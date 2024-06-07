
a=1
def h1():
    a=2
    print(locals())  # 如果放置在def外部則效果與globals()相同
    print(globals())
h1()
print(a)

# ================