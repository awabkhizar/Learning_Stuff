#Given an array of integers, where all elements but one occur twice, find the unique element.
a=[1,3,2,4,1,3,2]

ne=0

for i in range(len(a)):
    for x in range(len(a)):
        if a[i]==a[x] and i !=x:
            ne=1
            break 
    if ne == 0:
        print(a[i])
        break
    ne=0        