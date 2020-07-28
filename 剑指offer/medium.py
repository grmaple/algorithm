# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0
    def Insert(self, num):
        # write code here
        if self.minHeapCount < self.maxHeapCount:
            self.minHeapCount += 1
            if num < self.maxHeap[0]:
                tmpNum = self.maxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tmpNum)
            else:
                self.createMinHeap(num)
        else:
            self.maxHeapCount += 1
            if len(self.maxHeap) == 0:
                self.createMaxHeap(num)
            else:
                if self.minHeap[0] < num:
                    tmpNum = self.minHeap[0]
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tmpNum)
                else:
                    self.createMaxHeap(num)
                
    def GetMedian(self):
        # write code here
        if self.minHeapCount < self.maxHeapCount:
            return self.maxHeap[0]
        else:
            return float(self.maxHeap[0] + self.minHeap[0])/2
        
    def createMaxHeap(self, num):
        self.maxHeap.append(num)
        currentIndex = len(self.maxHeap) - 1
        while currentIndex:
                parentIndex = (currentIndex - 1) // 1
                #如果子结点比父节点大，则交换
                if self.maxHeap[parentIndex] < self.maxHeap[currentIndex]:
                    self.maxHeap[parentIndex], self.maxHeap[currentIndex] = self.maxHeap[currentIndex], self.maxHeap[parentIndex]
                    currentIndex = parentIndex
                else:
                    break
    def adjustMaxHeap(self, num):
        if num < self.maxHeap[0]:
            self.maxHeap[0] = num
            maxHeapLen = len(self.maxHeap)
            index = 0
            while index < maxHeapLen:
                leftIndex = index*2+1
                rightIndex = index*2+2
                largerIndex = 0
                #寻找子结点中最大的那个结点
                if rightIndex < maxHeapLen:
                    if self.maxHeap[rightIndex] < self.maxHeap[leftIndex]:
                        largerIndex = leftIndex
                    else:
                        largerIndex = rightIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break
                #如果子结点比父节点大，则交换
                if self.maxHeap[index] < self.maxHeap[largerIndex]:
                    self.maxHeap[index],self.maxHeap[largerIndex] = self.maxHeap[largerIndex],self.maxHeap[index]
                    index = largerIndex
                else:
                    break
                    
    def createMinHeap(self, num):
        self.minHeap.append(num)
        currentIndex = len(self.minHeap) - 1
        while currentIndex:
                parentIndex = (currentIndex - 1) // 1
                #如果子结点比父节点小，则交换
                if self.minHeap[currentIndex] < self.minHeap[parentIndex]:
                    self.minHeap[parentIndex], self.minHeap[currentIndex] = self.minHeap[currentIndex], self.minHeap[parentIndex]
                    currentIndex = parentIndex
                else:
                    break
    def adjustMinHeap(self, num):
        if num < self.minHeap[0]:
            self.minHeap[0] = num
            minHeapLen = len(self.minHeap)
            index = 0
            while index < minHeapLen:
                leftIndex = index*2+1
                rightIndex = index*2+2
                smallerIndex = 0
                #寻找子结点中最小的那个结点
                if rightIndex < minHeapLen:
                    if self.minHeap[leftIndex] < self.minHeap[rightIndex]:
                        smallerIndex = leftIndex
                    else:
                        smallerIndex = rightIndex
                elif leftIndex < minHeapLen:
                    smallerIndex = leftIndex
                else:
                    break
                #如果子结点比父节点小，则交换
                if self.minHeap[smallerIndex] < self.minHeap[index]:
                    self.minHeap[index],self.minHeap[smallerIndex] = self.minHeap[smallerIndex],self.minHeap[index]
                    index = smallerIndex
                else:
                    break
            
if __name__ == '__main__':
	s = Solution()
	for i in [5,2,3,4,1,6,7,0,8]:
		s.Insert(i)
		
	print(s.GetMedian())
	
	
