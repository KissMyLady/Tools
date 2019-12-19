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












||gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D268%2C152%2C50/sign=be82e914a151f3dec3e7ea24f2d3c229/7acb0a46f21fbe0948f7e2ca65600c338644ad46.jpg
||gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D268%2C152%2C50/sign=7596961fc01b9d168a92c92195e386b9/730e0cf3d7ca7bcb0916c3efb0096b63f724a884.jpg
||gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D268%2C152%2C50/sign=73c824193701213fcf661d9c32da04e7/908fa0ec08fa513dd84f7c1e336d55fbb3fbd90d.jpg
||gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D268%2C152%2C50/sign=15a5e07f825494ee87775c594bc8d2c8/.*？.jpg
||gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/whfpf%3D268%2C152%2C50/sign=c5a27de2bd1bb0518f71e0685047e882/.*.jpg
www.baidu.com##div[id="content_right"]
www.baidu.com##content_right
www.baidu.com##DIV[id="content_right"][class="cr-offset"]
www.baidu.com##.content_right
pornhub.com##.xpjcoeiwea
pornhub.com##.xlddfhyeyg
pornhub.com##.trlbqmowdv
pornhub.com##.ppkwnmjmnl
pornhub.com##.ohstkrtooj
pornhub.com##.nugslysjxz
pornhub.com##.kqrbztjtew
pornhub.com##.jfyupwbsdf
pornhub.com##.itvxtukqee
pornhub.com##.fiwhooybms
jianshu.com##._2OwGUo
blog.csdn.net##.recommend-item-box.recommend-recommend-box
blog.csdn.net##.recommend-item-box.blog-expert-recommend-box
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/summer270x150.png"]
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/.*"]
baike.baidu.com##img[src="https://baikebcs.bdimg.com/adpic/*"]
baidu.com##side-content
baidu.com##content_right






## https://blog.csdn.net/qq_15192373/article/details/81091278
4. 创建快捷方式
1）在/usr/share/applications创建一个文件：pycharm.desktop（touch，gedit，nano指令等）

cd /usr/share/applications
sudo gedit pycharm.desktop
2）编辑这个文件，添加以下内容

[Desktop Entry]
Version=1.0
Type=Application
Name=Pycharm
Icon=/home/zhuying/桌面/Home/pycharm-community-2019.1.1/bin/pycharm.png
Exec=sh /home/zhuying/桌面/Home/pycharm-community-2019.1.1/bin/pycharm.sh
MimeType=application/x-py;
Name[en_US]=pycharm



4. 创建快捷方式
在/usr/share/applications创建一个文件：pycharm.desktop（touch，gedit，nano指令等）

cd /usr/share/applications
sudo gedit pycharm.desktop
2）编辑这个文件，添加以下内容

[Desktop Entry]
Version=1.0
Type=Application
Name=sublime
Icon=/home/zhuying/桌面/Home/sublime_text_3/Icon/128x128/sublime-text.png
Exec=/home/zhuying/桌面/Home/sublime_text_3/sublime_text
MimeType=application/x-py;
Name[en_US]=sublime


lspci |grep VGA
00:0f.0 VGA compatible controller: VMware SVGA II Adapter

xrandr --addmode VIRTUAL1 1680x1050

sudo xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
