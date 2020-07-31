## 34第一个只出现一次的字符

### 题目

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.（从0开始计数）

### 解法

##### c++

```C++
class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        unordered_map<char, int> hash;
        for(auto c : str) hash[c]++;
        for(int i = 0; i < str.size(); ++i){
            if(hash[str[i]]==1)
                return i;
        }
        return -1;
    }
};
```

###### C++的哈希表

map: #include < map >

map内部实现了一个红黑树（红黑树是非严格平衡二叉搜索树，而AVL是严格平衡二叉搜索树），红黑树具有自动排序的功能，因此map内部的所有元素都是**有序**的，红黑树的每一个节点都代表着map的一个元素。因此，对于map进行的查找，删除，添加等一系列的操作都相当于是对红黑树进行的操作。map中的元素是按照二叉搜索树（又名二叉查找树、二叉排序树，特点就是左子树上所有节点的键值都小于根节点的键值，右子树所有节点的键值都大于根节点的键值）存储的，使用中序遍历可将键值按照从小到大遍历出来。

unordered_map: #include < unordered_map >

unordered_map内部实现了一个**哈希表**（也叫散列表，通过把关键码值映射到Hash表中一个位置来访问记录，查找的时间复杂度可达到O(1)，其在海量数据处理中有着广泛应用）。因此，其元素的排列顺序是无序的。

##### python

```python
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        ret = []
        #ret存储的是出现次数为1的字符的下标
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                ret.append[i]
        return ret[0]
		#return [i for i in range(len(s)) if s.count(s[i])==1][0] if s else -1
```

或者使用过滤函数filter()

```python
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        def func(c):
            Count = s.count(c)
            return Count == 1
        #过滤后的结果是出现次数为1的字符
        ret = list(filter(func,s))
        #ret[0]是第一个出现次数为1的字符，index()是取其在s的下标
        idx = s.index(ret[0])
        return idx
        #return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1
    	
```

###### **filter()** 

**filter()** 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。



