Redis分布式集群搭建  
=====  
效果图   
![ScreenShot00004](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot00004.jpg)  

## 先搭建Redis执行环境   
#### [下载-点击进入官网下载最新](https://redis.io/)  
> `wget http://download.redis.io/releases/redis-5.0.5.tar.gz`  
#### 解压  
> `tar -zxvf redis-3.2.8.tar.gz`  
    
#### 复制    
将文件放到usr/local⽬录下(可以自己选定其他目录, 但推荐这个,便于日后查找文件)    
> `sudo mv ./redis-3.2.8 /usr/local/redis/`  
#### 进⼊redis⽬录  
> `cd /usr/local/redis/`  

#### 生成   
> `sudo make`  
#### 测试(耗时长)   
> `sudo make test`  

#### 安装, 将redis的命令安装到/usr/local/bin/⽬录    
> `sudo make install`  

#### 完成后, 我们进入目录/usr/local/bin中查看       
> `cd /usr/local/bin`  
> `ls -all`  
>    
>> 文件说明    
>>> redis-server redis    :服务器  
>>> redis-cli redis       :命令行客户端  
>>> redis-benchmark redis :性能测试工具   
>>> redis-check-aof       :AOF文件修复工具  
>>> redis-check-rdb       :RDB文件检索工具  
此时, 就可以启动Redis服务器了, 但是还需要配置一点文件才能算完全成功    


## 配置Redis.conf文件       
#### 将配置⽂件移动到/etc/⽬录下      
* 移动前, 先手动创建这个路径       
* 同样的, 这个配置文件也可以不移动, 但是推荐移动, 方便日后查找修改        

配置⽂件⽬录为/usr/local/redis/redis.conf  
```Linux 
sudo cp /usr/local/redis/redis.conf /etc/redis/  
```

### 核心配置选项     
```Linux   
> 绑定ip：如果需要远程访问，可将此⾏注释，或绑定⼀个真实ip    
bind 127.0.0.1      

端⼝，默认为6379     
port 6379   
是否以守护进程运⾏  
如果以守护进程运⾏，则不会在命令⾏阻塞，类似于服务    
如果以⾮守护进程运⾏，则当前终端被阻塞  
设置为yes表示守护进程，设置为no表示⾮守护进程   
推荐设置为yes  
daemonize yes  

数据⽂件  
dbfilename dump.rdb  
  
数据⽂件存储路径    
dir /var/lib/redis   
(需要手动创建一个路径, 推荐创建这个, 方便日后管理)    

⽇志⽂件  
logfile /var/log/redis/redis-server.log  
(需要手动创建一个路径, 推荐创建这个, 方便日后管理)  

数据库，默认有16个  
database 16  

主从复制，类似于双机备份  
slaveof  
```
  

## 启动服务器/客户端   
恭喜恭喜, 看见曙光了, 现在可以开始启动了!   
### 启动服务器端  
使⽤help查看帮助⽂档  
> redis-server --help  
  
启动, 指定加载的配置文件  
> sudo redis-server /etc/redis/redis.conf   

停⽌
> 第一种方法:  
>> sudo service redis stop    
> 第二章方法:    
>> ps -ef|grep redis 查看redis服务器进程  
>> sudo kill -9 pid 杀死redis服务器  

重启   
`sudo service redis restart`  


### 启动客户端   
使⽤help查看帮助⽂档     
> redis-cli --help    

连接redis 
> redis-cli    

连接redis 
运⾏测试命令 
> ping(长江长江, 我是黄河, 收到请回答)    
> 黄河黄河, 长江收到   

## 搭建集群前要了解的知识引导   
[为什么要有集群](https://blog.csdn.net/u010498753/article/details/86510939)   
1. 一个项目服务(网站)，如果部署在一台Machine上，
> 所有的请求，都由这一台服务器处理，存在很大风险:    

#### A：并发处理能力有限  
> （一般单台服务器处理的并发量为250左右，超过250，可能会出现数据丢失，链接不稳定的情况）。因为单服务器的性能有限制。所以单台Tomcat的最大连接数有限制   

#### B：容错率低，一旦服务器故障，整个服务就无法访问了  
> eBay于 1999年6月停机22小时的事故，中断了约230万的拍卖，使eBay的股票下降了9.2个百分点。   

#### C：单台服务器计算能力低，无法完成复杂的海量数据计算    
> 提高CPU主频和总线带宽是最初提供计算机性能的主要手段。但是这一手段对系统性能的提供是有限的  
> 接着人们通过增加CPU个数和内存容量来提高性能，于是出现了向量机，对称多处理机(SMP)等    
> 
> 但是当CPU的个数超过某一阈值，这些多处理机系统的可扩展性就变的极差     
> 主要瓶颈在于CPU访问内存的带宽并不能随着CPU个数的增加而有效增长     
> 集群系统的性能随着CPU个数的增加几乎是线性变化的   


### [什么是集群](https://blog.csdn.net/u010498753/article/details/86510939)       
> 集群是是指将多台服务器集中在一起，每台服务器都实现相同的业务，做相同的事情     

#### 2.1 伸缩性（Scalability）
> 在一些大的系统中，预测最终用户的数量和行为是非常困难的, 伸缩性是指系统适应不断增长的用户数的能力      
> 提高这种并发会话能力的一种最直观的方式就增加资源(CPU，内存，硬盘等)    
> 集群是解决这个问题的另一种方式，它允许一组服务器组在一起，像单个服务器一样分担处理一个繁重的任务   
> 我们只需要将新的服务器加入集群中即可   
> 对于客户来看，服务无论从连续性还是性能上都几乎没有变化，好像系统在不知不觉中完成了升级   

#### 2.2 高可用性（High availability）  
> 单一服务器的解决方案并不是一个健壮方式，因为容易出现单点失效    
> 像银行、账单处理这样一些关键的应用程序是不能容忍哪怕是几分钟的死机  
>> 它们需要这样一些服务在任何时间都可以访问并在可预期的合理的时间周期内有响应    
>> 高可用性集群的出现是为了使集群的整体服务尽可能可用，以便考虑计算硬件和软件的易错性    
>>> 如果高可用性集群中的主节点发生了故障，那么这段时间内将由次节点代替它    
>>> 次节点通常是主节点的镜像，所以当它代替主节点时，它可以完全接管其身份，并且因此使系统环境对于用户是一致的  

#### 2.3 负载均衡（Load balancing）
> 负载均衡集群为企业需求提供了更实用的系统     
>> 如名称所暗示的，该系统使负载可以在计算机集群中尽可能平均地分摊处理     
>> 该负载可能是需要均衡的应用程序处理负载或网络流量负载   
>>> 这样的系统非常适合于运行同一组应用程序的大量用户     
>>> 每个节点都可以处理一部分负载，并且可以在节点之间动态分配负载，以实现平衡     

#### 2.4 高性能 (High Performance )
> 通常，第一种涉及为集群开发并行编程应用程序，以解决复杂的科学问题。
> 这是并行计算的基础，尽管它不使用专门的并行超级计算机，这种超级计算机内部由十至上万个独立处理器组成。
>> 但它却使用商业系统，如通过高速连接来链接的一组单处理器或双处理器PC, 并且在公共消息传递层上进行通信以运行并行应用程序。
>>> 因此，会常常听说又有一种便宜的Linux超级计算机问世了。 但它实际是一个计算机集群，其处理能力与真的超级计算机相等


### [为什么要进行分布式](https://blog.csdn.net/u010498753/article/details/86510939)   
传统的项目中，我们将各个模块放在一个系统中  
系统过于庞大，开发维护困难，各个功能模块之间的耦合度增高    
无法针对单个模块进行优化，也无法进行水平扩展。  

### [什么是分布式](https://blog.csdn.net/u010498753/article/details/86510939)  
> 分布式是指将多台服务器集中在一起，每台服务器都实现总体中的不同业务，做不同的事情  
>> 并且每台服务器都缺一不可，如果某台服务器故障，则网站部分功能缺失，或导致整体无法运行  
>>> #### 存在的主要作用是大幅度的提高效率，缓解服务器的访问和存储压力

### [分布式和集群的关系](https://blog.csdn.net/u010498753/article/details/86510939) 
在开发中我们可以将分布式和集群分开吗？  
这个问题，我们可以根据分布式的介绍看出    
其主要的功能是用了将我们的系统模块化，将系统进行解耦的，方便我们的维护和开发的    
但是其并不能解决我们的并发问题，也无法保证我们的系统在服务器宕机后的正常运转。     

而集群呢？其恰好弥补了分布式的缺陷，集群，就是多个服务器处理相同的业务     
> 这在一方面可以解决或者说改善我们系统的并发问题    
> 一方面可以解决我们服务器如果出现一定数量的宕机后，系统仍然可以正常运转    
  
因此我说，分布式和集群式一堆好基友，谁也离不开谁。。。。  


## Redis集群搭建--文件配置   
需要准备的东西:   
> 如果使用的是虚拟机, 请准备:  
>> 1. 下载虚拟机, 虚拟机之间能够相互ping通  
>> 2. 电脑能同时运行两台以上  
> 
> 如果使用的是实体, 请准备:   
>> 1. 同上, 只是吧虚拟机换成了实体电脑   


### 下面是虚拟机的分布式集群搭建    
此时我的配置:     
1. 一台Ubuntu为Master    
2. 一台Ubuntu server 编号one  
3. 一台Ubuntu server 编号two  

### 1. Ubuntu配置文件--并启动    
打开配置文件(可以自定义路径, 推荐默认地址, 方便日后查找)
创建7000.conf配置文件
```Linux
sudo vim 7000.conf
输 入: 
port 7000
bind 192.168.0.104
daemonize yes
pidfile 7000.pid
cluster-enabled yes
cluster-config-file 7000_node.conf
cluster-node-timeout 15000
appendonly yes
保 存
```
创建7001.conf配置文件
```Linux
sudo vim 7001.conf
输 入: 
port 7001
bind 192.168.0.104
daemonize yes
pidfile 7001.pid
cluster-enabled yes
cluster-config-file 7001_node.conf
cluster-node-timeout 15000
appendonly yes
保 存
```
创建7002.conf配置文件
```Linux
sudo vim 7002.conf
输 入: 
port 7002
bind 192.168.0.104
daemonize yes
pidfile 7002.pid
cluster-enabled yes
cluster-config-file 7002_node.conf
cluster-node-timeout 15000
appendonly yes
保 存
```
此时文件配置完成, 现在启动这三个服务器  
```Linux
redis-server 7000.conf
redis-server 7001.conf
redis-server 7002.conf
```
使用命令查看服务器启动情况  
> ps -aux|grep redis
![ScreenShot00003](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot00003.jpg)


### Ubuntu_Server_one配置文件--并启动     
步骤同上  
```Linux
port 7003
bind 192.168.0.101
daemonize yes
pidfile 7003.pid
cluster-enabled yes
cluster-config-file 7003_node.conf
cluster-node-timeout 15000
appendonly yes

port 7004
bind 192.168.0.101
daemonize yes
pidfile 7004.pid
cluster-enabled yes
cluster-config-file 7004_node.conf
cluster-node-timeout 15000
appendonly yes

port 7005
bind 192.168.0.101
daemonize yes
pidfile 7005.pid
cluster-enabled yes
cluster-config-file 7005_node.conf
cluster-node-timeout 15000
appendonly yes
```
![ScreenShot00001](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot00001.jpg)

### Ubuntu_Server_two配置文件--并启动     
```Linux
port 7006
bind 192.168.0.102 
daemonize yes
pidfile 7006.pid
cluster-enabled yes
cluster-config-file 7006_node.conf
cluster-node-timeout 15000
appendonly yes

port 7007
bind 192.168.0.102 
daemonize yes
pidfile 7007.pid
cluster-enabled yes
cluster-config-file 7007_node.conf
cluster-node-timeout 15000
appendonly yes

port 7008
bind 192.168.0.102 
daemonize yes
pidfile 7008.pid
cluster-enabled yes
cluster-config-file 7008_node.conf
cluster-node-timeout 15000
appendonly yes
```
![ScreenShot00002](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot00002.jpg)

## 创建集群     
安装ruby环境，因为redis-trib.rb是⽤ruby开发的     
[Ruby简介](https://www.runoob.com/ruby/ruby-intro.html)
节选:  
> Ruby是一种纯粹的面向对象编程语言。它由日本的松本行弘(まつもとゆきひろ/Yukihiro Matsumoto)创建于1993年。  
> 您可以在www.ruby-lang.org的Ruby邮件列表上找到松本行弘的名字。  
> 在Ruby社区，松本也被称为马茨（Matz）。  
> 
> Ruby是"程序员的最佳朋友"。
> Ruby的特性与 Smalltalk、Perl和Python类似。
> Perl、Python和Smalltalk 是脚本语言。
> Smalltalk是一个真正的面向对象语言。 
> Ruby，与Smalltalk一样，是一个完美的面向对象语言。    
> 使用Ruby的语法比使用Smalltalk的语法要容易得多。   

Ubuntu有自带Ruby版本, 如果太旧, 可以使用下面的方法更新(实测有效)    
```Linux
ruby -v

添加 PPA 源：
sudo add-apt-repository ppa:brightbox/ruby-ng
sudo apt-get update

先删除旧版本：
sudo apt-get purge --auto-remove ruby

然后安装新版本：
sudo apt-get install ruby2.6 ruby2.6-dev
```

## 启动集群  
1. 确保配置文件IP地址都正确     
2. 确保服务器都开启了   
找到redis-cli文件所在地  
打开终端输入:
```Linux
./redis-cli --cluster create 192.168.0.104:7000 192.168.0.104:7001 192.168.0.104:7002 192.168.0.101:7003 192.168.0.101:7004 192.168.0.101:7005 192.168.0.102:7006 192.168.0.102:7007 192.168.0.102:7008 --cluster-replicas 1
```  
上面格式化后看起来应该是这样:  
```Linux
./redis-cli --cluster create 
192.168.0.2:7001 
192.168.0.2:7002 
192.168.0.2:7003 
192.168.0.2:7004 
192.168.0.2:7005  
192.168.0.2:7006 
--cluster-replicas 1
```
效果图  
![ScreenShot00004](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot00004.jpg)  



## Redis简介
Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库, 并提供多种语言的API 
> 从2010年3月15日起，Redis的开发工作由VMware主持。    
> 从2013年5月开始，Redis的开发由Pivotal赞助。    
>> Redis是 NoSQL技术阵营中的一员，它通过多种键值数据类型来适应不同场景下的存储需求    
>> 借助一些高层级的接口使用其可以胜任，如缓存、队列系统的不同角色    
  
### Redis特性
Redis与其他key-value缓存产品有以下三个特点：    
> Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。    
> Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。    
> Redis支持数据的备份，即master-slave模式的数据备份。    
  
  
### Redis 优势
* 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。  
* 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。  
* 原子 – Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行。  
* 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。  

### redis应用场景
用来做缓存(ehcache/memcached)——redis的所有数据是放在内存中的（内存数据库）
可以在某些特定应用场景下替代传统数据库——比如社交类的应用
在一些大型系统中，巧妙地实现一些特定的功能：session共享、购物车
只要你有丰富的想象力，redis可以用在可以给你无限的惊喜…….


### nosql介绍  
NoSQL：一类新出现的数据库(not only sql)      
它的特点：    
> - 不支持SQL语法  
> - 存储结构跟传统关系型数据库中的那种关系表完全不同，nosql中存储的数据都是KV形式  
> - NoSQL的世界中没有一种通用的语言，每种nosql数据库都有自己的api和语法，以及擅长的业务场景  

NoSQL中的产品种类相当多：  
> Mongodb  
> Redis  
> Hbase hadoop  
> Cassandra hadoop  
  
NoSQL和SQL数据库的比较：  
> 适用场景不同：sql数据库适合用于关系特别复杂的数据查询场景，nosql反之    
> “事务”特性的支持：sql对事务的支持非常完善，而nosql基本不支持事务    
> 两者在不断地取长补短，呈现融合趋势  


