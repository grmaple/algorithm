class TreeNode(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

def Breadth_First_Search(root):
	# write code here
	if root == None:
		return []
	support = [root]
	ret = []
	while support:
		tmpNode = support[0]
		ret.append(tmpNode.val)
		if tmpNode.left:
			support.append(tmpNode.left)
		if tmpNode.right:
			support.append(tmpNode.right)
		del support[0]

	return ret
if __name__ == '__main__':
	t1 = TreeNode(1)
	t2 = TreeNode(2)
	t3 = TreeNode(3)
	t4 = TreeNode(4)
	t5 = TreeNode(5)
	t6 = TreeNode(6)
	t7 = TreeNode(7)
	t8 = TreeNode(8)
	
	t1.left = t2
	t1.right = t3
	t2.left = t4
	t2.right = t5
	t3.left = t6
	t3.right = t7
	t6.right = t8
	#lastOrderRecusive(t1)
	#preOrder(t1)
	ret = Breadth_First_Search(t1)
	print(ret)