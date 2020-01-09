斐波那契数列  
=====
- [模板来源--点击查看原文](https://www.cnblogs.com/panlq/p/9307203.html)


## 第一种: 递 推  
优点:  
> 1、运行时间: O(n)
> ![fib-1](https://github.com/KissMyLady/Tools/blob/master/algorithem/image/fib-1.jpg)  
>> 递推法，就是递增法，时间复杂度是 O(n)，呈线性增长，如果数据量巨大，速度会越拖越慢    

```Python
a, b = 0, 1
N = int(input('请输入要计算的斐波那契数列的第n项'))
print('您输入的数字是%s' % N)

NUM = 1
Fib = list()
max_num = int(N) + 1

print('第1项是: 0')
while NUM < Max_num:
    Fib.append(a)
    a, b = b, a + b
    print('第%s项是:'%(NUM+1), a)
    NUM += 1
    if NUM == N:
        print('斐波那契数列的第n(%s)项是: '%(N), a)
```



## 第二种: 递 归  
![fib-2](https://github.com/KissMyLady/Tools/blob/master/algorithem/image/fib-2.jpg)  
```Python  
def fib_recur(n):
  assert n >= 0, "n > 0"
  if n <= 1:
    return n
  return fib_recur(n-1) + fib_recur(n-2)

for i in range(1, 20):
    print('第%s项是: '% i,fib_recur(i))
```
优点:  
> 1、写法最简洁    

缺点:  
> 1、效率最低，会出现大量的重复计算O(1.618^n), 而且最深度1000</br>      
解除递归深度方法:      
```Python
import sys
sys.setrecursionlimit(10000)
```

## 第三种 生成器
```Python 
def fib_loop_while(max):
    a, b = 0, 1
    while max > 0:
        a, b = b, a + b
        max -= 1
        yield a

for i in fib_loop_while(10):
    print(i)  
```

> 带有yield的函数都被看成生成器，生成器是可迭代对象  
> 且具备__iter__ 和 __next__方法， 可以遍历获取元素  
>> python要求迭代器本身也是可迭代的  
>> 所以我们还要为迭代器实现__iter__方法    
>>> 而__iter__方法要返回一个迭代器迭代器自身正是一个迭代器，所以迭代器的__iter__方法返回自身即可  




## 第四种: class    
- [Python核心编程--迭代器讲解](#)  

```Python 
class Fibonacci(object):
    """迭代器"""
    def __init__(self, n):
        self.n = n 
        self.current = 0   # 保存当前记录位置
        self.a = 0 
        self.b = 1 

    def __next__(self):   
        if self.current < self.n: 
            self.a, self.b = self.b, self.a + self.b 
            self.current += 1 
            return self.a 
        else: 
            raise StopIteration 

    def __iter__(self):  
        return self  


if __name__ == '__main__':
    fib = Fibonacci(15)
    for num in fib:
        print(num)
```



## 第五种: 矩 阵  
![juzhen](https://github.com/KissMyLady/Tools/blob/master/algorithem/image/juzhen.jpg)  
```Python  
import numpy as np

def fib_matrix(n):
    for i in range(n):
        res = pow((np.matrix([[1, 1], [1, 0]], dtype='int64')), i) * np.matrix([[1], [0]])
        print(int(res[0][0]))

fib_matrix(50)


# 使用矩阵
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

# 调用
Fibonacci_Matrix(50)
```
优 点:  
> pow速度比双**号快, np.linalg.matrix_power也是一种方法  
> 因为幂运算可以使用二分加速，所以矩阵法的时间复杂度为 O(log n)  
> 用科学计算包numpy来实现矩阵法 O(log n)  


