# Ex-Sherlock and the valid string (medium)
# third page second exercise

# !/bin/python3

import sys


def isValid(s):
    # Complete this function
    sets= set(s)
    countel=[]
    isvalid= "YES"
    j=0
    for el in sets:
        countel.append(s.count(el))
    for i in range(len(countel)-1):
        if countel[i]!=countel[i+1]: #if every element is repeated tot times all the element in countel are equal, and the string "is valid" and we don't have to remove any element
            isvalid= "NO"
            if j<1: #We can do only one change, so at the end of this condition we add 1 to j, and we cannot do any more change.
                if abs(countel[i]-countel[i+1])==1 or countel[i]==1 and countel[i-1]!=1 or countel[i+1]==1 and countel[i]!=1:
                    #There are three particular case in which we can do the change.
                    # 1- If the next element differ from the previous by one (if it differ by more than one, we should remove more than one letter from the initial string. so it should be "not valid"
                    # 2- If an element appears in the string only one time, we can remove that letter to make the string valid, but only if the other elements appear more times. (and viceversa for the next element)
                    if countel.count(countel[i])>countel.count(countel[i+1]): #we substitute the element which is equal to the other elements in count, so that one which is repeated more times in countel
                        countel[i+1]=countel[i]
                        isvalid= "YES"
                    elif countel.count(countel[i])<countel.count(countel[i+1]):
                        countel[i]=countel[i+1]
                        isvalid= "YES"
                    else:
                        isvalid= "NO" #In the case in which the elements in countel appear same times (i.e. [1,1,2,2]), the strng is "not valid" because we should remove more than one element
                j+=1
    return isvalid

s = input().strip()
result = isValid(s)
print(result)