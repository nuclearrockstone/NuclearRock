---
title: Tex公式基础
description: Tex的入门编写指南
hide_table_of_contents: true
---

# 基本语法

## 语法

### 插入公式


基本的代数符号及字母只需正常输入并使用``$``进行标记即可

- 使用两个``$``将标记为行内公式
- 使用两组``$$``符号将标记为行间公式

Tex公式使用标识符控制格式和编辑内容


> 在标识符前后使用空格可以以提高阅读性和减少错误
>
> 公式编辑中的空格会被忽略，使用标识符``\quad``以实现空格效果



### 手动编号

使用标识符``\tag{}``可以对公式进行手动编号

## 示例

```
$ f(x)=a+b $
```

这是一个行内公式 $f(x)=a+b$

```
$$ f(x)=a+b \tag(1.1) $$
```

下方是一个手动编号的行间公式
$$
f(x)=a+b \tag{1.1}
$$

# 数学符号

## 运算标识符

|  名称   |     符号      |  标识符   |
| :-----: | :-----------: | :-------: |
|  点乘   |    $\cdot$    |   \cdot   |
| 不等于  |    $\neq$     |   \neq    |
| 恒等于  |   $\equiv$    |  \equiv   |
|  取模   |    $\bmod$    |   \bmod   |
| 平方根  |   $\sqrt2$    |   \sqrt   |
| n次方根 |  $\sqrt[4]2$  | \sqrt[n]  |
|  分式   | $\frac{x}{y}$ | \frac{}{} |
|  极限   |    $\lim$     |   \lim    |
|  积分   |    $\int$     |   \int    |
|  求和   |    $\sum$     |   \sum    |
|  连乘   |    $\prod$    |   \prod   |

## 标注标识符

| 名称 | 符号 | 标识符 |
| :--: | :--: | :--: |
| 上标 | $x^2$ | ^ |
| 下标 | $x_2$ | _ |
| 上横线 | $\overline{x+y}$ | \overline{} |
| 下横线 | $\underline{x+y}$ | \underline{} |
| 上大括号 | $\overbrace{1+2+3}$ | \overbrace{} |
| 下大括号 | $\underbrace{1+2+3}$ | \underbrace{} |
| 右向量 | $\vec{x} \quad \overrightarrow{x}$ | \vec&\overrightarrow |
| 左向量 | $\overleftarrow{x}$ | \overleftarrow |
| 基线三圆点 | $\ldots$ | \ldots |
| 居中三圆点 | $\cdots$ | \cdots |
| 垂直三圆点 | $\vdots$ | \vdots |
| 对角三圆点 | $\ddots$ | \ddots |
| 重音符号 | $\hat{x}$ | \hat{} |
| 重音符号 | $\bar{x}$ | \bar{} |
| 重音符号 | $\tilde{x}$ | \tilde{} |
| 指向箭头 | $\to$ | \to |
### 矩阵标识符
| abc | $$ \begin{equation}<br> \left[<br> \begin{array}{ccc}<br>     a_{11} & a_{12} & a_{13} \\<br>     a_{21} & a_{22} & a_{23} \\<br>     a_{31} & a_{32} & a_{33} <br> \end{array}<br> \right]        <br> \end{equation}$$ |
| --- | --- |
| abc |  |
## 示例

### 基础运算

```
$$ y=x*2+1-x \cdot y $$
```

$$ y=x*2+1-x\cdot y $$

```
$$ y \neq x \quad 1 \equiv 1 \quad 9 \bmod 2 =4 $$
```

$$ y \neq x \quad 1 \equiv 1 \quad 9 \bmod 2 =4 $$

### 微积分与上下标

```
$$ \lim_{x \to 0}x^{22}  \quad \int_{i=1}^{n}$$
```

$$ \lim_{x \to 0}x^{22} \quad \int_{i=1}^{n}$$

# 希腊字母

|      |      |      |      |
| ---- | ---- | ---- | ---- |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |

$$
x=y
$$

```python
import cv2
from matplotlib import pyplot as plt

queryImage = cv2.imread("1.jpg", 0)
trainingImage = cv2.imread("2.jpg", 0)

sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(queryImage, None)
kp2, des2 = sift.detectAndCompute(trainingImage, None)

FLANN_INDEX_KDTREE = 0
indexParams = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
searchParams = dict(checks=50)s
```

> This is a simple note
