class ArraySet:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def __str__(self):
        return str(self.array[0:self.size])

    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
            return True
        return False

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return True
        return False

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def intersect(self, setB):
        setC = ArraySet()
        for i in range(setB.size):
            if self.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC

    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

# Testing the code
setA = ArraySet()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
print('Set A:', setA)

setB = ArraySet()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
print('Set B:', setB)

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
print('Set A:', setA)
print('Set B:', setB)

print('A U B:', setA.union(setB))
print('A ^ B:', setA.intersect(setB))
print('A - B:', setA.difference(setB))
