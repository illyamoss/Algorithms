arr = [1,3,5,4,2]
print(arr)

def sort(arr):
    for q in range(len(arr)-1):
        for j in range(len(arr)-q-1):
	    if arr[j] > arr[j+1]:
	        arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(sort(arr))
