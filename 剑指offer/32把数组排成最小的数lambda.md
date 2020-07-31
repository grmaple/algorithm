### 32把数组排成最小的数

##### 题目

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

##### 解法

先将整型数组转换成String数组，然后将String数组排序，最后将排好序的字符串数组拼接出来。关键就是制定排序规则。

通过sort函数排序，但是不是通过int类型比较大小，而是重写一个函数cmp，通过字符串来比较大小

```C++
class Solution {
public:
    static bool cmp(int a, int b)
    {
        string as = to_string(a), bs = to_string(b);
        return as + bs < bs + as;
    }
    string PrintMinNumber(vector<int> nums) {
        sort(nums.begin(), nums.end(), cmp);
        //sort(nums.begin(),nums.end(),[](const int& a,const int& b){return to_string(a)+to_string(b) < to_string(b)+to_string(a);});
        string res;
        for(auto x :nums) res += to_string(x);
        //for(int i=0;i<nums.size();i++) res += to_string(nums[i]);
        return res;
    }
};
```

##### for (auto x : nums)

作用就是迭代容器中所有的元素，每一个元素的临时名字就是x，等同于下边代码

for (vector<int>::iterator iter = nums.begin(); iter != nums.end(); iter++)

##### C++的lambda

- [ ] > **[capture] (param) opt->ret{body;};**
  > [] 为捕获对象，可以是外部变量，指针，引用等
  > () 为参数列表
  > opt 函数选项，如mutable等
  > ret 返回类型，可以不写，由编译器自动推导
  > {} 函数体

lambda的优点是：可以编写内嵌的匿名函数，而不必编写独立函数或函数对象，使得代码更加的容易理解和精简。

原本

```C++
bool compare(int& a,int& b)
{
    return a>b;
}
sort(a, a+n, compare);
```

现在

```C++
sort(a, a+n, [](int a,int b){return a>b;});//降序排序
```

由于Lambda的类型是单一的，不能通过类型名来显式声明对应的对象，但可以利用auto关键字和类型推导：

```C++
auto f=[](int a,int b){return a>b;};
```

python版本

```python
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
		if not numbers: return ""
        #map(str, numbers)其实就是对numbers内的元素按照str()函数进行迭代。将int的列表，转化为str的列表
        numbers = list(map(str, numbers))
        numbers.sort(cmp=lambda x, y: cmp(x + y, y + x))
        #lstrip()方法用于截掉字符串左边的空格或指定字符。
        return "".join(numbers).lstrip('0') or'0'
```

##### python的lambda

**lambda 形参列表 : 函数返回值表达式语句**

```python
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=lambda x:x["age"])
```

过去需要这样

```python
def comp(x):
    return x["age"]
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=comp)
```

