## vector

### **vector初始化：**

vector<int> vec;        //声明一个int型向量
vector<int> vec(5);     //声明一个初始大小为5的int向量
vector<int> vec(10, 1); //声明一个初始大小为10且值都是1的向量

vector<int> tmp;
vector<int> vec(tmp);   //声明并用tmp向量初始化vec向量

vector<int> tmp(vec.begin(), vec.begin() + 3);  //用向量vec的第0个到第2个值初始化tmp

### **vector常见操作：**

##### **1.增加函数**

push_back 在数组的最后添加一个数据

insert 增加

##### **2.删除函数**

pop_back 去掉数组的最后一个数据

clear 清空当前的vector

erase 删除

*erase 只能清除vector里面的数据，但是内存空间没有释放，如果要释放内存空间，使用arr.swap(vector ());*

##### **3.遍历函数**

at 得到编号位置的数据

front 得到数组头的引用 (begin、end返回的是指针）

back 得到数组的最后一个单元的引用

begin 返回第一个元素的指针

end 返回最后一个元素的指针

*//使用begin()实现遍历*

```c++
vector<int> arr;
for(vector<int>::iterator iter=arr.begin();iter!=arr.end();++iter)
{ cout<<" "<<*iter; }
```

##### **4.判断函数**

empty 判断vector是否为空

##### **5.大小函数**

size 当前使用数据的大小

max_size 最大可允许的vector元素数量值

capacity vector实际能容纳的大小

##### **6.其他函数**

swap 交换

assign 使用括号内的值设置当前的vector

### vector<vector\<int>>

##### **1.定义**

```c++
vector<vector<int> > A;//正确的定义方式
vector<vector<int>> A;//c++11之前这样定义是错误的，c++11之后支持这种定义方式
```

##### **2 插入元素**

若想定义A = [[0,1,2],[3,4]]，有两种方法。

（1）定义vector B分别为[0,1,2]和[3,4]，然后放入vector A。

```c++
vector<vector<int> > A;
 
vector<int> B;
B.push_back(0);
B.push_back(1);
B.push_back(2);
 
A.push_back(B);
 
B.clear();
B.push_back(3);
B.push_back(4);
 
A.push_back(B);
```

 （2）

```c++
vector<vector<int> > A;
for(int i = 0; i < 2; ++i)
    A.push_back(vector<int>());  
A[0].push_back(0);
A[0].push_back(1);
A[0].push_back(2);
A[1].push_back(3);
A[1].push_back(4);
```

##### **3 大小**

```c++
//vector<vector<int> >A中的vector元素的个数
len = A.size();
//vector<vector<int> >A中第i个vector元素的长度
len = A[i].size();
```

**4 访问某元素**

　访问某元素时，方法和二维数组相同，例如：

```c++
printf("%d\n", A[0][0]);//0
printf("%d\n", A[0][1]);//1
printf("%d\n", A[0][2]);//2
printf("%d\n", A[1][0]);//3
printf("%d\n", A[1][1]);//4
```



