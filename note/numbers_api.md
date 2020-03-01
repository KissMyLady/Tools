# 百度云--图像识别

#### 作 用:  

* 图像数字识别



#### 使用方法:  

> 1. [开通百度云云账号](https://login.bce.baidu.com/?redirect=https%3A%2F%2Fconsole.bce.baidu.com%2Fbilling%2F#/order/detail~uuid=cb975c1ba8f14863a5f2a68a40e4a725&serviceType=OCR)  
> 2. 获取`控制台`  的  `access_token`码
> 3. 将获取到的`数据`,  在代码里做相应替换  
> 4. 返回的是json数据, 进行数据清洗, 提取相应数据即可

#### 性 能: 

* 差
* 错误非常高, 怀疑百度的这个的东西是骗人的



##### 调用接口,  提取json数据 

```Python
# encoding:utf-8
import requests, base64
# 数字识别
APP_ID = 'client_credentials&'
API_KEY = 'OYKQ7tzPFGxch5B0gxNLonI6'
SECRET_KEY = 'Rn2Iwa9usvofd8j09O0rCRzfXzAmA7I6'

def find_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=OYKQ7tzPFGxch5B0gxNLonI6&client_secret=Rn2Iwa9usvofd8j09O0rCRzfXzAmA7I6&'
    response = requests.get(host)
    if response:
        access_token_new = response.json()
        t = access_token_new['access_token']
    return t


def run(request_url, params):
    tt = find_token()
    access_token = '{}'.format(tt)
    request_url = request_url + "?access_token=" + access_token
    # print("request_url", request_url)
    
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        content = response.json()
        print (content)
        txt_path = r'G:\content_json.json'
        with open(txt_path, 'a', encoding='utf-8') as f:
            f.write(str(content))


if __name__ == '__main__':
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    file_path = r'G:\1.jpg'
    f = open(file_path, 'rb')
    img = base64.b64encode(f.read())
    params = {"image": img}
    run(request_url, params)
```

##### 清洗数据,  储存到CSV

```python
import csv, re

csv_file = open(r"G:\iphone_nums.csv", 'a', newline="", encoding='utf-8')
writer = csv.writer(csv_file)
writer.writerow(['numbers'])


# 注意, 此处提取的是json数据
with open(r'G:\content_json.json', 'r', encoding='gbk') as f:
	c = f.readlines()


# 数据清洗
for i in c:
    if 'words' in i:
        if '_' in i:
            pass
        else:
            new_i = (i.split(':'))[1]
            c = re.findall(r'\d+', new_i)
            print(c)
			
        try:
            c = int(c[0])
            writer.writerow([c])
        except:
            pass
    else:
        pass

csv_file.close()
```

##### 图像转url:  

```python
import base64


with open(r"G:\big data folder\12-13\图像识别\电话号码\1.jpg", 'rb') as f:
    base64_data = base64.b64encode(f.read())
    s = base64_data.decode()
    # print('data:image/jpeg;base64, %s' % s)

input_path = r'G:\big data folder\12-13\图像识别\电话号码\1.txt'
with open(input_path, 'a' ,encoding='utf-8') as f:
    f.write(str(s))
    
print(s)
```

**请求URL数据格式**

向授权服务地址`https://aip.baidubce.com/oauth/2.0/token`发送请求（推荐使用POST），并在URL中带上以下参数：

- **grant_type：** 必须参数，固定为`client_credentials`；
- **client_id：** 必须参数，应用的`API Key`；
- **client_secret：** 必须参数，应用的`Secret Key`；

```tex
https://aip.baidubce.com/oauth/2.0/token?
grant_type=client_credentials&
client_id=Va5yQRHlA4Fq5eR3LT0vuXV4&     
client_scret=0rDSjzQ20XUj5itV6WRtznPQSzr5pVw2&
```

### 控制台百度云账号 : 

```
https://aip.baidubce.com/oauth/2.0/token?

grant_type=client_credentials&
client_id=32Rk0eO7pIhZjXs2y3FLSVCW
client_secret=6CppLlK7R935bqfu2068OKwi27YNaXcn

{"error_description":"The request is missing a required parameter","error":"invalid_request"}
```

#### 拼接---OK

```
https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=32Rk0eO7pIhZjXs2y3FLSVCW&client_secret=6CppLlK7R935bqfu2068OKwi27YNaXcn&

```

## refresh_token

```
{"refresh_token":"25.38d6d5840266d7a745d5bc0e25716b5a.315360000.1898404668.282335-18628984","expires_in":2592000,"session_key":"9mzdCKZ02DVzE3B59MW6X3HlxueNrzABguSwlGpdACC0d54kdB5GXgX7EnOKFPooM\/3Q106LLuID\/TgIJO6LTUUqvHdj0A==","access_token":"24.3bea745255eceaf380d961213418fa9d.2592000.1585636668.282335-18628984","scope":"public vis-classify_dishes vis-classify_car brain_all_scope vis-classify_animal vis-classify_plant brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify brain_ingredient brain_advanced_general_classify brain_custom_dish brain_poi_recognize brain_vehicle_detect brain_redwine brain_currency brain_vehicle_damage wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406","session_secret":"81bf734ffb1dfac8df43383344245b06"}
```

```json
{
  "refresh_token": "25.38d6d5840266d7a745d5bc0e25716b5a.315360000.1898404668.282335-18628984",
  "expires_in": 2592000,
  "session_key": "9mzdCKZ02DVzE3B59MW6X3HlxueNrzABguSwlGpdACC0d54kdB5GXgX7EnOKFPooM\/3Q106LLuID\/TgIJO6LTUUqvHdj0A==",
  "access_token": "24.3bea745255eceaf380d961213418fa9d.2592000.1585636668.282335-18628984",
  "scope": "public vis-classify_dishes vis-classify_car brain_all_scope vis-classify_animal vis-classify_plant brain_object_detect brain_realtime_logo brain_dish_detect brain_car_detect brain_animal_classify brain_plant_classify brain_ingredient brain_advanced_general_classify brain_custom_dish brain_poi_recognize brain_vehicle_detect brain_redwine brain_currency brain_vehicle_damage wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406",
  "session_secret": "81bf734ffb1dfac8df43383344245b06"
}
```
