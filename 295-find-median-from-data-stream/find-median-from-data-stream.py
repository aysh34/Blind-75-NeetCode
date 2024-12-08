# heaps are implemented using the heapq module. heapq module by default implements a min-heap. Since heapq only supports min-heaps, you can simulate a max-heap by negating the values
import heapq
class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.left_max_heap) == 0 or num < -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap,-num)
        else:
            heapq.heappush(self.right_min_heap,num)

        # max-heap can have at most one more element than min-heap
        if len(self.left_max_heap) > (len(self.right_min_heap)+1):
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        elif len(self.right_min_heap) > len(self.left_max_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

    def findMedian(self) -> float:
        if len(self.right_min_heap) == len(self.left_max_heap): # even 
            med = (self.right_min_heap[0] + (-self.left_max_heap[0])) / 2
            return med
        return -self.left_max_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()