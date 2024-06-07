# input & output
## print 
# print(1,2,3)
# print("空白已被取代", 1,3,4,sep='&&') #使用sep參數使用時會取代原本的空白的分隔符號 同 linux 的 awk -F"&&"
# print(1,3,4,sep='&&',end='!!') #使用end參數可以取代原本的換行符號
# print(" 換行已被取代AAAAAAA")

## sleep loading... ##
# input
import time 
n = int(input("請輸入倒數秒數 :"))
print("Loading",end='')
for i in range(n+1):
    #flush=True 可以讓print()先行執行後續的程式碼
    #\r 可以讓print()覆蓋前一行的字元
    print(f'\r倒數{n-i}',end='',flush=True) 
    time.sleep(1)
print("time out",end='')
