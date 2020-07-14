arr = [1,2,3,4,5,6,7,8,9,10,11,12]


def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

print(binary_search(arr, 6))