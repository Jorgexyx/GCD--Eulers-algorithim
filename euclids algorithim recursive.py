def EuclidAlgorithim(m,n):
	print("(",m, " , ",n ,")")
	if (n == 0):
		return m
	return EuclidAlgorithim(n,m % n)

print(EuclidAlgorithim(31415,14142))