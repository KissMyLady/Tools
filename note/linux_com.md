Linux常用命令与配置  
======   

## 文件配置  
![linux-1](https://github.com/KissMyLady/Tools/blob/master/img/linux-1.jpg)  
- [点击进入--Ubuntu安装教程](https://github.com/KissMyLady/Python/blob/master/Nont/Linux/ubuntu_apt_get.md)  

## 删除包的方法    
删除软件及其配置文件   
`apt-get --purge remove <package>`    
删除没用的依赖包  
`apt-get autoremove <package>`  
此时dpkg的列表中有“rc”状态的软件包，可以执行如下命令做最后清理：    
`dpkg -l |grep ^ruby|awk '{print $2}' |sudo xargs dpkg -P`    
### 示例: 删除ruby包   
`apt-get --purge remove ruby`  
`apt-get autoremove ruby`  

## Vim配置与使用  
安装vim  
`shudo apt-get install vim`   
### Vim设置默认就显示行号    
/etc/vim/vimrc 这个是Ubuntu系统范围内的vim默认设置      
编辑的时候需要root权限，如下：    
打开文件后，在一个合适的地方加上set nu     
这样vim 编辑文件，打开默认就显示行号了        

### Vim中如何全选并复制？  
> 全部删除：按esc键后，先按gg（到达顶部），然后dG  
> 全部复制：按esc键后，先按gg，然后ggyG  
> 全选高亮显示：按esc键后，先按gg，然后ggvG或者ggVG    
>   
>> 单行复制：按esc键后, 然后yy 
>> 单行删除：按esc键后, 然后dd   
>> 粘贴：按esc键后, 然后p     
>> 复制到粘贴板: 全选高亮显示之后，ctrl+ shift+ c   

### vim只能粘贴50行的问题：   
> 在当前用户主目录编辑~/.vimrc（如果不存在，新建这个文件），添加一行   
>> :set viminfo='1000,<500   


Vi常用快捷键 
====
模式介绍         
1.一般模式:  
> 以vi打开一个文件就进入一般模式了，该模式可以移动光标，复制，粘贴    
2.编辑模式:   
> 可以编辑文本，界面的左下方或出现插入的字样   
3.命令行模式:   
> 可以提供你查找数据，读取，保存，大量替换字符，离开vi，显示行号    

### 模式转换   
打开文件就进入一般模式，安i，I，O, o, a, A, r, R等任何一个字符就进入编辑模式     
在一般模式下安：或/或？三个按钮中的任一个就进入命令行模式    
按Esc进入一般模式      

### 三. 快捷键     
光标移动，复制粘贴，查找替换      
h，j，k，l         ： 光标左，下，上，右移动一个字符(在键盘一条线上)   
#### ctrl + f     ：屏幕向下移动一页 
#### ctrl + b     ：屏幕向上移动一页  
n+<空格键>         ：n表示数字，光标会向右移动这一行的n个字符。   
0（数字）或home    ：移动到这一行的最前面字符处。   
#### G            ：移动到这个文件的最后一行   
#### 120G          :移到文件的第120行
#### gg           ：移动到文件的第一行  
n+enter          ：光标向下移动n行。   
#### /word       ：向下寻找一个字符串名为word的字符    
#### ？word      ：向上寻找一个字符串名为word的字符   
#### n/N         ：重复前一个查找动作(键入/wordd后, 按Enter, 再按n就可以下一个查找    
：n1，n2s/word1/word2/g    ：在第n1和n2行之间寻找word1字符串，并替换为word2       
：1，s/word1/word2/g：从第一行到最后一行寻找word1字符串，并替换为word2     
：1，s/word1/word2/g：从第一行到最后一行寻找word1字符串，并替换为word2   
：1，s/word1/word2/gc ：从第一行到最后一行寻找word1字符串，并替换为word2.并询问是否替换        
x/X      ：x向后删除一个字符，X向前删除一个字符     
#### dd  ：删除光标所在的一整行     
16dd     ：删除光标所在的向下16行       
#### yy  ：复制光标所在的那一行       
16yy     ：复制光标向下所在的16行     
#### p/P ：小p向下粘贴，大P向上粘贴     
J        ：将光标所行与下一行数据结合成一行   
#### u   ：撤销      
ctrl+r   ：重做上一个操作    
.        ：重复前一个操作    

一般模式切换到编辑模式   
- i/I， i从目前光标处插入，I目前光标所在行第一个非空格符处插入   
- a/A： a目前光标所在的下一个字符插入，A目前光标所在行最后一个字符处插入   
- o/O： o目前光标所在的下一行插入新的一行，O目前光标所在的上一行插入新的一行    

一般模式切换到命令模式     
：w    ：保存     
：q    ：离开, 不保存     
：wq   ：保存后离开    
：w!   ：强制写入   
   
：w+文件名   ：另存为     
：r+文件名   ：在编辑数据中读入另一个文件数据     
：set nu    ：显示行号   
：set nonu  ：取消行号    

 
程序启动    
====
## Ubuntu如何设置使用快捷键启动程序？    
Ubuntu系统下可以设置启动程序的快捷键，这样就不用把程序的快捷方式添加到桌面     
也不用到处找程序的图标，直接使用键盘就可以打开程序了    

以为‘eclipse’添加快捷键为例：
> 首先，打开“系统设置”中的“键盘（Keyboard Shortcuts）”，
> 在其中的“快捷键”中添加新的自定义快捷键。
> 名称随意，比如“eclipse”，命令输入：/home/cx/eclipse/eclipse 
>> 进入/usr/share/applications目录，可以看到这里都是程序的快捷方式，右键-属性，即可看到命令
>> （这个命令就是在终端下启动‘eclipse’运行的那个命令）
>> 
>>> 点击应用之后，就出现了一条新的快捷命令，但还处于“禁用”状态，
>>> 点击“禁用”，会显示为“新建快捷键…”，然后按下你希望用的快捷键，比如 Alt+E。
/usr/share/applications/deepin-terminal

## Ubuntu如何用命令启动程序启动程序？     
```Linux
sudo gedit ~/.bashr       
export PATH=$PATH:/opt/google/chrome   # chrome所在的目录     
```


ps命令  
=====
显示所有当前进程  
> ps -ax   -a代表all, x参数会显示 没有控制终端的进程    
 
根据用户过滤进程   
> ps -u      
> ps -u kissmylady  

通过cpu和内存使用来过滤进程    
> ps -aux    
按照CPU或者内存用量来筛选    
> 1.根据CPU使用来升序排序   
>> ps -aux --sort -pcpu   
> 
> 2.根据内存使用来升序排序     
>> ps -aux --sort -pmem    
>  
> 3、合并，并显示前10个结果：  
>> ps -aux --sort -pcpu, +pmem | head -n 10  

通过进程名和PID过滤     
> ps -C getty  
> ps -f -C getty      -f参数来查看格式化的信息列表  

根据线程来过滤进程  
如果我们想知道特定进程的线程，可以使用-L 参数，后面加上特定的PID   
> ps -L 1213  
  
树形显示进程  
> ps -axjf  或者pstree  
  
显示安全信息  
-e显示所有进程信息，-o参数控制输出。Pid,User和Args参数显示PID，运行应用的用户和该应用  
> ps -eo pid,user,args    
   
格式化输出root用户（真实的或有效的UID）创建的进程  
> ps -U root -u root u  
  
使用PS实时监控进程状态  
> watch -n 1 'ps -aux --sort -pmem, -pcpu'  



