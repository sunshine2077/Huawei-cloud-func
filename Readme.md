(1)打开http://www.huaweicloud.com/，注册华为云账户。

(2)打开打开https://console.huaweicloud.com/functiongraph/?region=ap-southeast-3#/serverless/functionList，进入华为云函数控制台，点击右上角【创建函数】：

(3)选择HTTP函数，区域选择新加坡，函数名称随便写，点击创建函数，进入到函数页面：

(4)点击右上角的上传自，选择zip文件，从此处下载zip代码包并上传到此处。接下来点击最上方的设置，点击上常规设置，修改执行超时时间为3000秒：
再点击触发器，点击创建触发器，设置触发器类型为API网关服务，API名称为API_mygpt，点击创建分组，新建一个分组，设置发布环境为release，设置安全认证为NONE，协议为HTTPS，超时时间为60000。
完成后点击确定，复制调用URL，并添加v1/chat/completions后缀
(5)打完收工，之后即可通过各种方式发送请求：

1.通过python：
```python
import requests
​
url = f"{你的URL}/v1/chat/completions"
​
while True:
  text=input()
  
  payload = {
      "model": "gpt-3.5-turbo",
      "messages": [
          {
              "role": "user",
              "content": text
          }
      ],
      "stream": False
  }
  headers = {"content-type": "application/json"}
  
  response = requests.request("POST", url, json=payload, headers=headers)
  
  print(response.text)
```

2.通过​powershell：
```powershell
$headers=@{}
$headers.Add("content-type", "application/json")
$response = Invoke-RestMethod -Uri '你的url/v1/chat/completions' -Method POST -Headers $headers -ContentType 'application/json' -Body '{
  "model": "gpt-3.5-turbo",
  "messages": [
    {
      "role": "user",
      "content": "需要输入的内容"
    }
  ],
  "stream": false
}'
```



唯一可惜的是华为云函数不支持HTTP流式传输，这意味着没有打字机效果，只能等待GPT的消息全部生成完成后才能回传，等待时延较长，勉强还是可以用的。可以关注小茜，小茜带领大家探索更多有趣的方案​！
