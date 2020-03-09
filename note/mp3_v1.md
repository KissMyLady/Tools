Mp3文件播放器  
=====

### 介 绍:   输入音频文件代码, 播放对应mp3文件  
![ScreenShot-00467](https://github.com/KissMyLady/Tools/blob/master/img/ScreenShot-00467.jpg)   
### 使用方法:  
> 1. 直接运行, 有输入提示

### 适用范围:  任意文件夹的音频文件  
## 1. 歌曲播放器 
```Python
import os, time
import pygame, random
import threading

# 找到所有文件
def Find_Music_Path(music_path):
    path_list = list()
    files = os.listdir(music_path)
    
    for i in files:
        if i.endswith(".mp3"):
            new_path = os.path.join(music_path, i)
            path_list.append(new_path)
        else:
            pass
    return path_list


# 暂停器
def stop_music(info_socket):
    while True:
        info = input('请输入, s暂停, 任意键开始, n: 下一曲')
        if info == 's':
            pygame.mixer.music.pause()
		
        elif info == 'n':
            pygame.mixer.music.stop()
			
        else:
            pygame.mixer.music.unpause()
		
			
# 播放器
def play_music(filepath):
    print("正在播放的是>>>>>>>", filepath)
    pygame.mixer.init()  # 初始化音频的部分
    pygame.mixer.music.load(filepath)
    music_value = 0.6
    pygame.mixer.music.set_volume(music_value)  # 音量, 0.0---1.0。
    pygame.mixer.music.play(start=0.0)  # loops和start分别代表重复的次数和开始播放的位置
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    
    # pygame.mixer.music.queue(filename)
    # 使用指定下一个要播放的音乐文件，当前的音乐播放完成后自动开始播放指定的下一个。一次只能指定一个等待播放的音乐文件。
    
    # pygame.mixer.music.get_busy()
    # 判断是否在播放音乐, 返回1为正在播放。
    n = 0
    while True:
        if pygame.mixer.music.get_busy() == 1:
            if n > 10:
                time.sleep(0.5)
            else:
                time.sleep(2)
                n += 1
        else:
            break
		
    pygame.mixer.music.stop()


def main(music_path):
    file_dict = dict()
    files = Find_Music_Path(music_path)  # 找到所有音频文件
    for i in range(len(files)):
        music = random.choice(files)
        play_music(music)


if __name__ == '__main__':
    music_path = r'G:\歌曲'
    t1 = threading.Thread(target=main, args=(music_path, ))
    t2 = threading.Thread(target=stop_music, args=(pygame, ))
	
    t1.start()
    t2.start()
```


## 2. 英语mp3播放器
```python
'''去水印:
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
'''
import os, time
import pygame
from random import shuffle


# 找到所有文件
def Find_Music_Path(music_path):
    path_list = list()
    files = os.listdir(music_path)
	
    for i in files:
        if i.endswith(".mp3"):
            new_path = os.path.join(music_path, i)
            path_list.append(new_path)
        else:
            pass
		
    return path_list


# 播 放
def play_music(filepath):
    print("正在播放的音频文件>>>>>>>", filepath)
    pygame.mixer.init()  # 初始化音频的部分
    pygame.mixer.music.load(filepath)
    music_value = 0.6
    pygame.mixer.music.set_volume(music_value)  # 音量, 0.0---1.0。
    pygame.mixer.music.play(start=0.0)  # loops和start分别代表重复的次数和开始播放的位置
    # 播放时长，没有此设置，音乐不会播放，会一次性加载完
    keyworld = input("s暂停, us取消暂停, 输入任意下一曲")
    
    while True:
        if keyworld == "s":
            pygame.mixer.music.pause()
            keyworld = input("输入: s暂停, us取消暂停, g下一曲: ")
			
        elif keyworld == "us":
            pygame.mixer.music.unpause()
            keyworld = input("输入:s暂停, us取消暂停, g下一曲: ")
			
        else:
            break

    pygame.mixer.music.stop()


def main(music_path):
    # 新概念一
    file_dict = dict()
    files = Find_Music_Path(music_path)	
    
    # 创建播放列表, "音频序号": "绝对路径"
    n = 0
    for i in range(1, 148, 2):
        try:
            file_dict["{}".format(i)] = files[n]
        except:
            pass
    n += 1
		
    while True:
        nums_list = [num for num in range(1, 148, 2)]
        print("可供选择的序号: ", nums_list)
        key_nums = input("请输入要播放的序列号>>>>> ")
		
        if int(key_nums) in nums_list:
            path = file_dict["{}".format(key_nums)]
            print("输入的序号是:",'\t', key_nums, "对应的路径是:",'\t', path)
            play_music("{}".format(path))
			
        else:
            shuffle(files)
            print('输入的数字没有对应的音频, 5s后默认随机播放')
            time.sleep(5)
            print(">>>>>>开始随机选取一首播放<<<<<<")
            play_music(files[5])


	# shuffle(files)
	# for i in files:
	# 	filepath = r"{}".format(i)
	# 	play_music(filepath, file_dict)


if __name__ == '__main__':
    music_path = r'F:\英语文件集合\新概念--听力分册'
    main(music_path)
```

