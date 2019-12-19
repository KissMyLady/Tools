虚拟机Mac安装教程  
====


## 准备东西:     
> 1、MacOS镜像文件      
> 2、VMware软件(推荐)/或者VirtualBox      
>> 3、VMware二次解锁文件(原VMware里面隐藏Mac安装，需要解锁)
>> 3.5、VirtualBox官网下免费的就可以，不要另外安什么插件    

效果图: 
1、如果使用的是VMware软件，里面有自带的优化功能，Mac最后使用起来会非常流畅，可以和ubuntu媲美了    
![mac-3]()  
2、如果使用的是VirtualBox, 它没有任何优化，所有的GUI都是CPU虚拟出来的，一个字, 卡   

3、建议下载VMware、 当然，你需要一个好资源(网上有很多版本，你可以通过搜索引擎找到)   


## 开始安装前  
说  明:   
> 1、有固态条件的，可以放在固态硬盘     
> 2、虚拟机不用装太多软件，所以留25G左右就足够了     
> 3、开始安装前，把镜像文件备份一次，防安装失败，(可能)导致镜像也没法用  


## 开始安装   
1、打开VMware(VirtualBox)  

2、将镜像文件放入虚拟机，配置      
 
3、完成   


## 进去后，修改分辨率  
在Mac虚拟机里的终端执行下面的命令，执行完之后重启即可  
```Linux
1920*1080分辨率：  
sudo nvram AC20C489-DD86-4E99-992C-B7C742C1DDA9:width=%80%07%00%00  
sudo nvram AC20C489-DD86-4E99-992C-B7C742C1DDA9:height=%38%04%00%00  

3840*2160分辨率：  
sudo nvram AC20C489-DD86-4E99-992C-B7C742C1DDA9:width=%00%0F%00%00  
sudo nvram AC20C489-DD86-4E99-992C-B7C742C1DDA9:height=%70%08%00%00  
```


## VMware说明  
1、VMware是收费软件      
2、你能够进去VMware后， 里面是没有MacOS操作系统安装的选项      
4、需要二次解码，要下一个小工具，然后运行小工具就可以有MacOS选项了          
5、网上有很多资源，自己时间够，找找完全没有问题      


## 关于指导说明    
1、时间不够的，加QQ号：137 3816 972(加速安装，2元红包)    
2、时间够的，  加QQ群: 36877 9008(免费提示你怎么弄)    
3、时间够，怎么找资源?  搜索引擎: '虚拟机装Mac系统',  很多文章教你, 当然本教程也是    
4、为什么收点小钱?  放链接失效快，手动发你又需要消耗一点时间，所以这是一点时间成本  
5、还有这篇文章存在也是需要一点时间写     



## 接下来    
- [学习Computer](https://github.com/KissMyLady/Computer)  
- [学习Django](https://github.com/KissMyLady/Django)    
- [学习思想](https://github.com/KissMyLady/Tools)      
