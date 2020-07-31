### 66机器人的运动范围

##### 题目

地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

##### 解法

dfs,搜索四个方向，st记录该方格是否被搜索过，
// 预判方格是否合法，合法就从该方格接着搜索

```c++
class Solution {
public:
    //计算行坐标和列坐标的数位之和
    int get_sum(pair<int, int> q)
    {
        int s = 0;
        while(q.first)
        {
            s += q.first % 10;
            q.first /= 10;
        }
        while(q.second)
        {
            s += q.second % 10;
            q.second /= 10;
        }
        return s;
    }
    //Rows and columns行和列
    int movingCount(int threshold, int rows, int cols)
    {
        int res = 0;
        
        if(!cols || !rows) return 0;
        
        //记录坐标点
        queue<pair<int, int>> q;
        //pair<int, int> t;声明一个包含两个int元素的对组
        //queue<t> q;声明一个包含对组队列
        //记录格子有没有被计算过,没有遍历过为false，遍历过为true
        vector<vector<bool>> st(rows, vector<bool>(cols, false));
        //vector<bool> vi(cols, false);声明一个初始大小为cols且值都是false的向量
        //vector<vector<bool>> st(rows, vi);声明一个初始大小为rows且值都是vi向量的二维向量
        //bfs
        //左，下，右，上
        int dx[4] = {-1, 0, 1, 0},dy[4] = {0, 1, 0, -1};
        //起点入队
        q.push({0,0});
        while(q.size())//访问队中的元素个数
        {
            //取队列的第一个元素
            pair<int, int> t = q.front();//访问队首元素
            
            q.pop();//弹出队列的第一个元素，并不会返回元素的值
            //遍历过的，或者sum>threshold的，就跳过
            if(st[t.first][t.second] || get_sum(t) > threshold) continue;
            //第一次遍历的，并且sum<threshold的，res++
            res++;
            //设置当前结点为已遍历
            st[t.first][t.second] = true;
            //四个方向都加入进来
            for(int i = 0; i < 4; i++)
            {
                int x = t.first + dx[i], y = t.second + dy[i];
                if(x >= 0 && x < rows && y >= 0 && y < cols) q.push({x,y});//入队，将{x,y}元素接到队列的末端
            }
        }
        return res;
    }
};
```

递归做法

判断当前节点是否可达的标准为：

1）当前节点在矩阵内；

2）当前节点未被访问过；

3）当前节点满足limit限制。

```C++
class Solution {
public:
    //计算行坐标和列坐标的数位之和
    int bitSum(int q)
    {
        int s = 0;
        while(q)
        {
            s += q % 10;
            q /= 10;
        }
        return s;
    }

    int movingCount(int threshold, int rows, int cols)
    {
        bool* visited=new bool[rows*cols];
        for(int i=0;i<rows*cols;i++)
            visited[i]=false;
        int count = countingSteps(threshold,rows,cols,0,0,visited);
        delete[] visited;
        return count;
    }
	int countingSteps(int limit,int rows,int cols,int r,int c, bool* visited)
    {
        //终止条件
        if (r < 0 || r >= rows || c < 0 || c >= cols
                || visited[r*cols+c] || bitSum(r) + bitSum(c) > limit)  return 0;
        visited[r*cols+c] = true;
        return countingSteps(limit,rows,cols,r - 1,c,visited)
                + countingSteps(limit,rows,cols,r,c - 1,visited)
                + countingSteps(limit,rows,cols,r + 1,c,visited)
                + countingSteps(limit,rows,cols,r,c + 1,visited)
                + 1;
    }
};
```

python递归

```python

class Solution:
    def __init__(self):
        self.count = 0
 
    def movingCount(self, threshold, rows, cols):
        # write code here
        arr = [[0 for i in range(cols)] for j in range(rows)]
        self.findway(arr, 0, 0, threshold)
        return self.count
 35
    def findway(self, arr, i, j, k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        # 将int类型，按位分开，成int类型的列表
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > k or arr[i][j] == 1:
            return
        arr[i][j] = 1
        self.count += 1
        self.findway(arr, i + 1, j, k)
        #self.findway(arr, i - 1, j, k)
        self.findway(arr, i, j + 1, k)
        #self.findway(arr, i, j - 1, k)

```

i = 35

str1 = str(i) #'35'将int类型转换成str类型

list1 =list(str1）#['3', '5']将str类型转换成list类型，并且将字母分开了。

list(map(int, list1)) #[3, 5]将全部为str的列表，转化为全部为int的列表

总的就是list(map(int, list(str(i))))# 将int类型，按位分开，成int类型的列表

**map()** 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

map(int, list1)其实就是对list1内的元素按照int()函数进行迭代。



