# 基于华为云函数构建FREE GPT-PROXY

## 1.前置操作
### 1.注册华为云账号
略
### 2.创建华为云函数:
进入https://console.huaweicloud.com/functiongraph/?region=cn-north-4#/serverless/dashboard，点击【创建函数】
选择HTTP函数，区域选择新加坡（**其他非中国大陆地区也可以**），语言选择python3，点击创建
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/61df720e-9d27-4557-b54d-a240ef3980d7)
新建index.py，复制代码内容
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/24359d11-0ad3-4469-a707-0da2d6369d48)
设置页面中超时时间改为100
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/684a3e6b-f31a-4f6b-8dfc-e1687e9f17e6)
创建触发器，选择APIG网关，设置安全认证为IAM，选择协议为HTTPS
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/5a2b4d23-0474-43de-8c9c-8dd1445b9f49)
完成后复制函数的URL备用
<img width="934" alt="image" src="https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/94365567-10ca-41c8-a1f2-528a768345f4">

### 3.创建IAM认证
点击右上角账号，点击我的凭证，进入凭证管理
点击创建用户：
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/74c5982f-9e36-481d-8ee0-a2ec2dde0c24)
输入即将要创建的用户的用户名和密码，打开编程访问和控制台访问的访问方式，其他选项保持默认选择：
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/408fc0f4-3c6b-48cb-bbad-bce30ea83950)
建立用户组，将刚刚建立的用户收入用户组中，并为用户组授权，在这里，为了方便我们直接收入到admin用户组中：
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/30f09e3c-3e47-4114-80c5-56b441880f8a)


## 2.华为云接口认证token获取
```shell
curl --request POST \
  --url 'https://iam.myhuaweicloud.com/v3/auth/tokens?nocatalog=true' \
  --header 'content-type: application/json' \
  --data '{
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "domain": {
                        "name": "华为云账号"        	//华云云账号
                    },
                    "name": "IAM用户名",             	//IAM用户名
                    "password": "IAM密码"      		//IAM用户密码
                }
            }
        },
        "scope": {
            "project": {
                "name": "ap-southeast-3"               //项目名称
            }
        }
    }
}'
```

## 3.调用函数
### 获取支持的模型列表：
```shell
curl --request POST \
  --url 云函数的URL \
  --header 'X-Auth-Token: 华为认证的token' \
  --header 'X-OpenAI-Key: chatgpt的key' \
  --header 'X-OpenAI-Method: get' \
  --header 'X-OpenAI-Url: https://api.openai.com/v1/models' \
  --header 'content-type: application/json'
```
### 请求gpt对话
```shell
curl --request POST \
  --url 云函数的URL \
  --header 'X-Auth-Token: 云函数的token' \
  --header 'X-OpenAI-Key: chatgpt的key' \
  --header 'X-OpenAI-Method: post' \
  --header 'X-OpenAI-Url: https://api.openai.com/v1/chat/completions' \
  --header 'content-type: application/json' \
  --data '{
	"model": "gpt-3.5-turbo",
	"messages": [
		{
			"role": "user",
			"content": "Hello!"
		}
	]
}'
```
