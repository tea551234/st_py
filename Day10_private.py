from rich import traceback ,inspect
from rich.console import Console 
traceback.install(show_locals=True)

console = Console()
class A :
    def __init__(self):
        self.__v=0
    def test():
        print("Testing")
O=A()

print(O.__v)
# Pyhton 實現私有變量的方式是透過修改變量名稱
# 透過反編譯可以發現私有變量的名稱變成了 _類名__變量名故還是可以透過下列指令輸出
# a=['key', 'value']
# inspect(A,methods=True)