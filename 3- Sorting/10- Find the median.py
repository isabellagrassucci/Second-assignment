def quicksort(lista):
    less=[]
    equal=[]
    greater=[]
    if len(lista)>1:
        pivot=lista[0]
        for x in lista:
            if x<pivot:
                less.append(x)
            if x==pivot:
                equal.append(x)
            if x>pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)
    else:
        return lista

lenght=int(input())
arr=list(map(int,input().split()))
sortedarr= quicksort(arr)

pos= round((lenght-1)/2)
print (sortedarr[pos])