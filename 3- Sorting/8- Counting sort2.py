lenght=int(input())
arr= list(map(int,input().split()))
times=0
for el in range(100):
    times=arr.count(el)
    for time in range(times):
        print (el, end= " ")