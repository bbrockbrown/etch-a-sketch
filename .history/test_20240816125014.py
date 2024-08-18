class DynamicArray:

    def __init__(self, capacity: int):
        self.vec = [None] * capacity
        self.n = len(self.vec)
        self.size = 0
        self.currIndex = 0

    def get(self, i: int) -> int:
        return self.vec[i]

    def set(self, i: int, n: int) -> None:
        self.vec[i] = n

    def pushback(self, n: int) -> None:
        self.vec[-1] = n
        self.currIndex += 1
        self.size += 1
        if self.currIndex == len(self.vec):
            self.resize()


    def popback(self) -> int:
        self.size -= 1
        return self.vec.pop()

    def resize(self) -> None:
        currLen = len(self.vec)
        newArr = [None] * currLen
        self.vec.append(newArr)
        self.n += currLen

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return (self.n - self.size)
