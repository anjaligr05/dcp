def onepassSeperate(arr):
	i = 0
	j = 0
	k = len(arr)-1
	
	while i<=k:
		if arr[i]=='R':
			arr[i], arr[j] = arr[j], arr[i]
			j+=1
		elif arr[i]=='B':
			arr[i], arr[k]= arr[k], arr[i]
			i-=1
			k-=1
		i+=1
	return arr
			
			
def separateRGB(arr):
	rc = 0
	gc = 0
	bc = 0
	for i in range(len(arr)):
		if arr[i]=='R':
			rc+=1
		elif arr[i]=='G':
			gc+=1
		elif arr[i]=='B':
			bc+=1
	i = 0
	while i<rc:
		arr[i]='R'
		i+=1
	while i<rc+gc:
		arr[i]='G'
		i+=1
	while i<len(arr):
		arr[i]='B'
		i+=1
	return arr
print separateRGB(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
print onepassSeperate(['G', 'B', 'R', 'R', 'B', 'R', 'G'])
