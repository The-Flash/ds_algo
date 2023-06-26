def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        if potentialMatch > target:
           right = middle - 1 
        if potentialMatch < target:
           left = middle + 1 
    return -1
   

if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7, 8]
    array2 = [4, 5, 9, 10, 23, 56, 60]
    searchIn1 = binarySearch(array1, 5)
    searchIn2 = binarySearch(array2, 10)
    print(f"Searching 5 in {array1}")
    print(f"Found at index: {searchIn1}") 
    print(f"Searching 10 in {array2}")
    print(f"Found at index: {searchIn2}")
