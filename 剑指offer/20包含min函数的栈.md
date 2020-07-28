### 20包含min函数的栈

##### 题目

在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

##### 解法

如果只有一个栈，则时间O(n)额外空间O(1)

想要时间O(1)就要额外空间O(n)，即增加一个栈

增加一个同步栈minV，记录当前最小值

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack=[]
        self.minV=[]
        
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minV:
            #当前值比输入的大，就把输入的放进minV
            if self.minV[-1]>node:
                self.minV.append(node)
            #当前值比输入的小，就把当前值再次放进minV
            else:
                self.minV.append(self.minV[-1])
        #初始化
        else:
            self.minV.append(node)
    def pop(self):
        # write code here
        if self.stack==[]:
            return None
        self.minV.pop()
        return self.stack.pop()
    
    def top(self):
        # write code here
        if self.stack==[]:
            return None
        return self.stack[-1]
    def min(self):
        # write code here
        if self.minV==[]:
            return None
        return self.minV[-1]
```

更巧妙的方法

stack不存入栈元素，而是存储入栈元素与最小值的差值

top\_记录最后一个插入的数

min\_记录最小值

通过stack和min\_来反推入栈元素

时间O(1)空间O(1)

然而却有一个致命的不足

value-min\_的差值可能会发生溢出，比如一个是INT_MAX另一个是INT_MIN，

```python
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.top_ = None
        self.min_ = None
    def push(self, node):
        # write code here
        if self.stack == []:
            self.min_ = node
        self.stack.append(node - self.min_)
        if node < self.min_:
            self.min_ = node
        self.top_ = node

    def pop(self):
        # write code here
        if self.stack:
            if self.stack[-1] < 0:
                self.min_ -= self.stack[-1]
            self.stack.pop()
            if self.stack != []:
                self.top_ = self.min_ + self.stack[-1]

    def top(self):
        return self.top_
    def min(self):
        return self.min_
```

C++版本

```c++
class Solution {
    stack<int> stack_;
    int top_, min_;
public:
    void push(int value) {
        if (stack_.empty()) // 第一次入栈需要额外考虑
            min_ = value;
 
        stack_.push(value - min_); // 存储入栈元素与最小值的差值
        if (value < min_) // 如果入栈元素比最小值要小则更新最小值
            min_ = value;
        top_ = value; //...............更新 top 的值
    }
    void pop() {
        if (!stack_.empty()) {
            // 如果出栈的是最小值(体现为存储值为负)，则需要更新最小值
            if (stack_.top() < 0)
                min_ -= stack_.top();
            stack_.pop();
 
            if (!stack_.empty()) // 出栈需要更新 top 的值
                top_ = min_ + (stack_.top()>0 ? stack_.top() : 0);
        }
    }
    int top() {
        return top_;
    }
    int min() {
        return min_;
    }
};
```

