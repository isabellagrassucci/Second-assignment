lenght= int(input())
arr= input().split()
value= int(arr[-1])
arr.pop()
arr.insert(-1,arr[-1])
string=" ".join(arr)
print (string)
for i in range(1,len(arr)-1)[::-1]:
    arr.pop(i)
    if int(arr[i-1])<value:
        arr.insert(i,str(value))
        string=" ".join(arr)
        print (string)
        break
    else:
        arr.insert(i,arr[i-1])
        string=" ".join(arr)
        print (string)
    if i-1==0 and int(arr[i-1])>value:
        arr.pop(i)
        arr.insert(i-1,str(value))
        string=" ".join(arr)
        print (string)