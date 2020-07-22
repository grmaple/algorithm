class TreeNone(object):
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
def lastOrderRecusive(root):
        tmpNone = root
        if tmpNone == None:
                return None
        lastOrderRecusive(tmpNone.left)
        lastOrderRecusive(tmpNone.right)
        print(tmpNone.val)
def lastOrder(root):
        if root == None:
                return None
        stack = []
        tmpNode = root
        while tmpNode or stack:
                while tmpNode:
                        stack.append(tmpNode)
                        tmpNode = tmpNode.left
                node = stack[-1]
                tmpNode = node.right
                if node.right == None:
                        node = stack.pop()
                        print(node.val)
                        while stack and node == stack[-1].right:
                                node = stack.pop()
                                print(node.val)

def preOrder(root):
        if root == None:
                return None
        stack = []
        tmpNode = root
        while tmpNode or stack:
                while tmpNode:
                        print(tmpNode.val)
                        stack.append(tmpNode)
                        tmpNode = tmpNode.left
                node = stack.pop()
                tmpNode = node.right
if __name__ == '__main__':
	t1 = TreeNone(1)
	t2 = TreeNone(2)
	t3 = TreeNone(3)
	t4 = TreeNone(4)
	t5 = TreeNone(5)
	t6 = TreeNone(6)
	t7 = TreeNone(7)
	t8 = TreeNone(8)
	
	t1.left = t2
	t1.right = t3
	t2.left = t4
	t2.right = t5
	t3.left = t6
	t3.right = t7
	t6.right = t8
	tmpNone = None
	#lastOrderRecusive(t1)
	#preOrder(t1)
	lastOrder(t1)
