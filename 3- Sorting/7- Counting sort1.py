lenght= int(input())
arr= list(map(int,input().split()))
for el in range(0,100):
    times= arr.count(el)
    print (times, end=" ")