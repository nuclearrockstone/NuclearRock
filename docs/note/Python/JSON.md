---
title: JSON
---

# JSON

```javascript
import json

# 打开JSON文件
with open('data.json', 'r') as f:
    data = json.load(f)

# 处理数据
print(data)  # 打印整个JSON数据

# 例如，访问特定字段
print(data['key'])  # 替换 'key' 为你实际的键名

```



