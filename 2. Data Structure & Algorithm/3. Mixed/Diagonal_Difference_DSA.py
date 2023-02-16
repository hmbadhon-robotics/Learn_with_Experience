import math
import os
import random 
import re
import sys


def diagonalDifference(arr):
    n= len(arr)
    primary_sum = 0
    secondary_sum = 0
    for i in range(n):
        primary_sum += arr[i][i]
        print('pri',primary_sum)
        secondary_sum += arr[i][n-1-i]
        print('sec',secondary_sum)
    return abs(primary_sum - secondary_sum)
    
    
    
    
if __name__ =='__main__':
    n = int(input().strip())                  
    arr =[]
    for _ in range(n):
        arr.append(list(map(int,input().rstrip().split())))
        print(arr)
    result = diagonalDifference(arr)
    print('Final result')
    print(result)