---
title: Conda
---

# Conda

**Conda是一种Python虚拟环境管理工具**，是目前较优的对Python进行虚拟环境管理的实践方式

### 安装

#### 发行版选择

目前主流的发行版是Anaconda（南美蟒蛇）公司提供的Anaconda和miniconda两种，两种发行版都带有Python和Conda工具，两者的区别在于Anaconda自带有大量科学计算和机器学习需要的第三方库，例如NumPy等，且带有图形化的导航界面，因此安装包体积较大，而minconda则没有带有这些工具，除此之外两者几乎没有区别

#### 环境变量配置

> 以miniconda为例

从Anaconda网站上下载exe安装包并安装之后，需要手动对环境变量进行配置。在系统环境变量`Path`下添加如下三个路径：

```plain text
%insatllpath%/miniconda3
%insatllpath%/miniconda3/Scripts
%insatllpath%/miniconda3/Library/bin
```

其中`%insatllpath%`应为你的conda的安装位置
### 验证安装

在命令行中输入conda，若出现相应命令，则安装成功

### 使用

#### 虚拟环境管理

**创建虚拟环境**

```powershell
conda create -n env_name
```

默认情况下，创建的虚拟环境是不包含python解释器的，因此直接使用容易产生报错

- 可以在创建虚拟环境是指定python版本
    ```powershell
    conda create -n env_name python=3.8
    ```


- 或者可以一劳永逸，设定在创建虚拟环境时自动安装python
    ```powershell
    conda config --add create_default_packages python
    ```


#### 在WindowsTerminal中使用AnacondaPromt

在`WindowsTerminal配置文件`中添加配置

使用Powershellpromt

```json
{     
	"commandline": "%WINDIR%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy ByPass -NoExit -Command \"& '%insatllpath%\\miniconda3\\shell\\condabin\\conda-hook.ps1' ; condaactivate '%insatllpath%\\miniconda3' \"",
	"guid": "{6de2fe5f-d6e3-bc1d-e10b-a25474ccdb41}",
	"hidden": false,
	"icon": "%path%\\Anaconda_Icon.png",
	"name": "miniconda3" 
}
```

使用CMDpromt

```json
 {     
	 "commandline": "%WINDIR%\\System32\\cmd.exe /K %insatllpath%\\miniconda3\\Scripts\\activate.bat %insatllpath%\\miniconda3",
	 "guid": "{6de2fe5f-d6e3-bc1d-e10b-a25474ccdb41}",
	 "hidden": false,
	 "icon": "%path%\\Anaconda_Icon.png",
	 "name": "miniconda3" 
 }
```

#### 解决conda base环境与之前安装的python环境冲突的问题

**问题描述**

如果你在安装conda之前已经安装了python，安装conda并添加环境变量后，即使不使用Anacondapromt，使用默认的Powershell和CMD，在命令行中调用python和pip，调用的为conda base环境中的python，这是因为在miniconda的路径下，既有conda程序，也有python和pip程序，因此覆盖了原有python的环境变量路径
>以我为例，在安装conda之前，已经在原有的python中进行了长时间的开发，因此已经在原有的python环境下安装了很多包，在使用conda后，试图使用`pip list`命令查看包的安装情况时遂发现此问题，此时在vscode等仍能识别的原有的python环境，但再向这个环境中使用`pip`安装包就显得很困难

**解决方案**

在环境变量中提高原有python路径的优先级，再系统变量中将原有的python路径置于conda路径之上

:::note 💡

正常情况下Windows的环境变量应该是系统变量大于用户变量的，但貌似Path是系统变量有限的，因为我原先Pyhton安装时添加的环境变量是添加在用户变量中的。。。。

::: 



