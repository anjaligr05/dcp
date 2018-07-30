def mulAllButThis(lst):
	print "ip, ", lst
	p = 1
	q = 1
	retL = [1]*len(lst)
	for i in range(len(lst)):
		retL[i] *= p
		retL[len(lst)-1-i] *=q
		p = p*lst[i]
		q = q*lst[len(lst)-1-i]
	return retL	
print mulAllButThis([3,2,1])
print mulAllButThis([4,5,7,1])
