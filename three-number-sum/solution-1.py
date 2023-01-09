# runtime -> O(n^2)
# space -> O(n)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left  = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                right -= 1
                left += 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1

    return triplets
