#CountingSort
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    arr1=[]
    arr1=[0 for i in range(100)]
    for x in arr:
        arr1[x]=arr1[x]+1

        print(arr1)
        
        
        

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    countingSort(arr)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
