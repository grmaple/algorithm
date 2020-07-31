# -*- coding:utf-8 -*-
class Solution:
    def GetFirstK(self, data, k):
		l = 0
		r = len(data) - 1
		while l < r :
			mid = (l + r) // 2
			if data[mid] < k: 
				l = mid + 1
			elif data[mid] > k:
				r = mid
			else:
				if mid == l or data[mid] != k:
					return mid
				else:
					r = mid
		return -1

    def GetLastK(self, data, k):
        l = 0
		r = len(data) - 1
		while l < r :
			mid = (l + r) // 2
			if data[mid] < k: 
				l = mid
			elif data[mid] > k:
				r = mid - 1
			else:
				if mid == r or data[mid] != k:
					return mid
				else:
					l = mid
		return -1

    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        if self.GetLastK(data, k) == -1 and self.GetFirstK(data, k) == -1:
            return 0
        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1
			
if __name__ == "__main__":
	s = Solution()
	data = [0, 1, 1, 1, 2]
	print(s.GetNumberOfK(data, 1))