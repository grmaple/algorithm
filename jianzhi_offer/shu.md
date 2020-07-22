## 树

### 树的构造

```python
class TreeNone(object):
	def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
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
    
```



### 树的遍历

1.深度优先遍历

先遍历

```python
def preOrderRecusive(root):
    #递归先写出口
    if root == None:
        return None
    print(root.val)
    preOrderRecusive(root.left)
    preOrderRecusive(root.right)     
```

递归可以转换成非递归，使用栈结构

```python
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
```

中根遍历

```python
def midOrderRecusive(root):
    if root == None:
        return None
    midOrderRecusive(root.left)
    print(root.val)
    midOrderRecusive(root.right)
```

```python
def midOrder(root):
    if root == None:
        return None
    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        print(node.val)
        tmpNode = node.right
```

后根遍历

```python
def lastOrderRecusive(root):
    if root == None:
        return None
    lastOrderRecusive(root.left)
    lastOrderRecusive(root.right)
    print(root.val)
```

```python
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
```

2.深度优先遍历