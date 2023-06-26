# This solution has been generalized to n number of largest numbers
def findThreeLargestNumbers(array: list[int], n = 3):
    threeLargest = [None] * n
    for num in array:
        updateLarget(threeLargest, num, n)
    return threeLargest

def updateLarget(threeLargest, num, n = 3):
    for i in range(n - 1, 0 - 1, -1):
        if threeLargest[i] is None or num > threeLargest[i]:
            shiftAndUpdate(threeLargest, num, i)
            break 


def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]

if __name__ == "__main__":
    array = [2, 3, 4, 5, 7, 8, 1, 23, 67, 22]
    largest = findThreeLargestNumbers(array, len(array))
    print(largest)
