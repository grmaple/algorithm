## Python 直接赋值、浅拷贝和深度拷贝解析

- **直接赋值：**其实就是对象的引用（别名）。

  b = a

- **浅拷贝(copy)：**拷贝父对象，不会拷贝对象的内部的子对象。

  b = a.copy()

  或者

  import copy

  b = copy.copy(a)

  或者

  b =a[:]

- **深拷贝(deepcopy)：** copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。

  import copy

  b = copy.deepcopy(a)

  ### 解析

  1、**b = a:** 赋值引用，a 和 b 都指向同一个对象。

  ![img](https://www.runoob.com/wp-content/uploads/2017/03/1489720931-7116-4AQC6.png)

  **2、b = a.copy():** 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。

  ![img](https://www.runoob.com/wp-content/uploads/2017/03/1489720930-6827-Vtk4m.png)

  **b = copy.deepcopy(a):** 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。

  ![img](https://www.runoob.com/wp-content/uploads/2017/03/1489720930-5882-BO4qO.png)

![img](https://upload-images.jianshu.io/upload_images/13253432-4eae0bbcf9d34ae3?imageMogr2/auto-orient/strip|imageView2/2/w/620/format/webp)



### 结论

**赋值和拷贝不一样**

赋值和原数据指向同一对象，改变会使原数据一起改变

拷贝和原数据指向不同对象，改变不会使原数据一起改变

当第一层数据为基本数据类型时，浅拷贝和深拷贝是一样的

**浅拷贝和深拷贝不一样**

如果原数据中包含子对象，则浅拷贝和深拷贝不一样

浅拷贝的子对象指向同一对象，改变会使原数据的子对象一起改变

深拷贝的子对象不是同一对象，改变不会使原数据的子对象一起改变



### 标准数据类型

Python3 中有六个标准的数据类型：

- Number（数字）

  包括 int、float、bool、complex（复数）

- String（字符串）

  a = '1'

  用单引号 **'** 或双引号 **"** 括起来，同时使用反斜杠 \\ 转义特殊字符。

  字符串不能被改变

- List（列表）

  a=[],a=[1]

  列表中元素的类型可以不相同

  列表是有序的对象集合

- Tuple（元组）

  a=(),a=(1,)

  与列表类似，不同之处在于元组的元素不能修改。

- Set（集合）

  a=set(),a={1}

  由一个或数个形态各异的大小整体组成

- Dictionary（字典）

  a={},a={1:'one'}

  字典是无序的对象集合

  字典当中的元素是通过键来存取的

  键(key)必须使用不可变类型。

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。