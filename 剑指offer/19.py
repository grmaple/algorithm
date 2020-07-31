# -*- coding:utf-8 -*-
class Solution:
	# matrix类型为二维列表，需要返回列表
	def printMatrix(self, matrix):
		# write code here
		ret = []
		if not matrix or not matrix[0]:
			return ret
		n = len(matrix)
		m = len(matrix[0])
		state = [[0 for i in range(m)] for j in range(n)]
		dx = [-1, 0, 1, 0]
		dy = [0, 1, 0, -1]
		x = 0
		y = 0
		d = 1
		Len = n*m
		for i in range(Len):
			ret.append(matrix[x][y])
			state[x][y] = 1
			a = x + dx[d]
			b = y + dy[d]
			if(a < 0 or a >= n or b < 0 or b >= m or state[a][b]) == 1:
				d = (d + 1) % 4
				a = x + dx[d]
				b = y + dy[d]
			x = a
			y = b
		return ret
if __name__ == "__main__":
	s = Solution()
	matrix = [[i for i in range(5)] for j in range(5)]
	print(s.printMatrix(matrix))