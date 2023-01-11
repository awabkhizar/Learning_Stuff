#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    i=1
    maxs=0
    for x in arr:
        if ( i > 1 ):
            maxs=maxs+x
        i=i+1

    i=1
    mins=0
    for a in arr:
        if ( i < len(arr) ):
            mins=mins+a
        i=i+1

    print(mins, maxs)