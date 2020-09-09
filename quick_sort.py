def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    mini_items = []
    identical_items = []
    big_items = []

    arr1 = arr[0]
    for item in arr:
        if item < arr1:
            mini_items.append(item) 
        elif item > arr1:
            big_items.append(item)
        else:
            identical_items.append(item)

    return quick_sort(mini_items) + identical_items + quick_sort(big_items)


arr = [a for a in range(899)]

print(quick_sort(arr[::-1]))
