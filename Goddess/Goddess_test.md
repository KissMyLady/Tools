女神选备胎问题--不要成为37%的样本   
====

## 预览图   
一图胜千语  
![goddess1](https://github.com/KissMyLady/Daily_Tools_Create/blob/master/Goddess/goddess.jpg)   
![goddess2](https://github.com/KissMyLady/Daily_Tools_Create/blob/master/Goddess/goddess2.jpg)  

> 柏拉图有一天问老师苏格拉底什么是爱情  
> 苏格拉底叫他到麦田走一次  
> 要不回头地走  
> 在途中要摘一棵最大最好的麦穗  
> 但只可以摘一次  
> 柏拉图觉得很容易  
> 充满信心地出去  
> 谁知过了半天他仍没有回去  
> 最后,他垂头丧气出现在老师跟前诉说空手而回的原因:   
> "很难得看见一株看似不错的,却不知是不是最好,  
> 不得已,因为只可以摘一次,只好放弃,再看看有没有更好的,  
> 到发现已经走到尽头时,才发觉手上一棵麦穗也没有  
> 这时,苏格拉底告诉他:  
> "那就是爱情——爱情是一种理想，而且很容易错过。"  

### 于是我们发现，爱情似乎很难选择吗？  
很多人都知道答案，先想象自己能谈多少次恋爱，然后在37%的地方打住，  
前面37%的恋爱，都但作为经验(样本), 后38%开始，只要有任何一个个体比  
37%里的样本优秀，我们就可以认为这个选择是可行了。 37%，是女神选取  
真命天子的最佳点。  

## 用程序模拟这个过程  
结果图, 假设女神谈100次恋爱,  增加样本数量，谈1000遍  
1-100分为伴侣分数(虽然我不赞成人用分数来衡量，暂且先这样把)  
如果女伴侣大于90分，我们就认为她成功了，反之，失败    
通过模拟， 这样女神有75%的几率是'成功人士'  
努力努力再努力吧， 让自己变得具有可塑性，   
### 程序模拟图
在模拟1000遍， 每次谈恋爱100次情况下，女神的成功率是75%, 看来非常高    
这还是100分中的， 90分的标准， 真实情况下， 80%对大部分人来说也很不错了    
! [goddess3](https://github.com/KissMyLady/Daily_Tools_Create/blob/master/Goddess/goddess3.jpg)   
代码在末尾  

## 结  论:
### 致男生  
* 1、男生不要落在那37%的样本区间;  
* 2、在备选集第一个出现;  

### 应  用:
1、买房： 如果你要看100套房， 把前37个人作为样本，看后面的就可以了。  
  但是中介也知道这个东西， 他们会先让你看比价差的房，拉低你的预期，  
  然后再看好的。

2、买车， 也是同上原理 

3、工作， 如果平均要换10次工作，那么前3次就作为样本，后面的7次，  
  作为备选区间，只要有一个比前面样本的好，那么就选这个。  
  
### 结  语:  
爱情当然还有很多因素影响， 还有很多维度，如果遇上喜欢的，就在一起吧~    
老化说的好，水至清则无鱼，人至察则无徒，太关注利益反而不好。 如果做人  
都这样， 那还有什么意思呢  

最后，我也希望能和喜欢的人在一起，希望大家也是，祝大家能够找到自己喜欢的人，恩恩爱爱  

```Python
import random

def main():
    def sample():                       # 生成社会随机样本, 优秀程度: 渣男1, 真命天子100
        one_sample = list()
        for x in range(100):
            one_sample.append(random.randint(1,100))
        return one_sample
    
    FIST_SAMPLE = sample()              # 女神开始对测试样本进行细致考察
    fist_reserve = list()               # 女神的37个样本测试集
    test_num =0
    for fool_man in FIST_SAMPLE:        # 现在开始恋爱
        fist_reserve.append(fool_man)   # 前37次恋爱，作样本测试集
        FIST_SAMPLE.remove(fool_man)    # 总体样本里移除37恋爱
        if test_num == 36:
            break                       # 如果已经谈了37次恋爱, 就开始选取真命天子
        test_num += 1
    
    
    print('开始选取真命天子, 样本集数量:', len(fist_reserve),'备选数量:', len(FIST_SAMPLE))
    print('因为是女神亲手把关, 所以她知道样本里面最优秀的人是: ',max(fist_reserve))
    times = 0
    for good_man in FIST_SAMPLE:                   # 此时, 有62个备选人
        if good_man < max(fist_reserve):           # 从备选中取, 只要比样本测试集的优秀, 就行
            if times > 61:
                print('最后一个', good_man)
                if good_man > 90:
                    print('>' * 10, '女神成功了', '<' * 10)
                    return True
                else:
                    print('真命天子分数太低, 不视同为成功')
                    print('>' * 10, '很不幸, 女神失败了', '<' * 10)
                    return False
            else:
                pass
        else:
            print('选取的这个人, 大于样本数, 女神的真命天子是:', good_man)
            if good_man > 90:
                print('>'*10,'女神成功了','<'*10)
                return True
            else:
                print('真命天子分数太低, 不视同为成功')
                print('>' * 10, '很不幸, 女神失败了', '<' * 10)
                return False
        times += 1

c = main()
sucess = 0
for a in range(1000):
    c = main()
    if c:
        sucess += 1
    else:
        pass
    
print('取到90分成功男人成功概率是:', sucess/1000)
```
## 看完了  
- [主页](https://github.com/KissMyLady)  
- [Daily_Tools_Create主页](https://github.com/KissMyLady/Daily_Tools_Create/tree/master)  
