---
title: Requests
---

# Requests

:::note 

**Tips**

    <details>
    <summary>学习资源</summary>

        *[video block not supported]*

    </details>

    <details>
    <summary>相关页面</summary>

        [Untitled Bookmark](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)

    </details>

    <details>
    <summary>目录</summary>

        *[table_of_contents block not supported]*

    </details>

::: 

## Reuqests概览

**Requests**是一个Python库，用于处理HTTP请求，解决了手动处理的繁琐过程，Response类用于存储HTTP请求返回的结果

[官方文档](https://docs.python-requests.org/en/latest/index.html#)

HTTP请求共有9种，使用到的主要方法有如下几种：

- **GET：**请求指定页面信息，并返回实体主体

- **POST：**向指定页面提交数据处理请求，数据被包含在请求中，例如修改表单或者上传文件等

使用`httpbin.org`可以模拟发起上述请求，并测试上述请求

[Untitled Bookmark](https://httpbin.org/)

## GET请求

`get()`方法可用于请求资源，例如获取页面（QueryPage），下载文件，登录网站等

```javascript
URL="https://httpbin.org/"
r=requests.get(URL)
>>> r
<Response [200]>
```

### 参数

```javascript
get(url,params,auth,timeout)
```

- `url`：统一资源定位符，请求资源的地址

- `params`：参数，传入类型为字典

- `auth`：传递登录信息，格式为列表

- `timeout`：页面延迟时间，超时返回500状态码

```javascript
#测试参数#
>>> payload={'page':1,'name':'history'}
>>> r=requests.get(URL+"/get",params=payload)
>>> r.url
'https://httpbin.org//get?page=1&name=history'
>>> r.json()
{'args': {'name': 'history', 'page': '1'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-65dd9257-3ea21e6828eb632f027704fd'}, 'origin': '23.226.8.69', 'url': 'https://httpbin.org/get?page=1&name=history'}
#测试登录#
>>> r=requests.get(URL+"/basic-auth/user/passwd",auth=('user','passwd'))
>>> r
<Response [200]>
>>> r=requests.get(URL+"/basic-auth/user/passwd",auth=('name','passwd'))
>>> r
<Response [401]>
#测试超时#
>>> r=requests.get(URL+"/delay/1",timeout=3)
>>> r
<Response [200]>
>>> r=requests.get(URL+"/delay/4",timeout=3)
Time Out Error
```

## **POST**请求

用于上传数据

## 处理Reuqests类的常用函数和属性

`r`为`reuqests`类的一个实例

| 使用方法 | 结果 | 作用 |
| --- | --- | --- |
| `dir(r)` |  | 返回对象可用的方法 |
| `help(r)` |  | 帮助 |
| `r.content` |  |  |
| `r.text` | 文本（若用于非文本文件会出现乱码） |  |
| `r.status_code` | 状态码 |  |
| `r.ok` | 布尔值 | 判断链接是否正常 |
| `r.headers` |  | 消息头 |
| `r.json()` | 字典 | 将返回的JSON数据变成字典数据 |

```javascript
>>> r=requests.get(URL+"/get",params=payload)
>>> dir(r)
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url'
>>> r.content
b'{\n  "args": {\n    "name": "history", \n    "page": "1"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.31.0", \n    "X-Amzn-Trace-Id": "Root=1-65dd94fa-3ccfa2fd79502b123584dc54"\n  }, \n  "origin": "23.226.8.69", \n  "url": "https://httpbin.org/get?page=1&name=history"\n}\n'
>>> r.text
'{\n  "args": {\n    "name": "history", \n    "page": "1"\n  }, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.31.0", \n    "X-Amzn-Trace-Id": "Root=1-65dd94fa-3ccfa2fd79502b123584dc54"\n  }, \n  "origin": "23.226.8.69", \n  "url": "https://httpbin.org/get?page=1&name=history"\n}\n'
>>> r.status_code
200
>>> r.ok
True
>>> r.headers
{'Date': 'Tue, 27 Feb 2024 07:53:30 GMT', 'Content-Type': 'application/json', 'Content-Length': '368', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
#访问字典中的值#
>>> r.json()['args']
{'name': 'history', 'page': '1'}
```

## 案例





