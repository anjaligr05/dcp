def willSumUp(lst, k):
	print lst, ", ", k
	mapL = {}
	for i in range(len(lst)):
		mapL[lst[i]] = mapL.get(lst[i],0) + 1
	for i in range(len(lst)):
		if k - lst[i] in mapL:
			if lst[i] == k - lst[i]:
				if mapL[lst[i]] > 1:
					return True
				else:
					return False
			return True
	return False
print willSumUp([10, 5,3], 8)
print willSumUp([5,3,2,4], 6)
print willSumUp([5,3,3,2], 6)
		
