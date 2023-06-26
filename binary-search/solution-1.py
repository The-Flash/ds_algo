def binarySearch(array, target):
   return binarySearchHelper(array, target, 0, len(array) - 1) 

# 
def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    # get the middle index
    middle = (left + right) // 2
    potentialMatch = array[middle]
    # if the target is equal to the potentialMatch
    # return the middle, ie, the index
    if target == potentialMatch:
        return middle
    # if the target is less than the potentialMatch,
    # search within the first half of the array, ie, the left
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    # if the target is greater than the potentialMatch
    # search within the second half of the array, ie, the right
    elif target > potentialMatch:
        return binarySearchHelper(array, target, middle + 1, right)

if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7, 8]
    array2 = [4, 5, 9, 10, 23, 56, 60]
    searchIn1 = binarySearch(array1, 5)
    searchIn2 = binarySearch(array2, 10)
    print(f"Searching 5 in {array1}")
    print(f"Found at index: {searchIn1}") 
    print(f"Searching 10 in {array2}")
    print(f"Found at index: {searchIn2}")
