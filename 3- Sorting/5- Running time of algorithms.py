lenght= int(input())
arr= input().split()
shift=0
for i in range(1,len(arr)):
    for j in range(0,i):
        if int(arr[i])<int(arr[j]):
            item= arr.pop(i)
            arr.insert(j,item)
            shift+= i-j
print (shift)