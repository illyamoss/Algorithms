arr = [1,3,5,4,2]
print(arr)

def sort(arr):
	count = len(arr)

	for q in range(count-1):
	    for j in range(count-q-1):
	        if arr[j] > arr[j+1]:
	            arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(sort(arr))