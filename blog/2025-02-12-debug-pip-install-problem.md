---
slug: Pip安装出现SSL
title: Python3.7/3.8环境下Pip安装出现SSL问题的解决方案
tags: [FixBug]
image: ./img/blog_social_card.jpg
---

在使用Conda创建Python3.7/3.8的环境时，使用Pip安装包，出现SSL错误，通过设置HTTPS代理解决

<!-- truncate -->

## 问题描述

在使用Conda创建Python3.7/3.8环境时，使用Pip安装包。出现SSL错误：
```
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLZeroReturnError(6, '
TLS/SSL connection has been closed (EOF) (_ssl.c:1149)'))': /simple/...
```
同时更高版本Python环境都可以正常安装包，经过查询得知该BUG引起的原因：

由于设置的系统代理不支持HTTPS，而Pip读取了系统代理参数后使用```HTTPS```代理进行下载导致错误

[参考自](https://kites.cc/p/python-pip-ssl-proxy-error/)

若关闭系统代理，Pip能够正常安装，则可以验证为该问题

## 问题解决

### 临时方案

直接指定使用```HTTP```代理

```
pip install --proxy http://127.0.0.1:%你使用的代理的端口% package
```


### 长期方案

修改对应虚拟环境的Pip配置文件，在对应的虚拟环境的文件夹下添加```pip.ini```文件（```%USERPROFILE%\.conda\envs\%virtual_env%```），在文件中添加下列内容：

```
[site]
proxy = http://127.0.0.1:%你使用的代理的端口%
```

即可解决问题