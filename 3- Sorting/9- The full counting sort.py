lenght= int(input())
arr=[]
lst=[]
for i in range(lenght):
    lst= input().split()
    if i<lenght//2:
        lst[1]= "-"
    lst.append(i)
    arr.append(lst)
arr.sort(key=lambda x: (int(x[0]), x[2]))
for el in arr:
    print (el[1], end=" ")