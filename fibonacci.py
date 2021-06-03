def finonacci(n):
	if n <= 1:
		return n
	return finonacci(n-1) + fibonacci(n-2)
	print(finonacci(30))
    
#O (2^n) - quadrática