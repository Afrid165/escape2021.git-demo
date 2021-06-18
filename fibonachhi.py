from functools import cache
@cache

import numpy

def fibonachhi(n):
`````
Function to calculate fibonachhi series through recursion.

````
 if n == 0:
   return 0
 if n == 1:
   return 1
 return fibonachhi(n-1) + fibonachhi(n-2)

def fib_gen(n):
 for i in range(n):
  yield fibonachhi(i)

if __name__ == '__main__':
 print(fibonachhi(30))
