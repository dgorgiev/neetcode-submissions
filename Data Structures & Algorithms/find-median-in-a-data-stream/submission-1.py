import bisect

class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            return (self.arr[int(n/2) - 1] + self.arr[int(n/2)]) / 2
        else:
            return self.arr[int(n/2)]
        