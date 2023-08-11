class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]

if __name__ == "__main__":
    minMaxStack = MinMaxStack()
    minMaxStack.push(2)
    minMaxStack.push(5)
    minMaxStack.push(6)
    minMaxStack.push(3)

    print(minMaxStack.stack)
    print("Minimum", minMaxStack.getMin())
    print("Maximum", minMaxStack.getMax())
