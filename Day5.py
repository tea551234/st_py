# for/while

## break and continue

# count = 10
# for i in range(count):
#     if i == 5:
#         # continue //跳過該次迴圈
#         break # 跳出迴圈
#     print(i)

##  List comprehension 列表推導式

arr1 = []
for i in range(10):
    if (i+1)%2 == 0:
        arr1.append(i)
print(f"arr.append        : {arr1}") # 一般寫法

#       output   Collection          Condition
arr2 = [ x +1    for x in range(10)  if x%2 == 0 ]
print(f"List comprehension: {arr2}") #