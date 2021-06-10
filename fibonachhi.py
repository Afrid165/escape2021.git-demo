def fibonachhi(n):
	if n == 0:
           return 0
        if n == 1:
           return 1
        return fibonachhi(n-1) + fibonachhi(n-2)

if _name_ == '_main_':
	print(fibonachhi(20))
