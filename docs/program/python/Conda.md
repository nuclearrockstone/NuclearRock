---
title: Conda
description: 使用Conda进行Python包管理
toc_min_heading_level: 3
---
![Anaconda_banner](https://image.nuclearrockstone.xyz/2025/02/Anaconda_banner2.png)

**Conda是一种Python虚拟环境管理工具**，是目前较优的对Python进行虚拟环境管理的实践方式
## 安装

### 发行版选择

目前主流的发行版是Anaconda（南美蟒蛇）公司提供的Anaconda和miniconda两种，两种发行版都带有Python和Conda工具，两者的区别在于Anaconda自带有大量科学计算和机器学习需要的第三方库，例如NumPy等，且带有图形化的导航界面，因此安装包体积较大，而minconda则没有带有这些工具，除此之外两者几乎没有区别

### 环境变量配置
>以miniconda为例

从Anaconda网站上下载exe安装包并安装之后，需要手动对环境变量进行配置。在系统环境变量```Path```下添加如下三个路径：
```
%insatllpath%/miniconda3
%insatllpath%/miniconda3/Scripts
%insatllpath%/miniconda3/Library/bin
```
其中```%insatllpath%```应为你的conda的安装位置
### 验证安装

在命令行中输入conda，若出现相应命令，则安装成功

## 使用

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
**在WindowsTerminal中使用AnacondaPromt**

在```WindowsTerminal配置文件```中添加配置
```json title="PowershellPromt"
{
    "commandline": "%WINDIR%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -ExecutionPolicy ByPass -NoExit -Command \"& '%insatllpath%\\miniconda3\\shell\\condabin\\conda-hook.ps1' ; condaactivate '%insatllpath%\\miniconda3' \"",
    "guid": "{6de2fe5f-d6e3-bc1d-e10b-a25474ccdb41}",
    "hidden": false,
    "icon": "%path%\\Anaconda_Icon.png",
    "name": "miniconda3"
}
```

```json title="cmdPromt"
{
    "commandline": "%WINDIR%\\System32\\cmd.exe /K %insatllpath%\\miniconda3\\Scripts\\activate.bat %insatllpath%\\miniconda3",
    "guid": "{6de2fe5f-d6e3-bc1d-e10b-a25474ccdb41}",
    "hidden": false,
    "icon": "%path%\\Anaconda_Icon.png",
    "name": "miniconda3"
}
```