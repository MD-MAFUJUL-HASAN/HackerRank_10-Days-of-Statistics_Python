#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from statistics import median


def quartiles(n, arr):
    # Write your code here
    a = int(median(arr[:n//2]))
    b = int(median(arr))
    c = int(median(arr[(n+1)//2:]))
    return a, b, c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = sorted(map(int, input().rstrip().split()))

    res = quartiles(n, data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
