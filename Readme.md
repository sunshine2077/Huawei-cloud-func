# 基于华为云函数构建FREE GPT-PROXY

## 1.前置操作
选择HTTP函数，区域选择新加坡，语言选择python3，点击创建
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/61df720e-9d27-4557-b54d-a240ef3980d7)
新建index.py，复制代码内容
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/24359d11-0ad3-4469-a707-0da2d6369d48)
设置页面中超时时间改为100
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/684a3e6b-f31a-4f6b-8dfc-e1687e9f17e6)
创建触发器，选择APIG网关
![image](https://github.com/sunshine2077/Huawei-cloud-func/assets/124233376/5a2b4d23-0474-43de-8c9c-8dd1445b9f49)

## 2.调用函数
### 获取支持的模型列表：
```shell
curl --request POST \
  --url 云函数的URL \
  --header 'X-Auth-Token: 云函数的token' \
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
