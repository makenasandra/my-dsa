import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    w = list(w)
    i = len(w) -1

    while i>0 and w[i-1] >= w[i]:
        print(f'{w[i-1]} is >= {w[i]}')
        i -= 1
    print('Value of i:',i)

    if i <= 0:
        print('no answer')
        return

    # Find the rightmost successor to pivot in the suffix
    j = len(w) - 1
    while w[j] <= w[i - 1]:
        print(f'{w[j]} <= {w[i - 1]}')
        j -= 1
    print('Value of j:', j)

    # Swap the pivot with the rightmost character
    w[i - 1], w[j] = w[j], w[i - 1]
    print(f'Swap {w[j]} with {w[i - 1]}')
    print('new w:',w)

    # Reverse the sufix
    w[i:] = w[len(w) - 1:i - 1:-1]
    print('final w:',w)

    print(''.join(w))




if __name__ == '__main__':
    w = 'abdc'
    biggerIsGreater(w)