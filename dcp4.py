def minPositiveMissing(lst):
	print 'list = ', lst
	if len(lst)<1:
		return 0
	mine = lst[0]
	maxe = lst[0]
	for i in range(1, len(lst)):
		if lst[i] < mine:
			mine = lst[i]
		if lst[i] > maxe:
			maxe = lst[i]
	for i in range(1, maxe+1):
		if i not in lst:
			return i
	return maxe+1
print minPositiveMissing([3, 4.-1,1])
print minPositiveMissing([2,1,0])
print minPositiveMissing([0,6,-1,4])
			
