斐波那契数列  
=====

第一种方法--while循环  
=====
优点:  
> 1、速度最快(运行时间: O(n))  
> 2、占用资源最小(必要时，可只储存上一个状态)   
![fib-1](https://github.com/KissMyLady/Tools/blob/master/algorithem/image/fib-1.jpg)

代码:  
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


