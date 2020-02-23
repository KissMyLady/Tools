### Pandas数据可视化(https://www.cnblogs.com/lemonbit/p/6896499.html)

> 1. 按日期筛选数据
>
> 2. 按日期显示数据
>
> 3. 按日期统计数据

### 方法步骤:  

###### 1. 读取并整理数据

###### 2. 按日期筛选数据

###### 3. 按日期显示数据

###### 4. 按日期统计数据



## 1. 读取并整理数据

#### 1.1 读取数据:  

```python
import pandas as pd
# 2-23_version_two.csv utf-8
# 2-23_version.txt     gbk
csv_path = r'G:\big data folder\Date_version\2-23_version_two.csv' # 先txt保存utf8,再打开utf-8
# read_csv里面没有字节码选择 
df = pd.read_csv(csv_path, header=None)
print(df.head(2))
```

显 示:  


```python
       0  1    2          3            4           5
0   name  G    A    Address      in_time   Determine
1  病例230  女  43岁  容城镇金源建材市场  无入院时间, 直接确诊  2020年2月16日
```

#### 1.2 整理数据: 

>  pd.to_datetime用法:  Pandas 基础(17) - to_datetime(https://www.cnblogs.com/rachelross/p/10493556.html)

一气呵成:  

```python
import pandas as pd
csv_path = r'G:\big data folder\Date_version\new_1.csv'
df = pd.read_csv(csv_path, header=None)

# 1. 整理数据:
# 1.1 数据列表重命名, 对应6个列表:
df.columns = ["a_name",    "b_Gender", "c_Age",
              "d_Address", "e_intime", "f"]
df['f'] = pd.to_datetime(df['f'], errors='ignore') # 将数据类型转换为日期类型
df = df.set_index('f')  # 将date设置为index


print(df.head(5))
''' 日期设为索引:
Determine   name        G     A    Address      in_time
2020-2-16  病例230        女    43  容城镇金源建材市场  无入院时间, 直接确诊
2020-2-6     病例1        女    42    龚场镇农贸市场    2020年2月4日
2020-1-30    病例2        男    41     汪桥镇庄屋坮   2020年1月21日
2020-2-2     病例3        女    60     容城镇企业局   2020年1月20日
'''
print("打印df.shape: ", df.shape)  # (267, 5)

# 1.2 查看Dataframe的数据类型
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(df.index)
'''
Index(['Determine', '2020-2-16',  '2020-2-6', '2020-1-30',  '2020-2-2',
       '2020-1-29',  '2020-2-6', '2020-1-30', '2020-1-29', '2020-1-30',
       ...
       '2020-2-21', '2020-2-21', '2020-2-22', '2020-2-22', '2020-2-22',
               nan,         nan,         nan,         nan,         nan],
      dtype='object', name='f', length=267)
'''
print("打印df.index类型: ", type(df.index))  # <class 'pandas.core.indexes.base.Index'>


# 1.2 构造Series类型数据
s = pd.Series(df['c_Age'], index=df.index)
print(type(s))
print("--"*20)
print(s.head(2))
'''
f
Determine     A
2020-2-16    43
Name: c_Age, dtype: object
'''
```





## 2 按日期筛选数据













# 常规可视化

```Python
from pyecharts.charts import Bar

# bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# bar.render_notebook()
#
# bar.render()
'''date
{'1-29': 17, '1-30': 14, '1-31': 8, '2-1': 9, '2-2': 50, '2-3': 11,
'2-4': 6, '2-5': 5, '2-6': 34, '2-7': 9, '2-8': 10, '2-9': 8, '2-10': 11,
'2-11': 7, '2-12': 11, '2-13': 6, '2-14': 12, '2-15': 7, '2-16': 2,
'2-17': 7, '2-18': 3, '2-19': 5, '2-20': 2, '2-21': 3, '2-22': 3, '2-23': 0}
'''
list_dict = {'1-29': 17, '1-30': 14, '1-31': 8, '2-1': 9, '2-2': 50, '2-3': 11,
'2-4': 6, '2-5': 5, '2-6': 34, '2-7': 9, '2-8': 10, '2-9': 8, '2-10': 11,
'2-11': 7, '2-12': 11, '2-13': 6, '2-14': 12, '2-15': 7, '2-16': 2,
'2-17': 7, '2-18': 3, '2-19': 5, '2-20': 2, '2-21': 3, '2-22': 3, '2-23': 0}

DATE_LIST = list()
DATE_NUMS = list()
for date in list_dict:
	date_time = date
	date_nums = list_dict[date]
	
	DATE_LIST.append(date)
	DATE_NUMS.append(date_nums)

for i, j in zip(DATE_LIST, DATE_NUMS):
	print(i , j)

bar = Bar()
# bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

bar.add_xaxis(DATE_LIST)
bar.add_yaxis("感染人数", DATE_NUMS)
bar.render_notebook()
bar.render()
```


