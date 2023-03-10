#Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Sample Input
# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

# Sample Output
# 0.500000
# 0.333333
# 0.166667

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    n=len(arr)
    for x in arr:
        if x > 0:
            pos=pos+1
        elif x < 0:
            neg=neg+1
        else:
            zer=zer+1
    
    pav=pos/n
    nav=neg/n
    zav=zer/n
    print("{:.6f}".format(pav));
    print("{:.6f}".format(nav));
    print("{:.6f}".format(zav));