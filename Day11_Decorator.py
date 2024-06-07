# import pandas as pd

d = {'a':20}

x1 = d.get('b', 0)
print(x1)

try:
    x2 = d['c']
except KeyError:
    print('KeyError')    

# from rich.console import Console
# from rich.table import Table
# console=Console()
# table = Table(show_header=True, header_style="bold magenta")

# fk_date = pd.DataFrame({"資料一": [23, 3, 23, 55, 6, 20],
#                         "資料二": [1, 2, 3, 4, 5, 6]})
# registry = []
# def register(func):
#     registry.append(func)
#     print(f"Register {func.__name__}")
#     return func

# @register
# def feater_3(data:pd.DataFrame) -> pd.DataFrame:
#     data["資料三"] = data["資料一"] + data["資料二"]
#     return data
# @register
# def feater_4(date:pd.DataFrame) -> pd.DataFrame:
#     date["資料四"] = date["資料一"] * date["資料二"]
#     return date

# feats = fk_date.copy()
# for func in registry:
#     func(feats)
# print(feats)




# #資料三 = 資料一 + 資料二
# def feater_3(data:pd.DataFrame) -> pd.DataFrame:
#     data["資料三"] = data["資料一"] + data["資料二"]
#     return data

# def feater_4(date:pd.DataFrame) -> pd.DataFrame:
#     date["資料四"] = date["資料一"] * date["資料二"]
#     return date

# feats=fk_date.copy()

# for gen_fun in [feater_3,feater_4]:
#     gen_fun(feats)

# print(feats)

#舊有函數
# def orignal_functions():
#     print("This is the orignal function") 
#     return 1 
# #建立裝飾器
# def decorator_function(func):
#     def plus_2():
#         print("修飾器啟用")
#         return func() + 2 
#     return plus_2
# d = decorator_function(orignal_functions)()
# print(d)

# 語法糖    

# def decorator_function(func):
#     def plus_2():
#         print("修飾器啟用")
#         return func() + 2 
#     return plus_2

# @decorator_function #使用語法糖,將原先的orignal_functions()函數透過decorator_function()進行修飾
# def orignal_functions():
#     print("This is the orignal function")
#     return 1 

# print(orignal_functions())