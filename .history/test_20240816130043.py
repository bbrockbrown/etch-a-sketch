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
        newArr = [None] * (currLen * 2)
        for i in range(currLen):
            newArr[i] = self.vec[i]
        self.vec = newArr
        self.n += currLen

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return (self.n - self.size)
    
    def print(self):
        for num in self.vec:
            print(num)

  
  
hi = ["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]
ans = [None ,0 ,1 ,None ,1 ,1 ,None ,2 ,2 , 2 ,None , 3, 3, 1, 2]

arr = DynamicArray(1)
assert arr.getSize() == 0
assert arr.getCapacity() == 1
arr.pushback(1)
assert arr.getSize() == 1
assert arr.getCapacity() == 1
arr.pushback(2)
assert arr.getSize() == 2
assert arr.getCapacity() == 2
assert arr.get(1) == 2
arr.set(1, 3)
assert arr.get(1) == 3
assert arr.popback() == 3





