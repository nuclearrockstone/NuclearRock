# Selenium

[Bookmark](https://www.selenium.dev/)

![cd8a3cc3ca7f](/img/cd8a3cc3ca7f)

## 安装环境

- 安装WebDriver：下载对应浏览器的WebDriver，并添加到系统环境变量

- 安装Selenium：`pip install selenium`

- 测试脚本：弹出浏览器界面即为安装成功
    ```javascript
    from selenium import webdriver
    driver = webdriver.Chrome()
    ```

    VS Code会在弹出后自动结束脚本，可以在命令行中进行测试


## 浏览器驱动

开始会话

```javascript
driver = webdriver.Chrome()
```

结束会话

```javascript
driver.quit()
```

打开网页

```javascript
driver.get("url")
```

获取网页信息

```javascript
driver.title
```

## 定位器

```javascript
from selenium.webdriver.common.by import By
driver.find_element(locator,value)
```

| **属性** | **函数** |
| --- | --- |
| CLASS | find_element(by=By.CLASS_NAME, value=‘’) |
| XPATH | find_element(by=By.XPATH, value=‘’) |
| LINK_TEXT | find_element(by=By.LINK_TEXT, value=‘’) |
| PARTIAL_LINK_TEXT | find_element(by=By.PARTIAL_LINK_TEXT, value=‘’) |
| TAG | find_element(by=By.TAG_NAME, value=‘’) |
| CSS | find_element(by=By.CSS_SELECTOR, value=‘’) |
| ID | find_element(by=By.ID, value=‘’) |

## 交互

```javascript
from selenium.webdriver.common.action_chains import ActionChains
element.sent_keys()
```



