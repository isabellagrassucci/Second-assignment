lenght= int(input())
arr= input().split()
value= int(arr[0])
left=[]
right=[]
for el in range(1,len(arr)):
    if int(arr[el])<value:
        left.append(arr[el])
    else:
        right.append(arr[el])
left= " ".join(left)
right= " ".join(right)
print (left, str(value), right)