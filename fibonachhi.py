from functools import cache
@cache


def fibonachhi(n):
 if n == 0:
   return 0
 if n == 1:
   return 1
 return fibonachhi(n-1) + fibonachhi(n-2)

if __name__ == '__main__':
 print(fibonachhi(30))
