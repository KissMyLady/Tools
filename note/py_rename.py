批量改名     
=====

```Python
import os

def get_filelist(dir, Filelist):
	if os.path.isfile(dir):
		Filelist.append(dir)
	elif os.path.isdir(dir):
		for s in os.listdir(dir):
			if 'you want rename' in s:
				bb_newDir = s.replace('hm_', '')
				print(bb_newDir)
				newDir = os.path.join(dir, s)
				print(newDir)
				aaaaa = os.path.join(dir, bb_newDir)
				os.rename(newDir, aaaaa)
				get_filelist(newDir, Filelist)
			else:
				newDir = os.path.join(dir, s)
				get_filelist(newDir, Filelist)
		return Filelist

if __name__ == '__main__':
	dir_path = r'D:\Python初级工程师'
	list = get_filelist(dir_path, [])
```
