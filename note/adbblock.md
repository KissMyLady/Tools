如何屏蔽网页广告   
====

## 我们先看一个网页  
![guan-1](https://github.com/KissMyLady/Tools/blob/master/img/guan-1.jpg)   


## 插件AdblockPlus      
![guan-2](https://github.com/KissMyLady/Tools/blob/master/img/guan-2.jpg)  
插件下载方法:  
1. 如果可以科学上网, 直接在谷歌浏览器商店搜索下载     
2. 不能科学上网的, 在搜索引擎里搜索这个插件, 网上有安装包,  安装就可以用     



## 拦截不想看到的东西(永久)   
![guan-3](https://github.com/KissMyLady/Tools/blob/master/img/guan-3.jpg)  
![guan-4](https://github.com/KissMyLady/Tools/blob/master/img/guan-4.jpg)  
![guan-5](https://github.com/KissMyLady/Tools/blob/master/img/guan-5.jpg)    


## 网页要清爽  
![guan-6](https://github.com/KissMyLady/Tools/blob/master/img/guan-6.jpg)  


## 百度侧边栏屏蔽规则  
把这几段代码复制到AdblockPlus添加规则里面就可以了  
```Linux
baidu.com##content_right
www.baidu.com##content_right
www.baidu.com##.content_right
www.baidu.com##div[id="content_right"]
baidu.com##side-content
www.baidu.com##DIV[id="content_right"][class="cr-offset"]
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/summer270x150.png"]
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/*"]
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/.*"]
```
![guan-7](https://github.com/KissMyLady/Tools/blob/master/img/guan-7.jpg)  


